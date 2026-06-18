<template>
  <div class="container">
    <h1>All Agreements</h1>

    <table>
      <thead>
        <tr>
          <th>Title</th>

          <th>Company</th>

          <th>Type</th>

          <th>Status</th>

          <th>Created</th>

          <th>Action</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="agreement in agreements" :key="agreement.id">
          <td>
            {{ agreement.title }}
          </td>

          <td>
            {{ agreement.counterparty_company }}
          </td>

          <td>
            {{ agreement.agreement_type }}
          </td>

          <td>
            {{ formatStatus(agreement.status) }}
          </td>
          <td>
            {{ formatDate(agreement.created_at) }}
          </td>

          <td>
            <button @click="viewAgreement(agreement.id)">View</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.container {
  max-width: 1000px;

  margin: auto;

  padding: 20px;
}

table {
  width: 100%;

  border-collapse: collapse;

  margin-top: 20px;
}

th {
  padding: 12px;

  text-align: left;

  border-bottom: 2px solid #ddd;
}

td {
  padding: 12px;

  border-bottom: 1px solid #ddd;
}

button {
  padding: 8px 14px;

  cursor: pointer;
}

tr:hover {
  background: #f5f5f5;
}
</style>

<script setup>
import { useRouter } from 'vue-router'
import { formatStatus } from '../utils/formatters'
import { formatDate } from '../utils/formatters'
import { ref, onMounted } from 'vue'
import api from '../services/api'

const router = useRouter()
const agreements = ref([])

function viewAgreement(id) {
  router.push(`/agreements/${id}`)
}

async function loadAgreements() {
  const response = await api.get('/agreements/')

  agreements.value = response.data
}

onMounted(() => {
  loadAgreements()
})
</script>
