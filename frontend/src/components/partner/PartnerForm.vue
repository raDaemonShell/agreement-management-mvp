<template>
  <div>
    <div class="field">
      <label>Initiator Name</label>

      <input v-model="agreementData.initiator_name" placeholder="Your Name" />
    </div>

    <div class="field">
      <label>Initiator Title</label>

      <input v-model="agreementData.initiator_title" placeholder="Your Title" />
    </div>

    <div class="field">
      <label>Contact Name</label>

      <input v-model="agreementData.counterparty_contact_name" placeholder="Contact Name" />
    </div>

    <div class="field">
      <label>Contact Title</label>

      <input v-model="agreementData.counterparty_contact_title" placeholder="Contact Title" />
    </div>

    <div class="field">
      <label>Email</label>

      <input v-model="agreementData.counterparty_email" placeholder="Email" />
    </div>

    <div class="field">
      <label>Phone</label>

      <input v-model="agreementData.counterparty_phone" placeholder="Phone" />
    </div>
  </div>
</template>

<style scoped>
.field {
  display: flex;

  flex-direction: column;

  margin-bottom: 20px;
}

input {
  width: 100%;

  max-width: 400px;

  padding: 10px;

  border: 1px solid #ccc;

  border-radius: 6px;

  font-size: 14px;
}
</style>

<script setup>
import { agreementData } from '../../stores/agreementStore'
</script>
