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

async function loadPartners() {
  const response = await fetch('http://127.0.0.1:8000/api/partners/')
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
  myCompany: 'TechVentures Inc',
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
    agreement.value.shareableLink = `${window.location.origin}/sign/${response.id}`

    currentStep.value++
  } catch (error) {
    console.error('Failed to generate:', error)
  }
}

async function sendForSignature() {
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
  }
}

async function nextStep() {
  if (currentStep.value === 3) {
    await generateAgreement()
    return
  }

  if (currentStep.value === 4) {
    await saveSectionsAndGeneratePdf()
    return
  }

  if (currentStep.value === 6) {
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
