<template>
  <div class="nav-footer">
    <span class="nav-counter">Screen {{ currentStep }} of {{ totalSteps }}</span>
    <div class="d-flex gap-2">
      <button
        class="vm-btn"
        @click="$emit('back')"
        :disabled="currentStep === 1"
        :style="{ opacity: currentStep === 1 ? 0.4 : 1 }"
      >
        <i class="ti ti-arrow-left"></i> Back
      </button>
      <button
        class="vm-btn vm-btn--primary"
        @click="$emit('next')"
        :disabled="currentStep === totalSteps"
        :style="{ opacity: currentStep === totalSteps ? 0.4 : 1 }"
      >
        Next screen <i class="ti ti-arrow-right"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  currentStep: Number,
  totalSteps: Number,
})

defineEmits(['next', 'back'])
</script>
