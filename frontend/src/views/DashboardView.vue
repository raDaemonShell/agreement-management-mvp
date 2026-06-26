<template>
  <div class="app-main">
    <div class="page">
      <DashboardHeader />

      <DashboardStatGrid :summary="summary" />

      <DashboardTabs
        :active-tab="activeTab"
        :summary="summary"
        @change-tab="activeTab = $event"
        :totalCount="totalCount"
      />

      <DashboardTable :agreements="filteredAgreements" />
    </div>
  </div>
</template>

<script setup>
import { API_URL } from '../services/api'
import DashboardHeader from '../components/dashboard/DashboardHeader.vue'
import DashboardStatGrid from '../components/dashboard/DashboardStatGrid.vue'
import DashboardTabs from '../components/dashboard/DashboardTabs.vue'
import DashboardTable from '../components/dashboard/DashboardTable.vue'
import { ref, onMounted, computed } from 'vue'

async function loadDashboard() {
  const response = await fetch(`${API_URL}/dashboard/`)
  summary.value = await response.json()
}
async function loadAgreements() {
  const response = await fetch(`${API_URL}/agreements/`)
  agreements.value = await response.json()
}

const activeTab = ref('ALL')
const agreements = ref([])

const summary = ref({
  draft: 0,

  awaiting_signature: 0,

  signed: 0,
})

const totalCount = computed(
  () => summary.value.draft + summary.value.awaiting_signature + summary.value.signed,
)

const filteredAgreements = computed(() => {
  if (activeTab.value === 'ALL') {
    return agreements.value
  }

  return agreements.value.filter((agreement) => agreement.status === activeTab.value)
})

onMounted(() => {
  loadDashboard()
})
onMounted(() => {
  loadAgreements()
})
</script>
