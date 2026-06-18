<template>
  <div class="card">
    <h3>
      {{ title }}
    </h3>

    <p>
      {{ value }}
    </p>
  </div>
</template>

<script setup>
defineProps({
  title: String,

  value: Number,
})
</script>

<style scoped>
.card {
  width: 220px;

  padding: 20px;

  border: 1px solid #ddd;

  border-radius: 8px;
}

h3 {
  margin-bottom: 10px;
}

p {
  font-size: 28px;

  font-weight: bold;
}
</style>
