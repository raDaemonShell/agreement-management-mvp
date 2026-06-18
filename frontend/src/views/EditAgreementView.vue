<template>
  <div class="container">
    <div class="card">
      <h1>Edit Agreement</h1>

      <div class="field">
        <label>Title</label>

        <input v-model="agreement.title" />
      </div>

      <div class="field">
        <label>Counterparty Company</label>

        <input v-model="agreement.counterparty_company" />
      </div>

      <div class="field">
        <label>Counterparty Email</label>

        <input v-model="agreement.counterparty_email" />
      </div>

      <button @click="saveAgreement">Save Changes</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;

  justify-content: center;

  padding: 30px;
}

.card {
  width: 500px;

  padding: 25px;

  border: 1px solid #ddd;

  border-radius: 8px;
}

.field {
  display: flex;

  flex-direction: column;

  margin-bottom: 20px;
}

label {
  margin-bottom: 8px;

  font-weight: bold;
}

input {
  padding: 10px;

  font-size: 16px;
}

button {
  padding: 10px 16px;

  cursor: pointer;
}
</style>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/api'

const router = useRouter()

const route = useRoute()

const agreement = ref({})

async function loadAgreement() {
  const response = await api.get(`/agreements/${route.params.id}/`)

  agreement.value = response.data
}

function validateAgreement() {
  if (!agreement.value.title) {
    alert('Title is required')

    return false
  }

  if (!agreement.value.counterparty_company) {
    alert('Company is required')

    return false
  }

  if (!agreement.value.counterparty_email) {
    alert('Email is required')

    return false
  }

  return true
}

async function saveAgreement() {
  if (!validateAgreement()) {
    return
  }

  await api.patch(
    `/agreements/${route.params.id}/`,

    agreement.value,
  )

  alert('Agreement updated')

  router.push(`/agreements/${route.params.id}`)
}

onMounted(() => {
  loadAgreement()
})
</script>
