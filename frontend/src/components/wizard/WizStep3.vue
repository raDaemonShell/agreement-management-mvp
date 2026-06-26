<template>
  <div class="wizard-screen" id="ws3">
    <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
      Tell us about this agreement
    </div>
    <div class="neutral-7 mb-4" style="font-size: 12px">
      Your answers shape the custom clause in Section 6
    </div>
    <div class="q-label">Primary purpose of this agreement?</div>
    <div class="q-pills">
      <div
        v-for="purpose in purposes"
        :key="purpose"
        class="q-pill"
        :class="{
          'is-active': agreement.purpose === purpose,
        }"
        @click="selectPurpose(purpose)"
      >
        {{ purpose }}
      </div>
    </div>
    <div class="q-label">Do you have intellectual property to protect?</div>
    <div class="q-pills">
      <div
        v-for="ip in ipOptions"
        :key="ip"
        class="q-pill"
        :class="{
          'is-active': agreement.intellectualProperty === ip,
        }"
        @click="selectIp(ip)"
      >
        {{ ip }}
      </div>
    </div>
    <div class="q-label">Agreement duration</div>
    <div class="date-row">
      <div class="date-box">
        <div class="date-box__label"><i class="ti ti-calendar"></i> Start date</div>
        <input type="date" class="vm-input--date" v-model="agreement.startDate" />
      </div>
      <div class="date-box">
        <div class="date-box__label"><i class="ti ti-calendar-off"></i> End date</div>
        <input type="date" class="vm-input--date" v-model="agreement.endDate" />
      </div>
    </div>
    <div class="dur-display">
      {{ durationText }}
    </div>
    <div class="q-label">Governing state law?</div>
    <div class="q-pills">
      <div
        v-for="law in laws"
        :key="law"
        class="q-pill"
        :class="{
          'is-active': law === 'Other' ? showOther : agreement.governingLaw === law,
        }"
        @click="selectLaw(law)"
      >
        {{ law }}
      </div>
    </div>

    <!-- custom other input -->
    <div v-if="showOther" style="margin-top: 8px; display: flex; align-items: center; gap: 8px">
      <input
        class="vm-input"
        v-model="otherLaw"
        placeholder="Enter state name e.g. Florida"
        @input="agreement.governingLaw = otherLaw"
        style="flex: 1"
      />
      <button class="vm-btn vm-btn--sm" @click="cancelOther">Cancel</button>
    </div>
    <div
      v-if="step3Error"
      class="vm-notice vm-notice--warning"
      style="margin-top: 16px; border-radius: var(--radius-md)"
    >
      <i class="ti ti-alert-circle" style="font-size: 14px; flex-shrink: 0"></i>
      <div>
        Please complete all fields before continuing:
        <ul style="margin-top: 4px; padding-left: 16px; font-size: 11px">
          <li v-if="!agreement.purpose">Select a primary purpose</li>
          <li v-if="!agreement.intellectualProperty">Select intellectual property option</li>
          <li v-if="!agreement.startDate">Select a start date</li>
          <li v-if="!agreement.endDate">Select an end date</li>
          <li
            v-if="
              agreement.startDate &&
              agreement.endDate &&
              new Date(agreement.endDate) <= new Date(agreement.startDate)
            "
          >
            End date must be after start date
          </li>
          <li v-if="!agreement.governingLaw">Select governing law</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, inject, ref } from 'vue'
const agreement = inject('agreement')
const purposes = ['Joint project bid', 'Ongoing services', 'Information sharing', 'Product resale']
const ipOptions = ['Yes — trade secrets', 'Yes — patents', 'Yes — methods', 'No']
const laws = ['California', 'New York', 'Texas', 'Other']
const showOther = ref(false)
const otherLaw = ref('')
const step3Error = inject('step3Error', ref(false))
const durationText = computed(() => {
  if (!agreement.value.startDate || !agreement.value.endDate) {
    return ''
  }

  const start = new Date(agreement.value.startDate)

  const end = new Date(agreement.value.endDate)

  const days = Math.ceil((end - start) / (1000 * 60 * 60 * 24))

  if (days <= 0) {
    return 'Invalid date range'
  }

  const years = Math.floor(days / 365)

  if (years >= 1) {
    return `Duration: ${years} year${years > 1 ? 's' : ''}`
  }

  return `Duration: ${days} days`
})

function selectLaw(law) {
  step3Error.value = false
  if (law === 'Other') {
    showOther.value = true
    agreement.value.governingLaw = ''
  } else {
    showOther.value = false
    otherLaw.value = ''
    agreement.value.governingLaw = law
  }
}

function cancelOther() {
  showOther.value = false
  otherLaw.value = ''
  agreement.value.governingLaw = ''
}

function selectPurpose(purpose) {
  agreement.value.purpose = purpose
  step3Error.value = false
}

function selectIp(ip) {
  agreement.value.intellectualProperty = ip
  step3Error.value = false
}
</script>
