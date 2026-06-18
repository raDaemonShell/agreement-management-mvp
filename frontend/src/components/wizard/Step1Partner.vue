<template>
  <div class="card">
    <h2>Step 1: Select Partner</h2>

    <PartnerList />

    <PartnerForm />
  </div>
</template>

<script setup>
import PartnerList from '../partner/PartnerList.vue'
import PartnerForm from '../partner/PartnerForm.vue'
</script>

<style scoped>
.card {
  padding: 20px;

  border: 1px solid #ddd;

  border-radius: 8px;
}
</style>
