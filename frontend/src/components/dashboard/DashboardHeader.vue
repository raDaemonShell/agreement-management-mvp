<template>
  <div class="d-flex align-center justify-space-between mb-5">
    <h1 class="fw-700" style="font-size: 20px; color: var(--neutral-12)">Agreements</h1>
    <button class="vm-btn vm-btn--primary" @click="goToWizard">+ New Agreement</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goToWizard() {
  router.push('/agreement/new')
}
</script>
