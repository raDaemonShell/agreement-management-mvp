<template>
  <div class="card">
    <h2>Step 2: Agreement Type</h2>

    <div v-for="type in agreementTypes" :key="type.value" class="radio-item">
      <label>
        <input
          type="radio"
          name="agreement_type"
          v-model="agreementData.agreement_type"
          :value="type.value"
        />

        {{ type.label }}
      </label>
    </div>
  </div>
</template>

<script setup>
import { agreementData } from '../../stores/agreementStore'

const agreementTypes = [
  { label: 'NDA', value: 'NDA' },
  { label: 'MSA', value: 'MSA' },
  { label: 'Teaming Agreement', value: 'TEAMING' },
  { label: 'Subcontractor Agreement', value: 'SUBCONTRACTOR' },
  { label: 'Licensing Agreement', value: 'LICENSING' },
  { label: 'Letter Of Intent', value: 'LOI' },
  { label: 'Work Order', value: 'WORK_ORDER' },
]
</script>

<style scoped>
.card {
  padding: 20px;

  border: 1px solid #ddd;

  border-radius: 8px;
}

.radio-item {
  margin-bottom: 12px;
}
</style>
