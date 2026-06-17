<template>
  <div>
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

    <hr />

    <pre>{{ agreementData }}</pre>
  </div>
</template>

<script setup>
import { agreementData } from '../../stores/agreementStore';

const agreementTypes = [
  { label:'NDA', value:'NDA' },
  { label:'MSA', value:'MSA' },
  { label:'Teaming Agreement', value:'TEAMING' },
  { label:'Subcontractor Agreement', value:'SUBCONTRACTOR' },
  { label:'Licensing Agreement', value:'LICENSING' },
  { label:'Letter Of Intent', value:'LOI' },
  { label:'Work Order', value:'WORK_ORDER' },
];
</script>

<style scoped>
/* Add your styles here */
.radio-item {
  margin-bottom: 0.5rem;
}
</style>
