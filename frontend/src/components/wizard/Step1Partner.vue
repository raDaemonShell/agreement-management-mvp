<template>
  <div>
    <h2>Step 1: Select Partner</h2>

    <PartnerList />
    <br />
    <PartnerForm />

    <hr />

    <h3>Current Data</h3>
    <pre>{{ agreementData }}</pre>
  </div>
</template>

<script setup>
import PartnerList from '../partner/PartnerList.vue';
import PartnerForm from '../partner/PartnerForm.vue';
import { agreementData } from '../../stores/agreementStore';
</script>
