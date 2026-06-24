<template>
  <div class="screen-strip">Screen 1 — Email notification received</div>
  <div class="page-wrap">
    <div class="d-flex align-center gap-2 mb-3" style="font-size: 11px; color: var(--neutral-6)">
      <i class="ti ti-inbox" style="font-size: 14px"></i> Inbox &mdash;
      {{ agreement.contact_email }}
    </div>
    <div class="vm-card">
      <div class="email-header">
        <div class="email-sender-av">V</div>
        <div class="flex-grow-1">
          <div class="fw-500" style="font-size: 12px; color: var(--neutral-11)">
            Varmodel &middot; agreements@varmodel.com
          </div>
          <div style="font-size: 11px; color: var(--neutral-6)">
            To: {{ agreement.contact_email }} &middot; {{ sentDate }}
          </div>
        </div>
      </div>

      <div class="p-5">
        <div class="fw-700 mb-3" style="font-size: 16px; color: var(--neutral-12)">
          You've been invited to sign a {{ agreementTypeTitle }}
        </div>

        <div style="font-size: 13px; color: var(--neutral-7); line-height: 1.7" class="mb-4">
          <strong style="color: var(--neutral-11)">{{ agreement.initiator_name }}</strong> from
          {{ agreement.initiator_company }} has sent you a partnership agreement for your review and
          signature on the Varmodel platform.
        </div>

        <div class="vm-notice vm-notice--purple mb-4">
          <div>
            <div class="fw-500 mb-1" style="font-size: 12px; color: #5b21b6">
              {{ agreementTypeTitle }}
            </div>
            <div style="font-size: 12px; color: #3c3489">
              Between {{ agreement.initiator_name }} and {{ agreement.contact_name }}
            </div>
          </div>
        </div>

        <div class="email-meta-grid mb-4">
          <div class="email-meta-cell">
            <div class="email-meta-cell__label">Agreement type</div>
            <div class="email-meta-cell__value">{{ agreement.agreement_type }}</div>
          </div>
          <div class="email-meta-cell">
            <div class="email-meta-cell__label">Valid period</div>
            <div class="email-meta-cell__value">{{ startDate }} – {{ endDate }}</div>
          </div>
          <div class="email-meta-cell">
            <div class="email-meta-cell__label">Link expires</div>
            <div class="email-meta-cell__value" style="color: #854f0b">{{ expiryDate }}</div>
          </div>
        </div>

        <div style="font-size: 12px; color: var(--neutral-7); line-height: 1.7" class="mb-4">
          You can review the full agreement and forward this link to your legal counsel before
          signing. No Varmodel account is required to review or sign.
        </div>

        <button class="vm-btn vm-btn--primary vm-btn--lg vm-btn--block" @click="$emit('next')">
          <i class="ti ti-file-text" style="font-size: 16px"></i> Review &amp; sign agreement
        </button>

        <div class="expiry-strip">
          <i class="ti ti-clock" style="font-size: 13px"></i>
          Link expires {{ expiryDate }} &middot; {{ daysRemaining }} days remaining
        </div>

        <div style="font-size: 10px; color: var(--neutral-5); line-height: 1.5; margin-top: 14px">
          This agreement was generated via Varmodel. Varmodel is not a law firm and this is not
          legal advice. We recommend consulting an attorney before signing.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  agreement: Object,
})

defineEmits(['next'])

const agreementTypeMap = {
  NDA: 'Non-Disclosure Agreement',
  MSA: 'Master Services Agreement',
  TEAMING: 'Teaming Agreement',
  SUBCONTRACTOR: 'Subcontractor Agreement',
  LOI: 'Letter of Intent',
}

const agreementTypeTitle = computed(
  () => agreementTypeMap[props.agreement.agreement_type] || props.agreement.agreement_type,
)

const fmt = (dateStr) =>
  new Date(dateStr).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })

const sentDate = computed(() => fmt(props.agreement.created_at))
const startDate = computed(() => fmt(props.agreement.start_date))
const endDate = computed(() => fmt(props.agreement.end_date))

const expiryDate = computed(() => {
  const d = new Date(props.agreement.created_at)
  d.setDate(d.getDate() + props.agreement.link_expiration_days)
  return fmt(d)
})

const daysRemaining = computed(() => {
  const expiry = new Date(props.agreement.created_at)
  expiry.setDate(expiry.getDate() + props.agreement.link_expiration_days)
  const diff = Math.ceil((expiry - new Date()) / (1000 * 60 * 60 * 24))
  return Math.max(0, diff)
})
</script>
