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
          <div class="sign-slot__status">
            <i class="ti ti-check"></i> Signed · {{ initiatorSignedLabel }}
          </div>
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
        :class="{ 'is-active': !customMode && agreement.linkExpirationDays === option.days }"
        @click="selectExpiry(option.days)"
      >
        {{ option.label }}
      </div>
      <div class="expiry-chip" :class="{ 'is-active': customMode }" @click="customMode = true">
        Custom
      </div>
    </div>

    <!-- custom days input -->
    <div v-if="customMode" style="margin-top: 8px; display: flex; align-items: center; gap: 8px">
      <input
        class="vm-input"
        type="number"
        min="1"
        max="365"
        v-model.number="customDays"
        style="width: 80px"
        placeholder="Days"
        @input="agreement.linkExpirationDays = customDays"
      />
      <span style="font-size: 12px; color: var(--neutral-7)">days</span>
      <button class="vm-btn vm-btn--sm" @click="customMode = false">Cancel</button>
    </div>
    <div
      v-if="step6Error"
      class="vm-notice vm-notice--warning"
      style="margin-top: 8px; border-radius: var(--radius-md)"
    >
      <i class="ti ti-alert-circle" style="font-size: 14px; flex-shrink: 0"></i>
      <div>Please set a valid link expiration before sending.</div>
    </div>

    <div class="vm-notice vm-notice--info" style="margin-top: 16px">
      <i class="ti ti-mail"></i> Recipient ({{ agreement.contactName }}) can forward this link to
      legal counsel for review before signing.
    </div>
  </div>
</template>

<script setup>
import { inject, ref, computed, onMounted } from 'vue'
import { formatSignedDate } from '../../utils/formatters'

const agreement = inject('agreement')
const step6Error = inject('step6Error', ref(false))
const copied = ref(false)
const customMode = ref(false)
const customDays = ref(30)

const expiryOptions = [
  { days: 3, label: '3 days' },
  { days: 7, label: '7 days' },
  { days: 14, label: '14 days' },
]

function selectExpiry(days) {
  customMode.value = false
  agreement.value.linkExpirationDays = days
}

function ensureInitiatorSignedAt() {
  if (!agreement.value.initiatorSignedAt) {
    agreement.value.initiatorSignedAt = new Date().toISOString()
  }
}

// Generate shareable link when step 6 mounts
onMounted(() => {
  ensureInitiatorSignedAt()

  if (agreement.value.id && !agreement.value.shareableLink) {
    agreement.value.shareableLink = `${window.location.origin}/sign/${agreement.value.id}`
  }
})

const initiatorSignedLabel = computed(() =>
  formatSignedDate(agreement.value.initiatorSignedAt || new Date()),
)

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
