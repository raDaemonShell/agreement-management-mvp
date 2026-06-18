<template>
  <div class="container">
    <h1>Agreement Dashboard</h1>

    <div class="actions">
      <button @click="goToWizard">+ New Agreement</button>

      <button @click="goToAgreementList">View Agreements</button>
    </div>

    <div class="stats">
      <StatCard title="Draft" :value="summary.draft" />

      <StatCard title="Awaiting Signature" :value="summary.awaiting_signature" />

      <StatCard title="Signed" :value="summary.signed" />
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 1000px;

  margin: auto;

  padding: 30px;
}

h1 {
  margin-bottom: 30px;
}

.actions {
  display: flex;

  gap: 15px;

  margin-bottom: 30px;
}

button {
  padding: 10px 16px;

  cursor: pointer;
}

.stats {
  display: flex;

  gap: 20px;

  flex-wrap: wrap;
}
</style>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'
import StatCard from '../components/StatCard.vue'

const router = useRouter()
const summary = ref({
  draft: 0,

  awaiting_signature: 0,

  signed: 0,
})

function goToAgreementList() {
  router.push('/agreements')
}

function goToWizard() {
  router.push('/agreement/new')
}

async function loadDashboard() {
  const response = await api.get('dashboard/')

  summary.value = response.data
}

onMounted(() => {
  loadDashboard()
})
</script>
