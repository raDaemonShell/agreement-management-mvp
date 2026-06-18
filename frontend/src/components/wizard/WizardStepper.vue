<template>
  <div class="steps">
    <div v-for="step in steps" :key="step.id" class="step">
      {{ step.id }}

      {{ step.name }}
    </div>
  </div>
</template>

<script setup>
const steps = [
  { id: 1, name: 'Select Partner' },

  { id: 2, name: 'Agreement Type' },

  { id: 3, name: 'Agreement Details' },

  { id: 4, name: 'Review' },

  { id: 5, name: 'PDF Preview' },

  { id: 6, name: 'Sign & Send' },
]
</script>

<style scoped>
.steps {
  display: flex;

  gap: 10px;

  margin-bottom: 30px;

  flex-wrap: wrap;
}

.step {
  padding: 10px 15px;

  border: 1px solid #ddd;

  border-radius: 20px;
}
</style>
