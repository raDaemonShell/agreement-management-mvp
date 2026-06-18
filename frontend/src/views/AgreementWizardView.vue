<template>
  <div>
    <h1>Create New Agreement</h1>

    <WizardStepper />

    <hr />

    <Step1Partner v-if="currentStep === 1" />

    <Step2AgreementType v-if="currentStep === 2" />

    <Step3AgreementDetails v-if="currentStep === 3" />

    <Step4Review v-if="currentStep === 4" />

    <Step5PdfPreview v-if="currentStep === 5" />

    <Step6SignSend v-if="currentStep === 6" />

    <div class="buttons">
      <button @click="previousStep">Back</button>

      <button @click="nextStep">Next</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import WizardStepper from '../components/wizard/WizardStepper.vue'

import Step1Partner from '../components/wizard/Step1Partner.vue'

import Step2AgreementType from '../components/wizard/Step2AgreementType.vue'

import Step3AgreementDetails from '../components/wizard/Step3AgreementDetails.vue'

import Step4Review from '../components/wizard/Step4Review.vue'

import Step5PdfPreview from '../components/wizard/Step5PdfPreview.vue'

import Step6SignSend from '../components/wizard/Step6SignSend.vue'

const currentStep = ref(1)

function nextStep() {
  if (currentStep.value < 6) {
    currentStep.value++
  }
}

function previousStep() {
  if (currentStep.value > 1) {
    currentStep.value--
  }
}
</script>

<style scoped>
.buttons {
  margin-top: 30px;

  display: flex;

  gap: 10px;
}
</style>
