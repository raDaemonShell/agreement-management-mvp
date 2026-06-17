<template>

<div class="card">

<h2>{{ title }}</h2>

<h1>{{ value }}</h1>

</div>

</template>

<script setup>

defineProps({

title: String,

value: Number,

})

</script>

<style scoped>

.card{

border:1px solid #ddd;

padding:20px;

border-radius:10px;

width:200px;

}

</style>