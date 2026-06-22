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
        @click="agreement.purpose = purpose"
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
        @click="agreement.intellectualProperty = ip"
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
          'is-active': agreement.governingLaw === law,
        }"
        @click="agreement.governingLaw = law"
      >
        {{ law }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, inject } from 'vue'

const agreement = inject('agreement')

const purposes = ['Joint project bid', 'Ongoing services', 'Information sharing', 'Product resale']

const ipOptions = ['Yes — trade secrets', 'Yes — patents', 'Yes — methods', 'No']

const laws = ['California', 'New York', 'Texas', 'Other']

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
</script>
