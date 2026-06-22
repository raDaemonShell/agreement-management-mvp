<template>
  <div class="vm-tabs">
    <div
      class="vm-tab"
      :class="{
        'is-active': activeTab === 'ALL',
      }"
      @click="selectTab('ALL')"
    >
      All ({{ totalCount }})
    </div>

    <div
      class="vm-tab"
      :class="{
        'is-active': activeTab === 'DRAFT',
      }"
      @click="selectTab('DRAFT')"
    >
      Drafts ({{ summary.draft }})
    </div>

    <div
      class="vm-tab"
      :class="{
        'is-active': activeTab === 'SENT',
      }"
      @click="selectTab('SENT')"
    >
      Shared ({{ summary.awaiting_signature }})
    </div>

    <div
      class="vm-tab"
      :class="{
        'is-active': activeTab === 'SIGNED',
      }"
      @click="selectTab('SIGNED')"
    >
      Signed ({{ summary.signed }})
    </div>
  </div>
</template>

<script setup>
defineProps({
  activeTab: String,
  summary: Object,
  totalCount: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits(['change-tab'])

function selectTab(tab) {
  emit(
    'change-tab',

    tab,
  )
}
</script>
