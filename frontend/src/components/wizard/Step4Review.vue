<template>

<div>

<h2>Step 4: Review Agreement</h2>

<hr>

<h3>Partner</h3>

<p>{{ agreementData.partner }}</p>

<hr>

<h3>Initiator</h3>

<p>Name: {{ agreementData.initiator_name }}</p>

<p>Title: {{ agreementData.initiator_title }}</p>

<hr>

<h3>Counterparty</h3>

<p>Name: {{ agreementData.counterparty_name }}</p>

<p>Title: {{ agreementData.counterparty_title }}</p>

<p>Email: {{ agreementData.counterparty_email }}</p>

<p>Phone: {{ agreementData.counterparty_phone }}</p>

<hr>

<h3>Agreement Type</h3>

<p>{{ agreementData.agreement_type }}</p>

<hr>

<h3>Agreement Details</h3>

<p>Purpose: {{ agreementData.purpose }}</p>

<p>IP Protection: {{ agreementData.ip_protection }}</p>

<p>Governing Law: {{ agreementData.governing_law }}</p>

<p>Start Date: {{ agreementData.start_date }}</p>

<p>End Date: {{ agreementData.end_date }}</p>

<p>Duration: {{ agreementData.duration }} days</p>

<hr>

<div class="disclaimer">

<h3>Disclaimer</h3>

<p>

Varmodel is not a law firm and does not provide legal advice.

Users are encouraged to consult an attorney before executing agreements.

Varmodel is not liable for omitted terms.

</p>

</div>

</div>

</template>

<script setup>

import { agreementData }

from '../../stores/agreementStore'

</script>

<style scoped>

.disclaimer{

padding:15px;

border:1px solid gray;

margin-top:20px;

}

</style>