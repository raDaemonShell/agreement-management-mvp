<template>
  <div class="container">
    <h1>Agreement Details</h1>

    <div>
      <h3>Basic Information</h3>
      <p><strong>Title:</strong> {{ agreement.title }}</p>
      <p><strong>Company:</strong> {{ agreement.counterparty_company }}</p>
      <p><strong>Agreement Type:</strong> {{ agreement.agreement_type }}</p>
      <p><strong>Status:</strong> {{ agreement.status }}</p>

      <hr />

      <h3>Initiator</h3>
      <p>{{ agreement.initiator_name }}</p>
      <p>{{ agreement.initiator_title }}</p>

      <hr />

      <h3>Counterparty</h3>
      <p>{{ agreement.counterparty_contact_name }}</p>
      <p>{{ agreement.counterparty_contact_title }}</p>
      <p>{{ agreement.counterparty_email }}</p>

      <hr />

      <h3>Dates</h3>
      <p>Start: {{ agreement.start_date }}</p>
      <p>End: {{ agreement.end_date }}</p>

      <hr />

      <div class="actions">
        <button @click="editAgreement">Edit Agreement</button>

        <button @click="deleteAgreement">Delete Agreement</button>

        <button @click="updateStatus('SENT')">Send Agreement</button>

        <button @click="updateStatus('SIGNED')">Mark Signed</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;

  margin: auto;

  padding: 20px;
}

.actions {
  display: flex;

  gap: 10px;

  margin-top: 20px;
}

button {
  padding: 10px 16px;

  cursor: pointer;
}
</style>

<style scoped>
.actions {
  display: flex;

  gap: 10px;

  margin-top: 20px;
}
</style>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import api from '../services/api'

const route = useRoute()

const router = useRouter()

const agreement = ref({})

function editAgreement() {
  router.push(`/agreements/${route.params.id}/edit`)
}

async function deleteAgreement() {
  const confirmed = confirm('Delete this agreement?')

  if (!confirmed) {
    return
  }

  try {
    await api.delete(`/agreements/${route.params.id}/`)

    alert('Agreement deleted')

    router.push('/agreements')
  } catch (error) {
    console.log(error)
  }
}

async function updateStatus(newStatus) {
  try {
    await api.patch(
      `/agreements/${route.params.id}/`,

      {
        status: newStatus,
      },
    )

    loadAgreement()

    alert('Status updated')
  } catch (error) {
    console.log(error)
  }
}

async function loadAgreement() {
  const response = await api.get(`/agreements/${route.params.id}/`)

  agreement.value = response.data
}

onMounted(() => {
  loadAgreement()
})
</script>
