<template>
  <div class="field">
    <h3>Select Partner</h3>

    <select v-model="agreementData.counterparty_company">
      <option value="">Select Partner</option>

      <option v-for="partner in partners" :key="partner.id" :value="partner.company_name">
        {{ partner.company_name }}
      </option>
    </select>
  </div>
</template>

<style scoped>
.field {
  display: flex;

  flex-direction: column;

  margin-bottom: 20px;
}

select {
  width: 100%;

  max-width: 400px;

  padding: 10px;

  border: 1px solid #ccc;

  border-radius: 6px;

  font-size: 14px;
}
</style>

<script setup>
import { ref, onMounted } from 'vue'
import { agreementData } from '../../stores/agreementStore'
import api from '../../services/api'

const partners = ref([])

async function loadPartners() {
  try {
    const response = await api.get('/partners/')
    partners.value = response.data
  } catch (error) {
    console.error('Error fetching partners:', error)
  }
}

onMounted(() => {
  loadPartners()
})
</script>
