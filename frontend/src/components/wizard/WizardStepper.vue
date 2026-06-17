<template>

<div class="steps">

<div
v-for="step in steps"
:key="step.id"
>

{{ step.id }}. {{ step.name }}

</div>

</div>

</template>

<script setup>

const steps = [

{ id:1, name:'Select Partner' },

{ id:2, name:'Agreement Type' },

{ id:3, name:'Agreement Details' },

{ id:4, name:'Review' },

{ id:5, name:'PDF Preview' },

{ id:6, name:'Sign & Send' },

]

</script>

<style scoped>

.steps{

display:flex;

gap:20px;

margin-bottom:30px;

}

</style>