<template>
  <div class="guest-layout" v-if="agreement">
    <HeaderBar />
    <StepperBar :currentStep="currentStep" />

    <EmailView v-if="currentStep === 1" :agreement="agreement" @next="currentStep++" />
    <ReviewView v-if="currentStep === 2" :agreement="agreement" @next="currentStep++" />
    <IdentityView v-if="currentStep === 3" :agreement="agreement" @next="currentStep++" />
    <SignView v-if="currentStep === 4" :agreement="agreement" @next="currentStep++" />
    <ExecutedView v-if="currentStep === 5" :agreement="agreement" />

    <FootBarView
      :currentStep="currentStep"
      :totalSteps="5"
      @next="currentStep++"
      @back="currentStep--"
    />
  </div>

  <div v-else-if="loading" style="padding: 40px; text-align: center; color: var(--neutral-6)">
    Loading agreement...
  </div>

  <div v-else style="padding: 40px; text-align: center; color: var(--neutral-6)">
    Agreement not found.
  </div>
</template>

<script setup>
import '../assets/guest.css'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

import HeaderBar from '../components/guest/HeaderBar.vue'
import StepperBar from '../components/guest/StepperBar.vue'
import EmailView from '../components/guest/EmailView.vue'
import ReviewView from '../components/guest/ReviewView.vue'
import IdentityView from '../components/guest/IdentityView.vue'
import SignView from '../components/guest/SignView.vue'
import ExecutedView from '../components/guest/ExecutedView.vue'
import FootBarView from '../components/guest/FootBarView.vue'

const route = useRoute()
const agreement = ref(null)
const loading = ref(true)
const currentStep = ref(1)

const API_URL = 'http://127.0.0.1:8000/api'

onMounted(async () => {
  try {
    const response = await fetch(`${API_URL}/agreements/${route.params.id}/`)
    if (!response.ok) throw new Error('Not found')
    agreement.value = await response.json()
  } catch {
    agreement.value = null
  } finally {
    loading.value = false
  }
})
</script>
