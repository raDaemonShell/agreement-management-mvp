<template>
  <div class="wizard-screen" id="ws5">
    <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
      Preview final document
    </div>
    <div class="neutral-7 mb-4" style="font-size: 12px">
      This is exactly how the PDF will look to both parties.
    </div>
    <div class="pdf-wrap">
      <div class="pdf-toolbar">
        <div class="pdf-toolbar__filename">
          <i class="ti ti-file-text" style="font-size: 16px; color: var(--neutral-6)"></i>
          {{ fileName }}<span class="pdf-toolbar__page">Page 1 of 2</span>
        </div>
        <button class="vm-btn vm-btn--sm" @click="downloadPdf" :disabled="downloading">
          <i class="ti ti-download"></i> {{ downloading ? 'Preparing...' : 'Download draft' }}
        </button>
      </div>
      <div class="pdf-doc">
        <div class="pdf-title">{{ pdfTitle }}</div>
        <div class="pdf-subtitle">
          Generated via Varmodel · Draft · {{ formattedStartDate }} - {{ formattedEndDate }} ·
          Governed by {{ agreement.governingLaw }} law
        </div>
        <div class="pdf-parties">
          <div class="pdf-party">
            <div class="pdf-party__badge">Disclosing Party</div>
            <div class="pdf-party__name">{{ agreement.myCompany }}</div>
            <div class="pdf-party__loc">{{ agreement.myCompanyLocation }}</div>
            <div class="pdf-party__contact">
              <div class="pdf-party__contact-badge">Signing contact</div>
              <div class="pdf-party__contact-name">{{ agreement.initiatorName }}</div>
              <div class="pdf-party__contact-title">{{ agreement.initiatorTitle }}</div>
            </div>
          </div>
          <div class="pdf-party">
            <div class="pdf-party__badge">Receiving Party</div>
            <div class="pdf-party__name">{{ agreement.partner?.name }}</div>
            <div class="pdf-party__loc">{{ agreement.partner?.loc }}</div>
            <div class="pdf-party__contact">
              <div class="pdf-party__contact-badge">Signing contact</div>
              <div class="pdf-party__contact-name">{{ agreement.contactName }}</div>
              <div class="pdf-party__contact-title">{{ agreement.contactTitle }}</div>
            </div>
          </div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">1. Parties</div>
          <div class="pdf-sec__body">{{ agreement.sections.sec1 }}</div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">2. Confidential Information</div>
          <div class="pdf-sec__body">{{ agreement.sections.sec2 }}</div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">3. Obligations</div>
          <div class="pdf-sec__body">{{ agreement.sections.sec3 }}</div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">4. Term</div>
          <div class="pdf-sec__body">{{ agreement.sections.sec4 }}</div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">5. Remedies</div>
          <div class="pdf-sec__body">{{ agreement.sections.sec5 }}</div>
        </div>
        <div class="pdf-ai-block">
          <div class="pdf-ai-block__label">
            <i class="ti ti-sparkles"></i> Section 6 — Special provisions (AI-assisted)
          </div>
          <div class="pdf-ai-block__body">{{ agreement.sections.sec6 }}</div>
        </div>
        <div class="pdf-sig-row">
          <div class="pdf-sig-box">
            <div class="pdf-sig-box__label">Signature — {{ agreement.myCompany }}</div>
            <div class="pdf-sig-box__name">{{ agreement.initiatorName }}</div>
            <div class="pdf-sig-box__meta">{{ initiatorSignedMeta }}</div>
          </div>
          <div class="pdf-sig-box">
            <div class="pdf-sig-box__label">Signature — {{ agreement.partner?.name }}</div>
            <div class="pdf-sig-box__blank"></div>
            <div class="pdf-sig-box__meta">
              {{ agreement.contactName }} · {{ agreement.contactTitle }} · Awaiting signature
            </div>
          </div>
        </div>
        <div class="pdf-disclaimer">
          <i class="ti ti-alert-triangle"></i> Generated as a starting point. Varmodel Inc is not a
          law firm and this is not legal advice. Consult an attorney prior to execution.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { inject, computed, ref, onMounted } from 'vue'
import { getAgreementPdfUrl } from '../../services/agreementService'
import { formatInitiatorSignedMeta, formatSignedDate } from '../../utils/formatters'

const agreement = inject('agreement')
const downloading = ref(false)

function ensureInitiatorSignedAt() {
  if (!agreement.value.initiatorSignedAt) {
    agreement.value.initiatorSignedAt = new Date().toISOString()
  }
}

onMounted(() => {
  ensureInitiatorSignedAt()
})

const initiatorSignedMeta = computed(() =>
  formatInitiatorSignedMeta(
    agreement.value.initiatorTitle,
    agreement.value.initiatorSignedAt,
  ),
)

const pdfTitle = computed(() => {
  const title = agreement.value.agreementTypeTitle || 'Non-Disclosure Agreement'
  return title.replace(/\s*\([^)]*\)/, '').trim().toUpperCase()
})

const formattedStartDate = computed(() =>
  agreement.value.startDate ? formatSignedDate(agreement.value.startDate) : '',
)

const formattedEndDate = computed(() =>
  agreement.value.endDate ? formatSignedDate(agreement.value.endDate) : '',
)

async function downloadPdf() {
  downloading.value = true
  try {
    const url = await getAgreementPdfUrl(agreement.value.id)
    window.open(url, '_blank')
  } catch (err) {
    console.error('Download error:', err)
  } finally {
    downloading.value = false
  }
}

const fileName = computed(() => {
  if (!agreement.value.agreementTypeTitle || !agreement.value.partner) return 'agreement.pdf'
  return `${agreement.value.agreementTypeTitle} - ${agreement.value.partner.name}.pdf`
})
</script>
