<template>

<div>

<h3>Initiator Information</h3>

<input
v-model="agreementData.initiator_name"
placeholder="Your Name"
/>

<input
v-model="agreementData.initiator_title"
placeholder="Your Title"
/>

<br><br>

<h3>Counterparty Information</h3>

<input
v-model="agreementData.counterparty_contact_name"
placeholder="Contact Name"
/>

<input
v-model="agreementData.counterparty_contact_title"
placeholder="Contact Title"
/>

<input
v-model="agreementData.counterparty_email"
placeholder="Email"
/>

<input
v-model="agreementData.counterparty_phone"
placeholder="Phone"
/>

</div>

</template>

<script setup>

import { agreementData } from '../../stores/agreementStore'

</script>