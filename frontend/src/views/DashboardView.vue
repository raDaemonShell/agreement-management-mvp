<template>

<div>

<h1>Agreement Dashboard</h1>

<button @click="goToWizard">

+ New Agreement

</button>

<div class="stats">

<StatCard

title="Draft"

:value="summary.draft"

/>

<StatCard

title="Awaiting Signature"

:value="summary.awaiting_signature"

/>

<StatCard

title="Signed"

:value="summary.signed"

/>

</div>

</div>

</template>

<script setup>

import { ref, onMounted } from 'vue'

import { useRouter } from 'vue-router'

import api from '../services/api'

import StatCard from '../components/StatCard.vue'

const router = useRouter()

function goToWizard(){

router.push('/agreement/new')

}

const summary = ref({

draft:0,

awaiting_signature:0,

signed:0,

})

async function loadDashboard(){

const response = await api.get('dashboard/')

summary.value = response.data

}

onMounted(() => {

loadDashboard()

})

</script>

<style scoped>

.stats{

display:flex;

gap:20px;

}

</style>