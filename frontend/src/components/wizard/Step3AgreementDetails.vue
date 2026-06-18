<template>
  <div class="card">
    <h2>Step 3: Agreement Details</h2>

    <div class="field">
      <label>Purpose</label>

      <input v-model="agreementData.purpose" placeholder="Agreement purpose" />
    </div>

    <div class="field">
      <label>IP Protection</label>

      <select v-model="agreementData.ip_protection">
        <option value="">Select</option>

        <option>Yes</option>

        <option>No</option>
      </select>
    </div>

    <div class="field">
      <label>Governing Law</label>

      <input v-model="agreementData.governing_law" placeholder="Country or State" />
    </div>

    <div class="field">
      <label>Start Date</label>

      <input type="date" v-model="agreementData.start_date" />
    </div>

    <div class="field">
      <label>End Date</label>

      <input type="date" v-model="agreementData.end_date" @change="calculateDuration" />
    </div>

    <h3>
      Duration:

      {{ agreementData.duration }}

      days
    </h3>
  </div>
</template>

<script setup>
import { agreementData } from '../../stores/agreementStore'

function calculateDuration() {
  if (agreementData.start_date && agreementData.end_date) {
    const start = new Date(agreementData.start_date)

    const end = new Date(agreementData.end_date)

    const difference = end - start

    agreementData.duration = Math.ceil(difference / (1000 * 60 * 60 * 24))
  }
}
</script>

<style scoped>
.card {
  padding: 20px;

  border: 1px solid #ddd;

  border-radius: 8px;
}

.field {
  display: flex;

  flex-direction: column;

  margin-bottom: 20px;
}

input,
select {
  width: 300px;

  padding: 10px;

  border: 1px solid #ccc;

  border-radius: 6px;

  font-size: 14px;
}
</style>
