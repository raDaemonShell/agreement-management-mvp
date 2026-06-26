<template>
  <div class="screen-strip">Screen 5 — Execution confirmed</div>
  <div class="page-wrap" v-if="agreement">
    <div class="vm-card">
      <div class="executed-header">
        <div class="success-circle">
          <i class="ti ti-check" style="font-size: 22px; color: #27500a"></i>
        </div>
        <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
          Agreement executed
        </div>
        <div style="font-size: 12px; color: var(--neutral-7); line-height: 1.6">
          Both parties have signed. Copies sent to
          <strong>{{ agreement.initiator_email || agreement.initiator_name }}</strong> and
          <strong>{{ agreement.contact_email }}</strong>
        </div>
      </div>

      <div class="exe-parties">
        <div class="exe-party">
          <div class="exe-party__name">{{ agreement.initiator_name }}</div>
          <div class="exe-party__co">{{ agreement.initiator_company }}</div>
          <div class="exe-party__sig">
            <i class="ti ti-check" style="font-size: 10px"></i> Signed {{ sentDate }}
          </div>
        </div>
        <div class="exe-party">
          <div class="exe-party__name">{{ agreement.contact_name }}</div>
          <div class="exe-party__co">{{ agreement.partner?.name }}</div>
          <div class="exe-party__sig">
            <i class="ti ti-check" style="font-size: 10px"></i> Signed {{ todayDate }}
          </div>
        </div>
      </div>

      <div class="audit-block">
        <div class="audit-title">
          <i class="ti ti-shield-check" style="font-size: 15px; color: #27500a"></i>
          Signing audit record &mdash; {{ agreement.partner?.name }}
        </div>
        <div class="audit-row">
          <span class="audit-key">Signatory</span>
          <span class="audit-val"
            >{{ agreement.contact_name }} &middot; {{ agreement.contact_title }}</span
          >
        </div>
        <div class="audit-row">
          <span class="audit-key">Email</span>
          <span class="audit-val">{{ agreement.contact_email }}</span>
        </div>
        <div class="audit-row">
          <span class="audit-key">Email verified</span>
          <span class="audit-val audit-val--ok">Yes &middot; OTP confirmed</span>
        </div>
        <div class="audit-row">
          <span class="audit-key">IP address</span>
          <span class="audit-val">{{ ipAddress }}</span>
        </div>
        <div class="audit-row">
          <span class="audit-key">Timestamp</span>
          <span class="audit-val">{{ timestamp }}</span>
        </div>
        <div class="audit-row">
          <span class="audit-key">Device</span>
          <span class="audit-val">{{ device }}</span>
        </div>
        <div class="audit-row">
          <span class="audit-key">Agreement ID</span>
          <span class="audit-val audit-val--mono">{{ agreement.id }}</span>
        </div>
      </div>

      <div class="executed-actions">
        <button
          class="vm-btn flex-grow-1"
          style="justify-content: center"
          @click="downloadPdf"
          :disabled="downloading"
        >
          <i class="ti ti-download"></i>
          {{ downloading ? 'Preparing...' : 'Download signed PDF' }}
        </button>
        <button
          class="vm-btn flex-grow-1"
          style="justify-content: center"
          @click="emailCopy"
          :disabled="emailing"
        >
          <i class="ti ti-mail"></i>
          {{ emailing ? 'Sending...' : 'Email me a copy' }}
        </button>
      </div>

      <!-- success message -->
      <div
        v-if="emailSent"
        style="text-align: center; font-size: 12px; color: #27500a; padding: 8px 16px"
      >
        <i class="ti ti-circle-check"></i> Email sent to {{ agreement.contact_email }}
      </div>

      <div class="account-nudge">
        <div>
          <div class="account-nudge__title">Manage your agreements on Varmodel</div>
          <div class="account-nudge__sub">
            Create a free account to store, track, and send your own agreements
          </div>
        </div>
        <button class="vm-btn vm-btn--primary" style="white-space: nowrap; font-size: 12px">
          Sign up free
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps({
  agreement: Object,
})

const API_URL = 'http://127.0.0.1:8000/api'

const ipAddress = ref('Fetching...')
const device = ref('')
const timestamp = ref('')
const downloading = ref(false)
const emailing = ref(false)
const emailSent = ref(false)

const fmt = (dateStr) =>
  new Date(dateStr).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })

const sentDate = computed(() => fmt(props.agreement.created_at))
const todayDate = computed(() => fmt(new Date()))

onMounted(async () => {
  timestamp.value = new Date().toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
    timeZoneName: 'short',
  })

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

  try {
    const res = await fetch('https://api.ipify.org?format=json')
    const data = await res.json()
    ipAddress.value = data.ip
  } catch {
    ipAddress.value = 'Unavailable'
  }
})

async function downloadPdf() {
  downloading.value = true
  try {
    const res = await fetch(`${API_URL}/agreements/${props.agreement.id}/download_pdf/`)
    const data = await res.json()
    window.open(data.url, '_blank')
  } catch (err) {
    console.error('Download error:', err)
  } finally {
    downloading.value = false
  }
}

async function emailCopy() {
  emailing.value = true
  emailSent.value = false
  try {
    const res = await fetch(`${API_URL}/agreements/${props.agreement.id}/email_copy/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: props.agreement.contact_email }),
    })
    if (!res.ok) throw new Error('Failed to send email')
    emailSent.value = true
  } catch (err) {
    console.error('Email copy error:', err)
  } finally {
    emailing.value = false
  }
}
</script>
