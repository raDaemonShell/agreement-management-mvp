<template>
  <div class="card">
    <h2>Step 4: Review Agreement</h2>

    <div class="section">
      <h3>Partner</h3>

      <p>{{ agreementData.counterparty_company }}</p>
    </div>

    <div class="section">
      <h3>Initiator</h3>

      <p>Name: {{ agreementData.initiator_name }}</p>

      <p>Title: {{ agreementData.initiator_title }}</p>
    </div>

    <div class="section">
      <h3>Counterparty</h3>

      <p>Name: {{ agreementData.counterparty_contact_name }}</p>

      <p>Title: {{ agreementData.counterparty_contact_title }}</p>

      <p>Email: {{ agreementData.counterparty_email }}</p>

      <p>Phone: {{ agreementData.counterparty_phone }}</p>
    </div>

    <div class="section">
      <h3>Agreement Type</h3>

      <p>{{ agreementData.agreement_type }}</p>
    </div>

    <div class="section">
      <h3>Agreement Details</h3>

      <p>Purpose: {{ agreementData.purpose }}</p>

      <p>IP Protection: {{ agreementData.ip_protection }}</p>

      <p>Governing Law: {{ agreementData.governing_law }}</p>

      <p>Start Date: {{ agreementData.start_date }}</p>

      <p>End Date: {{ agreementData.end_date }}</p>

      <p>Duration: {{ agreementData.duration }} days</p>
    </div>

    <div class="disclaimer">
      <h3>Disclaimer</h3>

      <p>
        Varmodel is not a law firm and does not provide legal advice. Users are encouraged to
        consult an attorney before executing agreements. Varmodel is not liable for omitted terms.
      </p>
    </div>
  </div>
</template>

<script setup>
import { agreementData } from '../../stores/agreementStore'
</script>

<style scoped>
.card {
  padding: 20px;

  border: 1px solid #ddd;

  border-radius: 8px;

  background: white;
}

.section {
  margin-bottom: 25px;

  padding-bottom: 15px;

  border-bottom: 1px solid #ddd;
}

.disclaimer {
  padding: 15px;

  border: 1px solid #ddd;

  border-radius: 8px;

  background: #fafafa;
}
</style>
