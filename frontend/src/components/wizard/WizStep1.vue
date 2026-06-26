<template>
  <div class="wizard-screen" id="ws1">
    <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
      Select a partner
    </div>
    <div class="neutral-7 mb-4" style="font-size: 12px; line-height: 1.5">
      Choose a partner from your saved list, or search the Varmodel directory to add one.
    </div>
    <div>
      <div
        v-for="partner in selectedPartners"
        :key="partner.id"
        class="partner-item"
        :class="{
          'is-selected': partner.sel,
        }"
        @click="selectPartner(partner)"
      >
        <div
          class="partner-item__av"
          :style="{
            background: partner.bg,

            color: partner.col,
          }"
        >
          {{ partner.av }}
        </div>

        <div class="flex-grow-1">
          <div class="partner-item__name">
            {{ partner.name }}
          </div>

          <div class="partner-item__sub">
            {{ partner.sub }}
          </div>
        </div>

        <button class="vm-btn vm-btn--icon" @click.stop="removePartner(partner.id)">
          <i class="ti ti-trash"></i>
        </button>
      </div>
    </div>
    <div class="add-row" @click="toggleSearch">
      <i class="ti ti-search"></i><span>Search Varmodel directory to add a partner</span>
    </div>
    <div class="search-panel is-open" v-show="searchOpen">
      <div
        class="fw-700 mb-3"
        style="font-size: 11px; color: #0c447c; display: flex; align-items: center; gap: 5px"
      >
        <i class="ti ti-building-community"></i> Search Varmodel companies
      </div>
      <div class="search-wrap">
        <i class="ti ti-search"></i
        ><input
          class="search-input"
          id="dir-search"
          placeholder="Type company name, industry, or location…"
          v-model="searchText"
        />
      </div>
      <div>
        <div v-if="!searchText" class="search-empty">Type to search...</div>

        <div v-else-if="searchMatches.length === 0" class="search-empty">No companies found</div>

        <div v-else class="search-results-wrap">
          <div
            v-for="company in searchMatches"
            :key="company.name"
            class="search-result-item"
            @click="addFromSearch(company)"
          >
            <div
              class="search-result-item__av"
              :style="{
                background: company.bg,
                color: company.col,
              }"
            >
              {{ company.av }}
            </div>

            <div class="flex-grow-1">
              <div class="search-result-item__name">
                {{ company.name }}
              </div>

              <div class="search-result-item__meta">{{ company.ind }} · {{ company.loc }}</div>
            </div>

            <span
              class="search-badge"
              :class="company.st === 'partner' ? 'search-badge--partner' : 'search-badge--verified'"
            >
              {{ company.st === 'partner' ? 'Your partner' : 'Verified' }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="contact-section is-visible" id="contact-section">
      <div class="contact-section__title">
        <i class="ti ti-user"></i> Signing contact at
        <span style="color: var(--neutral-11)">
          {{ agreement.partner?.name || '—' }}
        </span>
      </div>
      <div class="form-row-2">
        <div class="form-field">
          <label class="vm-label"
            >Contact name <span style="color: var(--color-danger)">*</span></label
          ><input
            class="vm-input"
            v-model="agreement.contactName"
            placeholder="e.g. Maria Rivera"
          />
        </div>
        <div class="form-field">
          <label class="vm-label">Job title <span style="color: var(--color-danger)">*</span></label
          ><input
            class="vm-input"
            v-model="agreement.contactTitle"
            placeholder="e.g. Owner / CEO"
          />
        </div>
        <div class="form-field">
          <label class="vm-label">Email address</label
          ><input
            class="vm-input"
            v-model="agreement.contactEmail"
            placeholder="e.g. maria@riverabuilds.com"
          />
        </div>
        <div class="form-field">
          <label class="vm-label">Phone (optional)</label
          ><input
            class="vm-input"
            v-model="agreement.contactPhone"
            placeholder="e.g. +1 (408) 555-0120"
          />
        </div>
      </div>
    </div>
    <div class="initiator-section">
      <div class="section-sub-label">Your signing details (initiating party)</div>
      <div class="form-row-2">
        <div class="form-field">
          <label class="vm-label">Your name</label
          ><input class="vm-input" v-model="agreement.initiatorName" />
        </div>
        <div class="form-field">
          <label class="vm-label">Your title</label
          ><input class="vm-input" v-model="agreement.initiatorTitle" />
        </div>
      </div>
    </div>
    <!-- validation error -->
    <div
      v-if="step1Error"
      class="vm-notice vm-notice--warning"
      style="margin-top: 16px; border-radius: var(--radius-md)"
    >
      <i class="ti ti-alert-circle" style="font-size: 14px; flex-shrink: 0"></i>
      <div>
        Please fill in all required fields before continuing:
        <ul style="margin-top: 4px; padding-left: 16px; font-size: 11px">
          <li v-if="!agreement.partner">Select a partner company</li>
          <li v-if="!agreement.contactName?.trim()">Contact name is required</li>
          <li v-if="!agreement.contactTitle?.trim()">Contact job title is required</li>
          <li v-if="!agreement.contactEmail?.trim()">Contact email is required</li>
          <li v-if="!agreement.initiatorName?.trim()">Your name is required</li>
          <li v-if="!agreement.initiatorTitle?.trim()">Your title is required</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, inject } from 'vue'

const searchOpen = ref(false)
const dirCompanies = inject('dirCompanies', ref([]))
const selectedPartners = ref([])
const step1Error = inject('step1Error', ref(false))
const searchText = ref('')

const searchMatches = computed(() => {
  if (!searchText.value.trim()) return []

  return dirCompanies.value.filter((c) =>
    [c.name, c.ind, c.loc].some((v) =>
      v
        .toLowerCase()

        .includes(searchText.value.toLowerCase()),
    ),
  )
})

const agreement = inject('agreement')

function selectPartner(company) {
  agreement.value.partner = company

  selectedPartners.value.forEach((p) => (p.sel = false))

  company.sel = true
}

function toggleSearch() {
  searchOpen.value = !searchOpen.value
}

function removePartner(id) {
  selectedPartners.value = selectedPartners.value.filter((p) => p.id !== id)
}

function addFromSearch(company) {
  const exists = selectedPartners.value.some((p) => p.id === company.id)

  if (exists) return

  selectedPartners.value.push({
    ...company,
    sub: `${company.ind} · ${company.loc}`,
  })

  searchOpen.value = false

  searchText.value = ''
}
</script>
