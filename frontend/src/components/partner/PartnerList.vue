<template>
  <div>
    <h3>Select Partner</h3>
    <select v-model="agreementData.counterparty_company">
      <option value="">Select Partner</option>
      <option
        v-for="partner in partners"
        :key="partner.id"
        :value="partner.company_name"
        >
        {{ partner.company_name }}
      </option>
    </select>
  </div>
</template>

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
