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
        <button class="vm-btn vm-btn--sm"><i class="ti ti-download"></i> Download draft</button>
      </div>
      <div class="pdf-doc">
        <div class="pdf-title">NON-DISCLOSURE AGREEMENT</div>
        <div class="pdf-subtitle">
          Generated via Varmodel · Draft ·

          {{ agreement.startDate }}

          -

          {{ agreement.endDate }}

          · Governed by

          {{ agreement.governingLaw }}

          law
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
          <div class="pdf-sec__body">
            This

            {{ agreement.agreementTypeTitle }}

            is entered into between {{ agreement.myCompany }} and

            {{ agreement.partner?.name }}

            represented by

            {{ agreement.initiatorName }}

            and

            {{ agreement.contactName }}.
          </div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">2. Confidential Information</div>
          <div class="pdf-sec__body">
            “Confidential Information” means any non-public information disclosed by either Party,
            including trade secrets, business plans, financial data, and technical information in
            any form…
          </div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">3. Obligations</div>
          <div class="pdf-sec__body">
            Each Party agrees to hold the other’s Confidential Information in strict confidence, use
            it solely for the {{ agreement.purpose }}, and not disclose to any third party without
            prior written consent…
          </div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">4. Term</div>
          <div class="pdf-sec__body">
            This Agreement shall remain in effect from {{ agreement.startDate }}

            to

            {{ agreement.endDate }}

            governed by

            {{ agreement.governingLaw }}

            law.
          </div>
        </div>
        <div class="pdf-sec">
          <div class="pdf-sec__title">5. Remedies</div>
          <div class="pdf-sec__body">
            Each Party acknowledges that breach may cause irreparable harm, entitling the
            non-breaching Party to seek equitable relief in addition to legal remedies…
          </div>
        </div>
        <div class="pdf-ai-block">
          <div class="pdf-ai-block__label">
            <i class="ti ti-sparkles"></i> Section 6 — Special provisions (AI-assisted)
          </div>
          <div class="pdf-ai-block__body">
            {{ agreement.partner?.name }}

            will protect

            {{ agreement.intellectualProperty }}

            throughout the duration of this agreement for

            {{ agreement.purpose }}

            under

            {{ agreement.governingLaw }}

            law.
          </div>
        </div>
        <div class="pdf-sig-row">
          <div class="pdf-sig-box">
            <div class="pdf-sig-box__label">Signature — {{ agreement.myCompany }}</div>
            <div class="pdf-sig-box__name">{{ agreement.initiatorName }}</div>
            <div class="pdf-sig-box__meta">
              {{ agreement.initiatorTitle }} · Jun 1, 2026 · 10:42 AM PST
            </div>
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
import { inject, computed } from 'vue'

const agreement = inject('agreement')

const fileName = computed(() => {
  if (!agreement.value.agreementTypeTitle || !agreement.value.partner) {
    return 'agreement.pdf'
  }

  return `${agreement.value.agreementTypeTitle} - ${agreement.value.partner.name}.pdf`
})
</script>
