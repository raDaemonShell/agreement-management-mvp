<template>

<div>

<h2>Step 6: Sign & Send</h2>

<hr>

<h3>Initiator Signature</h3>

<input

v-model="agreementData.initiator_signature"

placeholder="Type your full name"

/>

<br><br>

<h3>Recipient Email</h3>

<input

v-model="agreementData.counterparty_email"

placeholder="Recipient Email"

/>

<br><br>

<h3>Expiry Window</h3>

<select v-model="agreementData.expiry_days">

<option :value="3">3 Days</option>

<option :value="7">7 Days</option>

<option :value="14">14 Days</option>

</select>

<hr>

<h3>Current Data</h3>

<pre>

{{ agreementData }}

</pre>

<button @click="submitAgreement">

Create Agreement

</button>

</div>

</template>

<script setup>

import api from '../../services/api'
import { agreementData } from '../../stores/agreementStore';

async function submitAgreement() {
  try {
    const payload = {
      title: `${agreementData.agreement_type} Agreement`,
      agreement_type: agreementData.agreement_type,
      initiator_name: agreementData.initiator_name,
      initiator_title: agreementData.initiator_title,
      counterparty_company: agreementData.counterparty_company,
      counterparty_contact_name: agreementData.counterparty_contact_name,
      counterparty_contact_title: agreementData.counterparty_contact_title,
      counterparty_email: agreementData.counterparty_email,
      start_date: agreementData.start_date,
      end_date: agreementData.end_date,
    };

    const response = await api.post('/agreements/', payload);

    console.log(response.data);
    alert('Agreement saved successfully');
  } catch (error) {
    console.error(error)

    console.log(error.response)

    console.log(error.response.data)

    alert(JSON.stringify(error.response.data))
  }
}
</script>