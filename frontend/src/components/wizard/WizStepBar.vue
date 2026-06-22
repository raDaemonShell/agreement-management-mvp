<template>
  <div class="wizard-steps" id="stepbar">
    <template v-for="(step, index) in steps" :key="step">
      <div class="wizard-step__item">
        <div class="wizard-step__dot" :class="dotClass(index + 1)">
          <i v-if="index + 1 < currentStep" class="ti ti-check"></i>

          <span v-else>
            {{ index + 1 }}
          </span>
        </div>

        <span class="wizard-step__label" :class="labelClass(index + 1)">
          {{ step }}
        </span>
      </div>

      <div v-if="index < steps.length - 1" class="wizard-step__conn"></div>
    </template>
  </div>
</template>

<script setup>
const props = defineProps({
  currentStep: Number,
})

const steps = ['Partner', 'Type', 'Details', 'Review', 'PDF Preview', 'Sign & Send']

function dotClass(step) {
  if (step < props.currentStep) return 'wizard-step__dot--done'

  if (step === props.currentStep) return 'wizard-step__dot--active'

  return 'wizard-step__dot--todo'
}

function labelClass(step) {
  if (step < props.currentStep) return 'wizard-step__label--done'

  if (step === props.currentStep) return 'wizard-step__label--active'

  return 'wizard-step__label--todo'
}
</script>
