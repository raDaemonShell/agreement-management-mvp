<template>
  <div class="page" id="page-wizard">
    <div class="wizard-container">
      <div class="d-flex align-center gap-2 pointer mb-4" @click="goToDashboard">
        <i class="ti ti-arrow-left" style="font-size: 15px; color: var(--neutral-6)"></i>
        <span style="font-size: 12px; color: var(--neutral-7)">Back to agreements</span>
      </div>
      <div class="vm-card wizard-wrap">
        <WizStepBar :currentStep="currentStep" />

        <component :is="currentComponent" />

        <WizFootBar :currentStep="currentStep" @next="nextStep" @previous="previousStep" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { API_URL } from '../services/api'
import { ref, computed, provide, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { createAgreement, updateAgreement } from '../services/agreementService' // ← add updateAgreement

import WizStepBar from '../components/wizard/WizStepBar.vue'
import WizStep1 from '../components/wizard/WizStep1.vue'
import WizStep2 from '../components/wizard/WizStep2.vue'
import WizStep3 from '../components/wizard/WizStep3.vue'
import WizStep4 from '../components/wizard/WizStep4.vue'
import WizStep5 from '../components/wizard/WizStep5.vue'
import WizStep6 from '../components/wizard/WizStep6.vue'
import WizStep7 from '../components/wizard/WizStep7.vue'
import WizFootBar from '../components/wizard/WizFootBar.vue'

const currentStep = ref(1)
const router = useRouter()
const dirCompanies = ref([])

const step1Error = ref(false)
const step2Error = ref(false)
const step3Error = ref(false)
const step6Error = ref(false)
const generating = ref(false)

provide('step1Error', step1Error)
provide('step2Error', step2Error)
provide('step3Error', step3Error)
provide('step6Error', step6Error)
provide('generating', generating)

async function loadPartners() {
  const response = await fetch(`${API_URL}/partners/`)
  dirCompanies.value = await response.json()
}

onMounted(() => {
  loadPartners()
})

provide('dirCompanies', dirCompanies)

function goToDashboard() {
  router.push({ name: 'dashboard' })
}

const agreement = ref({
  myCompany: 'Sony Inc.',
  myCompanyLocation: 'San Francisco, CA',
  myEmail: 'amatorioarjay@gmail.com',
  myPhone: '99999999',
  myTitle: 'CEO',
  // Step 1
  partner: null,
  contactName: '',
  contactTitle: '',
  contactEmail: '',
  contactPhone: '',
  initiatorName: 'Your Name',
  initiatorTitle: 'Your Title',
  initiatorSignedAt: null,
  // Step 2
  agreementType: '',
  agreementTypeTitle: '',
  agreementTypeDescription: '',
  // Step 3
  purpose: '',
  intellectualProperty: '',
  startDate: '',
  endDate: '',
  governingLaw: '',
  //step4
  sections: {
    sec1: '',
    sec2: '',
    sec3: '',
    sec4: '',
    sec5: '',
    sec6: '',
  },
  // Step 6
  linkExpirationDays: 7,

  status: 'DRAFT',
  // Set after save
  id: null,
  shareableLink: '',
})

provide('agreement', agreement)

function ensureInitiatorSignedAt() {
  if (!agreement.value.initiatorSignedAt) {
    agreement.value.initiatorSignedAt = new Date().toISOString()
  }
}

function validateStep1() {
  const a = agreement.value
  return (
    a.partner !== null &&
    a.contactName.trim() !== '' &&
    a.contactTitle.trim() !== '' &&
    a.contactEmail.trim() !== '' &&
    a.initiatorName.trim() !== '' &&
    a.initiatorTitle.trim() !== ''
  )
}
function validateStep2() {
  return agreement.value.agreementType !== ''
}
function validateStep3() {
  const a = agreement.value
  return (
    a.purpose !== '' &&
    a.intellectualProperty !== '' &&
    a.startDate !== '' &&
    a.endDate !== '' &&
    a.governingLaw !== '' &&
    new Date(a.endDate) > new Date(a.startDate)
  )
}
function validateStep6() {
  return agreement.value.linkExpirationDays > 0
}

// sanitize — strips dangerous characters
function sanitize(val) {
  if (!val) return ''
  return val.trim().replace(/[<>]/g, '')
}

// sanitize all text inputs before saving
function sanitizeAgreement() {
  const a = agreement.value
  a.contactName = sanitize(a.contactName)
  a.contactTitle = sanitize(a.contactTitle)
  a.contactEmail = sanitize(a.contactEmail)
  a.contactPhone = sanitize(a.contactPhone)
  a.initiatorName = sanitize(a.initiatorName)
  a.initiatorTitle = sanitize(a.initiatorTitle)
}

async function generateAgreement() {
  try {
    const payload = {
      title: `${agreement.value.agreementTypeTitle} - ${agreement.value.myCompany}`,
      partner_id: agreement.value.partner?.id,
      contact_name: agreement.value.contactName,
      contact_title: agreement.value.contactTitle,
      contact_email: agreement.value.contactEmail,
      contact_phone: agreement.value.contactPhone,
      initiator_name: agreement.value.initiatorName,
      initiator_title: agreement.value.initiatorTitle,
      initiator_company: agreement.value.myCompany,
      initiator_location: agreement.value.myCompanyLocation,
      initiator_email: agreement.value.myEmail,
      initiator_phone: agreement.value.myPhone,
      agreement_type: agreement.value.agreementType,
      purpose: agreement.value.purpose,
      intellectual_property: agreement.value.intellectualProperty,
      start_date: agreement.value.startDate,
      end_date: agreement.value.endDate,
      governing_law: agreement.value.governingLaw,
      link_expiration_days: agreement.value.linkExpirationDays,
      status: agreement.value.status,
    }
    const response = await createAgreement(payload)
    agreement.value.id = response.id
    currentStep.value++
  } catch (error) {
    console.error('Failed to generate:', error)
  } finally {
    generating.value = false
  }
}

async function sendForSignature() {
  generating.value = true

  try {
    ensureInitiatorSignedAt()

    await updateAgreement(agreement.value.id, {
      status: 'SENT',
      link_expiration_days: agreement.value.linkExpirationDays,
      initiator_signed_at: agreement.value.initiatorSignedAt,
    })

    agreement.value.status = 'SENT'
    currentStep.value++
  } catch (err) {
    console.error('Failed to send:', err)
  } finally {
    generating.value = false
  }
}

async function nextStep() {
  if (currentStep.value === 1) {
    if (!validateStep1()) {
      step1Error.value = true
      return
    }
    step1Error.value = false
    sanitizeAgreement()
  }

  if (currentStep.value === 2) {
    if (!validateStep2()) {
      step2Error.value = true
      return
    }
    step2Error.value = false
  }

  if (currentStep.value === 3) {
    if (!validateStep3()) {
      step3Error.value = true
      return
    }
    step3Error.value = false
    generating.value = true
    await generateAgreement()
    return
  }

  if (currentStep.value === 4) {
    await saveSectionsAndGeneratePdf()
    return
  }

  if (currentStep.value === 6) {
    if (!validateStep6()) {
      step6Error.value = true
      return
    }
    step6Error.value = false
    await sendForSignature()
    return
  }

  if (currentStep.value === 7) {
    router.push({ name: 'agreement-new' })
    return
  }

  if (currentStep.value < 7) {
    currentStep.value++
  }
}

async function saveSectionsAndGeneratePdf() {
  generating.value = true

  try {
    ensureInitiatorSignedAt()

    const sections = agreement.value.sections

    await updateAgreement(agreement.value.id, {
      section_1: sections.sec1,
      section_2: sections.sec2,
      section_3: sections.sec3,
      section_4: sections.sec4,
      section_5: sections.sec5,
      section_6: sections.sec6,
      initiator_signed_at: agreement.value.initiatorSignedAt,
    })

    currentStep.value++
  } catch (err) {
    console.error('Failed to save sections:', err)
  } finally {
    generating.value = false
  }
}

function previousStep() {
  if (currentStep.value > 1) {
    currentStep.value--
  }
}

const steps = {
  1: WizStep1,
  2: WizStep2,
  3: WizStep3,
  4: WizStep4,
  5: WizStep5,
  6: WizStep6,
  7: WizStep7,
}

const currentComponent = computed(() => steps[currentStep.value])
</script>
