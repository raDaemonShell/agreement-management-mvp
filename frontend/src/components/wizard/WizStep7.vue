<template>
  <div class="wizard-screen" id="ws7">
    <div class="done-screen">
      <div class="done-screen__circle">
        <i class="ti ti-check" style="font-size: 22px; color: #27500a"></i>
      </div>
      <div class="done-screen__title">Agreement sent for signature</div>
      <div class="done-screen__sub">Agreement link sent to {{ agreement.contactEmail }}</div>

      <div class="done-parties">
        <div class="done-party">
          <div class="done-party__name">{{ agreement.initiatorName }}</div>
          <div class="done-party__co">{{ agreement.myCompany }}</div>
          <div class="done-party__status">
            <i class="ti ti-check"></i> Signed · {{ initiatorSignedLabel }}
          </div>
        </div>
        <div class="done-party">
          <div class="done-party__name">{{ agreement.contactName }}</div>
          <div class="done-party__co">{{ agreement.partner?.name }}</div>
          <div class="done-party__status">
            <i class="ti ti-clock" style="font-size: 11px"></i> Awaiting signature
          </div>
        </div>
      </div>

      <div class="d-flex justify-center gap-3">
        <button class="vm-btn" @click="downloadPdf" :disabled="downloading">
          <i class="ti ti-download"></i>
          {{ downloading ? 'Preparing...' : 'Download PDF' }}
        </button>
        <button class="vm-btn" @click="goToDashboard">
          <i class="ti ti-folder"></i> View agreements
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { inject, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { formatSignedDate } from '../../utils/formatters'

const agreement = inject('agreement')
const router = useRouter()
const downloading = ref(false)

const API_URL = 'http://127.0.0.1:8000/api'

const initiatorSignedLabel = computed(() =>
  formatSignedDate(agreement.value.initiatorSignedAt || new Date()),
)

function goToDashboard() {
  router.push({ name: 'dashboard' })
}

async function downloadPdf() {
  downloading.value = true
  try {
    const res = await fetch(`${API_URL}/agreements/${agreement.value.id}/download_pdf/`)
    const data = await res.json()
    window.open(data.url, '_blank')
  } catch (err) {
    console.error('Download error:', err)
  } finally {
    downloading.value = false
  }
}
</script>
