<template>
  <div class="wizard-footer">
    <span class="wizard-counter">Step {{ currentStep }} of 7</span>
    <div class="d-flex gap-2">
      <button
        class="vm-btn"
        @click="$emit('previous')"
        :disabled="currentStep === 1"
        :style="{ opacity: currentStep === 1 ? 0.4 : 1 }"
      >
        <i class="ti ti-arrow-left"></i> Back
      </button>

      <button
        class="vm-btn vm-btn--primary"
        @click="$emit('next')"
        :disabled="isGenerating"
        :style="{ opacity: isGenerating ? 0.7 : 1 }"
      >
        <i v-if="isGenerating" class="ti ti-loader" style="animation: spin 1s linear infinite"></i>
        {{ nextButtonText }}
        <i v-if="!isGenerating" class="ti ti-arrow-right"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, inject, ref } from 'vue'

const props = defineProps({
  currentStep: Number,
})

defineEmits(['next', 'previous'])

const generating = inject('generating', ref(false))

const isGenerating = computed(() => generating.value)

const nextButtonText = computed(() => {
  if (isGenerating.value) {
    if (props.currentStep === 3) return 'Generating...'
    if (props.currentStep === 4) return 'Preparing PDF...'
    if (props.currentStep === 6) return 'Sending...'
  }

  switch (props.currentStep) {
    case 3:
      return 'Generate agreement'
    case 4:
      return 'PDF Preview'
    case 5:
      return 'Continue to signing'
    case 6:
      return 'Send for signature'
    case 7:
      return 'New agreement'
    default:
      return 'Continue'
  }
})
</script>

<style scoped>
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
