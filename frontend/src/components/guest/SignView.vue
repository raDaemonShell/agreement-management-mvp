<template>
  <div class="screen-strip">Screen 4 — Signature capture</div>
  <div class="page-wrap" v-if="agreement">
    <div class="vm-card">
      <div class="vm-card__header">
        <div>
          <div class="vm-card__title">Sign the agreement</div>
          <div style="font-size: 11px; color: var(--neutral-6); margin-top: 2px">
            By signing, you confirm you have read and agree to all terms.
          </div>
        </div>
        <span class="vm-pill vm-pill--info" style="font-size: 10px">
          {{ agreement.agreement_type }} &middot; {{ agreement.initiator_company }} &times;
          {{ agreement.partner?.name }}
        </span>
      </div>

      <div class="p-5">
        <span class="sidebar-label">Signature status</span>
        <div class="sign-parties mt-2">
          <div class="sign-slot">
            <div class="sign-slot__label">{{ agreement.initiator_company }}</div>
            <div class="sig-display">{{ agreement.initiator_name }}</div>
            <div class="sig-check">
              <i class="ti ti-check" style="font-size: 11px"></i> Signed {{ sentDate }}
            </div>
          </div>
          <div class="sign-slot sign-slot--active">
            <div class="sign-slot__label sign-slot__label--active">
              {{ agreement.partner?.name }} &mdash; your signature
            </div>
            <input class="sig-input" placeholder="Type your full legal name" v-model="signature" />
            <div class="sig-hint">Your typed name constitutes a legal signature</div>
          </div>
        </div>

        <span class="sidebar-label">Captured at signing</span>
        <div class="capture-grid mt-2">
          <div class="capture-item">
            <div class="capture-item__label">Full name</div>
            <div class="capture-item__value">{{ agreement.contact_name }}</div>
          </div>
          <div class="capture-item">
            <div class="capture-item__label">Email</div>
            <div class="capture-item__value">{{ agreement.contact_email }}</div>
          </div>
          <div class="capture-item">
            <div class="capture-item__label">IP address</div>
            <div class="capture-item__value">{{ ipAddress }}</div>
          </div>
          <div class="capture-item">
            <div class="capture-item__label">Timestamp</div>
            <div class="capture-item__value">{{ timestamp }}</div>
          </div>
          <div class="capture-item">
            <div class="capture-item__label">Device</div>
            <div class="capture-item__value">{{ device }}</div>
          </div>
          <div class="capture-item">
            <div class="capture-item__label">Identity</div>
            <div class="capture-item__value capture-item__value--ok">
              <i class="ti ti-circle-check" style="font-size: 12px"></i> Email verified
            </div>
          </div>
        </div>

        <div class="legal-confirm" @click="confirmed = !confirmed">
          <div class="checkbox" :class="{ 'is-checked': confirmed }">
            <i v-if="confirmed" class="ti ti-check" style="font-size: 10px; color: white"></i>
          </div>
          <div style="font-size: 12px; color: var(--neutral-7); line-height: 1.6">
            I confirm I have read the full agreement, I agree to all terms, and I understand that my
            typed name constitutes a legally binding signature.
          </div>
        </div>

        <button
          class="vm-btn vm-btn--primary vm-btn--lg vm-btn--block mb-2"
          @click="handleSign"
          :disabled="!canSign"
          :style="{ opacity: canSign ? 1 : 0.5 }"
        >
          <i class="ti ti-writing" style="font-size: 16px"></i> Sign &amp; execute agreement
        </button>
        <div style="font-size: 10px; color: var(--neutral-5); text-align: center; line-height: 1.5">
          Varmodel is not a law firm. This is not legal advice. Audit data is shared with both
          parties upon execution.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps({
  agreement: Object,
})

const emit = defineEmits(['next'])

const signature = ref('')
const confirmed = ref(false)
const ipAddress = ref('Fetching...')
const device = ref('')
const timestamp = ref('')

const canSign = computed(() => signature.value.trim().length > 0 && confirmed.value)

const fmt = (dateStr) =>
  new Date(dateStr).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })

const sentDate = computed(() => fmt(props.agreement.created_at))

onMounted(async () => {
  // timestamp
  timestamp.value = new Date().toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
    timeZoneName: 'short',
  })

  // device
  const ua = navigator.userAgent
  const browser = ua.includes('Chrome')
    ? 'Chrome'
    : ua.includes('Firefox')
      ? 'Firefox'
      : ua.includes('Safari')
        ? 'Safari'
        : 'Browser'
  const os = ua.includes('Mac')
    ? 'macOS'
    : ua.includes('Win')
      ? 'Windows'
      : ua.includes('Linux')
        ? 'Linux'
        : 'Unknown OS'
  device.value = `${browser} · ${os}`

  // IP address
  try {
    const res = await fetch('https://api.ipify.org?format=json')
    const data = await res.json()
    ipAddress.value = data.ip
  } catch {
    ipAddress.value = 'Unavailable'
  }
})

async function handleSign() {
  if (!canSign.value) return

  try {
    const response = await fetch(`http://127.0.0.1:8000/api/agreements/${props.agreement.id}/`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: 'SIGNED' }),
    })

    if (!response.ok) throw new Error('Failed to sign')

    emit('next')
  } catch (err) {
    console.error('Signing error:', err)
  }
}
</script>
