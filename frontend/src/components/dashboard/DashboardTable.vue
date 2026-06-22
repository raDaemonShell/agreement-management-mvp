<template>
  <div class="vm-table">
    <div class="vm-table__head">
      <div class="vm-table__th">Agreement</div>
      <div class="vm-table__th">To</div>
      <div class="vm-table__th">Type</div>
      <div class="vm-table__th">Due date</div>
      <div class="vm-table__th">Status</div>
      <div class="vm-table__th"></div>
    </div>

    <div>
      <div v-for="agreement in agreements" :key="agreement.id" class="vm-table__row">
        <div>
          <div class="vm-table__name">
            {{ agreement.title }}
          </div>

          <div class="vm-table__sub">
            {{ agreementTypeTitle(agreement.agreement_type) }}
          </div>
        </div>

        <div class="vm-table__cell">
          {{ agreement.partner?.name }}
        </div>

        <div class="vm-table__cell">
          {{ agreement.agreement_type }}
        </div>

        <div class="vm-table__cell">
          {{ formatDate(agreement.end_date) }}
        </div>

        <div>
          <span class="vm-pill" :class="statusClass(agreement.status)">
            {{ statusText(agreement.status) }}
          </span>
        </div>

        <div>
          <button v-if="agreement.status === 'SIGNED'" class="vm-btn vm-btn--sm vm-btn--dl">
            <i class="ti ti-download"></i>

            PDF
          </button>

          <span v-else style="color: #bbb"> — </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
console.log('test')

defineProps({
  agreements: Array,
})

function agreementTypeTitle(type) {
  const map = {
    NDA: 'Non-Disclosure Agreement',

    MSA: 'Master Services Agreement',

    TEAMING: 'Teaming Agreement',

    SUBCONTRACTOR: 'Subcontractor Agreement',

    LOI: 'Letter of Intent',
  }

  return map[type] || type
}

function formatDate(dateString) {
  if (!dateString) return '-'

  return new Date(dateString).toLocaleDateString(
    'en-US',

    {
      month: 'short',

      day: 'numeric',

      year: 'numeric',
    },
  )
}

function statusClass(status) {
  switch (status) {
    case 'DRAFT':
      return 'vm-pill--draft'

    case 'SENT':
      return 'vm-pill--sent'

    case 'SIGNED':
      return 'vm-pill--signed'

    default:
      return ''
  }
}

function statusText(status) {
  switch (status) {
    case 'DRAFT':
      return 'Draft'

    case 'SENT':
      return 'Awaiting signature'

    case 'SIGNED':
      return 'Signed'

    default:
      return status
  }
}
</script>
