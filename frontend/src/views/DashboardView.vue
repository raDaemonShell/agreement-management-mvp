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
import DashboardHeader from '../components/dashboard/DashboardHeader.vue'
import DashboardStatGrid from '../components/dashboard/DashboardStatGrid.vue'
import DashboardTabs from '../components/dashboard/DashboardTabs.vue'
import DashboardTable from '../components/dashboard/DashboardTable.vue'
import { ref, onMounted, computed } from 'vue'
import api from '../services/api'

async function loadDashboard() {
  const response = await api.get('dashboard/')

  summary.value = response.data
}
async function loadAgreements() {
  const response = await api.get('/agreements/')

  agreements.value = response.data
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
