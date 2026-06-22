<template>
  <div class="wizard-footer">
    <span class="wizard-counter"> Step {{ currentStep }} of 7 </span>

    <div class="d-flex gap-2">
      <button
        class="vm-btn"
        @click="$emit('previous')"
        :disabled="currentStep === 1"
        :style="{
          opacity: currentStep === 1 ? 0.4 : 1,
        }"
      >
        <i class="ti ti-arrow-left"></i>

        Back
      </button>

      <button class="vm-btn vm-btn--primary" @click="$emit('next')">
        {{ nextButtonText }}

        <i class="ti ti-arrow-right"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentStep: Number,
})

defineEmits(['next', 'previous'])

const nextButtonText = computed(() => {
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

function nextStep() {
  if (currentStep.value < 7) {
    currentStep.value++
  } else {
    currentStep.value = 1
  }
}
</script>
