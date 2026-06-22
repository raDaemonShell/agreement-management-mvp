<template>
  <div class="wizard-screen" id="ws2">
    <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
      Select agreement type
    </div>
    <div class="neutral-7 mb-4" style="font-size: 12px">
      Choose the type of contract you need to create
    </div>
    <div
      v-for="type in agreementTypes"
      :key="type.value"
      class="radio-pill"
      :class="{
        'is-selected': agreement.agreementType === type.value,
      }"
      @click="selectAgreement(type)"
    >
      <div
        class="radio-dot"
        :class="{
          'is-on': agreement.agreementType === type.value,
        }"
      ></div>

      <div>
        <div class="radio-pill__title">
          {{ type.title }}
        </div>

        <div class="radio-pill__desc">
          {{ type.description }}
        </div>
      </div>
    </div>
    <div class="or-divider">or</div>
    <div class="upload-box">
      <i class="ti ti-upload"></i>
      <div style="font-size: 13px; color: var(--neutral-7)">Upload your own contract</div>
      <div style="font-size: 11px; color: var(--neutral-6); margin-top: 3px">
        PDF or DOCX, max 10MB
      </div>
    </div>
  </div>
</template>

<script setup>
import { inject } from 'vue'

const agreement = inject('agreement')

const agreementTypes = [
  {
    value: 'NDA',

    title: 'Non-Disclosure Agreement (NDA)',

    description: 'Protect confidential information shared between parties',
  },

  {
    value: 'MSA',

    title: 'Master Services Agreement (MSA)',

    description: 'Define terms for ongoing services between businesses',
  },

  {
    value: 'TEAMING',

    title: 'Teaming Agreement',

    description: 'Formalize a collaboration for a specific project or bid',
  },

  {
    value: 'SUBCONTRACTOR',

    title: 'Subcontractor Agreement',

    description: 'Engage a subcontractor with defined scope and obligations',
  },

  {
    value: 'LOI',

    title: 'Letter of Intent (LOI)',

    description: 'Express intent to enter a formal agreement',
  },
]

function selectAgreement(type) {
  agreement.value.agreementType = type.value

  agreement.value.agreementTypeTitle = type.title

  agreement.value.agreementTypeDescription = type.description
}
</script>
