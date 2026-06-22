<template>
  <div class="wizard-screen" id="ws6">
    <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">Sign &amp; send</div>
    <div class="neutral-7 mb-4" style="font-size: 12px">
      Sign below, set an expiry, and send the agreement link to {{ agreement.partner?.name }}
    </div>

    <div class="sign-grid">
      <div>
        <div class="sign-slot__label">Your signature — {{ agreement.initiatorName }}</div>
        <div class="sign-slot is-signed">
          <div class="sign-slot__name">{{ agreement.initiatorName }}</div>
          <div class="sign-slot__status"><i class="ti ti-check"></i> Signed · Jun 1, 2026</div>
        </div>
      </div>
      <div>
        <div class="sign-slot__label">Counterparty — {{ agreement.contactName }}</div>
        <div class="sign-slot">
          <i class="ti ti-clock" style="font-size: 20px; color: var(--neutral-5)"></i>
          <div class="sign-slot__pending">Awaiting {{ agreement.partner?.name }}</div>
        </div>
      </div>
    </div>

    <div class="vm-label">Recipient email</div>
    <div class="static-field">{{ agreement.contactEmail }}</div>

    <div class="vm-label">Shareable link</div>
    <div class="link-row">
      <div class="link-field">{{ agreement.shareableLink }}</div>
      <button class="vm-btn vm-btn--sm" @click="copyLink">
        <i class="ti ti-copy"></i> {{ copied ? 'Copied!' : 'Copy' }}
      </button>
    </div>

    <div class="vm-label">Link expires in</div>
    <div class="expiry-chips">
      <div
        v-for="option in expiryOptions"
        :key="option.days"
        class="expiry-chip"
        :class="{ 'is-active': agreement.linkExpirationDays === option.days }"
        @click="agreement.linkExpirationDays = option.days"
      >
        {{ option.label }}
      </div>
    </div>

    <div class="vm-notice vm-notice--info">
      <i class="ti ti-mail"></i> Recipient ({{ agreement.contactName }}) can forward this link to
      legal counsel for review before signing.
    </div>
  </div>
</template>

<script setup>
import { inject, ref } from 'vue'

const agreement = inject('agreement')
const copied = ref(false)

const expiryOptions = [
  { days: 3, label: '3 days' },
  { days: 7, label: '7 days' },
  { days: 14, label: '14 days' },
]

// ← remove selectExpiry, chip just updates local state
async function copyLink() {
  try {
    await navigator.clipboard.writeText(agreement.value.shareableLink)
    copied.value = true
    setTimeout(() => (copied.value = false), 2000)
  } catch {
    copied.value = false
  }
}
</script>
