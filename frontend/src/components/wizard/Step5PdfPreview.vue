<template>

<div>

<h2>Step 5: PDF Preview</h2>

<div class="pdf">

<h1>Agreement Preview</h1>

<hr>

<h3>Partner</h3>

<p>{{ agreementData.partner }}</p>

<hr>

<h3>Initiator</h3>

<p>

{{ agreementData.initiator_name }}

-

{{ agreementData.initiator_title }}

</p>

<hr>

<h3>Counterparty</h3>

<p>

{{ agreementData.counterparty_name }}

-

{{ agreementData.counterparty_title }}

</p>

<p>

{{ agreementData.counterparty_email }}

</p>

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

<h3>Signature Area</h3>

<p>Initiator: __________________</p>

<p>Counterparty: Awaiting signature</p>

</div>

</div>

</template>

<script setup>

import { agreementData }

from '../../stores/agreementStore'

</script>

<style scoped>

.pdf{

border:1px solid gray;

padding:25px;

background:white;

}

</style>