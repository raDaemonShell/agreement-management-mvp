<template>
  <div class="stepper">
    <template v-for="(step, index) in steps" :key="step.label">
      <div class="step-item">
        <div
          class="step-dot"
          :class="{
            'step-dot--done': currentStep > step.number,
            'step-dot--active': currentStep === step.number,
            'step-dot--todo': currentStep < step.number,
          }"
        >
          <i v-if="currentStep > step.number" class="ti ti-check" style="font-size: 10px"></i>
          <span v-else>{{ step.number }}</span>
        </div>
        <span
          class="step-label"
          :class="{
            'step-label--done': currentStep > step.number,
            'step-label--active': currentStep === step.number,
            'step-label--todo': currentStep < step.number,
          }"
        >
          {{ step.label }}
        </span>
      </div>
      <div v-if="index < steps.length - 1" class="step-conn"></div>
    </template>
  </div>
</template>

<script setup>
defineProps({
  currentStep: Number,
})

const steps = [
  { number: 1, label: 'Email received' },
  { number: 2, label: 'Review agreement' },
  { number: 3, label: 'Verify identity' },
  { number: 4, label: 'Sign' },
  { number: 5, label: 'Executed' },
]
</script>
