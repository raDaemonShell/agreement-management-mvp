<template>
  <div class="stat-grid">
    <div class="stat-tile">
      <div class="stat-tile__num primary">{{ summary.draft }}</div>
      <div class="stat-tile__lbl">Draft</div>
    </div>
    <div class="stat-tile">
      <div class="stat-tile__num primary" style="color: #0c447c">
        {{ summary.awaiting_signature }}
      </div>
      <div class="stat-tile__lbl">Awaiting Signature</div>
    </div>
    <div class="stat-tile">
      <div class="stat-tile__num primary" style="color: #27500a">{{ summary.signed }}</div>
      <div class="stat-tile__lbl">Signed</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  summary: Object,
})
</script>
