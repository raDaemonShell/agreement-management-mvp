<template>
  <div class="wizard-screen is-active" id="ws4">
    <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
      Review your agreement
    </div>

    <div class="neutral-7 mb-4" style="font-size: 12px">
      Click “Edit” on any section to modify content or use AI rewrite to replace a whole section.
    </div>

    <div class="vm-notice vm-notice--warning">
      <i class="ti ti-alert-triangle"></i>
      Starting point only. Varmodel is not liable for omissions. Consult an attorney before signing.
    </div>

    <div class="parties-card">
      <div class="parties-card__title">
        <i class="ti ti-users"></i>
        Parties to this agreement
      </div>

      <div class="parties-grid">
        <div class="party-block">
          <div class="party-block__label">Disclosing party</div>
          <div class="party-block__name">{{ agreement.myCompany }}</div>
          <div class="party-block__loc">{{ agreement.myCompanyLocation }}</div>
          <div class="party-block__contact">
            <i class="ti ti-user" style="font-size: 12px"></i>
            {{ agreement.initiatorName }} · {{ agreement.initiatorTitle }}
          </div>
        </div>

        <div class="party-block">
          <div class="party-block__label">Receiving party</div>
          <div class="party-block__name">{{ agreement.partner?.name }}</div>
          <div class="party-block__loc">{{ agreement.partner?.loc }}</div>
          <div class="party-block__contact">
            <i class="ti ti-user" style="font-size: 12px"></i>
            {{ agreement.contactName }} · {{ agreement.contactTitle }}
          </div>
        </div>
      </div>
    </div>

    <div class="contract-preview">
      <div class="contract-preview__header">
        <span class="vm-card__title">{{ contractTitle }}</span>
        <span class="vm-pill vm-pill--draft">Draft</span>
      </div>

      <div v-for="section in editableSections" :key="section.id" class="sec-block" :id="section.id">
        <div class="sec-block__top">
          <span class="sec-block__label">{{ section.title }}</span>
          <button class="vm-btn vm-btn--sm" @click="toggleEdit(section.id)">
            <i class="ti ti-edit"></i>
            Edit
          </button>
        </div>

        <div
          class="sec-block__body"
          :id="`${section.id}-body`"
          v-show="editingSection !== section.id"
        >
          {{ agreement.sections[section.id] }}
        </div>

        <div
          class="sec-editor"
          :id="`${section.id}-editor`"
          :class="{ 'is-open': editingSection === section.id }"
          v-show="editingSection === section.id"
        >
          <textarea
            class="vm-textarea"
            :id="`${section.id}-ta`"
            :rows="section.rows"
            v-model="tempText"
          ></textarea>

          <div class="sec-editor__actions">
            <input
              class="vm-ai-prompt"
              :id="`${section.id}-ai`"
              v-model="aiPrompt"
              :placeholder="section.aiPlaceholder"
            />
            <button
              class="vm-btn vm-btn--sm vm-btn--outline-primary"
              @click="aiRewrite(section.id)"
            >
              <i class="ti ti-sparkles"></i>
              Rewrite
            </button>
            <button
              class="vm-btn vm-btn--sm vm-btn--primary"
              @click="saveEdit(section.id)"
            >
              <i class="ti ti-check"></i>
              Save
            </button>
            <button class="vm-btn vm-btn--sm" @click="cancelEdit">Cancel</button>
          </div>
        </div>
      </div>

      <div class="sec-block" id="sec6">
        <div class="sec-block__top">
          <span class="sec-block__label">Section 6 — Special provisions</span>
          <button
            v-if="editingSection !== 'sec6'"
            class="vm-btn vm-btn--sm vm-btn--outline-primary"
            @click="toggleEdit('sec6')"
          >
            <i class="ti ti-sparkles"></i>
            AI rewrite
          </button>
        </div>

        <div v-show="editingSection !== 'sec6'" class="ai-block">
          <div class="ai-block__label">
            <i class="ti ti-sparkles"></i>
            AI-generated from your answers
          </div>
          <div class="ai-block__body">{{ agreement.sections.sec6 }}</div>
        </div>

        <div
          class="sec-editor"
          id="sec6-editor"
          :class="{ 'is-open': editingSection === 'sec6' }"
          v-show="editingSection === 'sec6'"
        >
          <textarea
            class="vm-textarea"
            id="sec6-ta"
            rows="3"
            v-model="tempText"
          ></textarea>

          <div class="sec-editor__actions">
            <input
              class="vm-ai-prompt"
              id="sec6-ai"
              v-model="aiPrompt"
              placeholder="Describe a change…"
            />
            <button
              class="vm-btn vm-btn--sm vm-btn--outline-primary"
              @click="aiRewrite('sec6')"
            >
              <i class="ti ti-sparkles"></i>
              Rewrite
            </button>
            <button class="vm-btn vm-btn--sm vm-btn--primary" @click="saveEdit('sec6')">
              <i class="ti ti-check"></i>
              Save
            </button>
            <button class="vm-btn vm-btn--sm" @click="cancelEdit">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { inject, ref, computed, onMounted } from 'vue'

const agreement = inject('agreement')

const editingSection = ref(null)
const tempText = ref('')
const aiPrompt = ref('')

const editableSections = [
  { id: 'sec1', title: 'Section 1 — Parties', rows: 3, aiPlaceholder: 'Describe a change for AI to rewrite…' },
  { id: 'sec2', title: 'Section 2 — Confidential information', rows: 3, aiPlaceholder: 'Describe a change…' },
  { id: 'sec3', title: 'Section 3 — Obligations', rows: 3, aiPlaceholder: 'Describe a change…' },
  { id: 'sec4', title: 'Section 4 — Term', rows: 2, aiPlaceholder: 'Describe a change…' },
  { id: 'sec5', title: 'Section 5 — Remedies', rows: 2, aiPlaceholder: 'Describe a change…' },
]

const contractTitle = computed(() => {
  const type = agreement.value.agreementType || 'Agreement'
  const partner = agreement.value.partner?.name || 'Partner'
  return `${type} — ${agreement.value.myCompany} × ${partner}`
})

function formatDisplayDate(dateString) {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}

function durationLabel() {
  const { startDate, endDate } = agreement.value
  if (!startDate || !endDate) return ''

  const start = new Date(startDate)
  const end = new Date(endDate)
  const days = Math.ceil((end - start) / (1000 * 60 * 60 * 24))

  if (days <= 0) return 'invalid duration'

  const years = Math.floor(days / 365)
  if (years >= 1) return `${years} year${years > 1 ? 's' : ''}`

  return `${days} days`
}

/** e.g. "Joint project bid" → "the joint project bid" */
function withThe(text) {
  if (!text) return 'the permitted purpose'
  const lower = text.toLowerCase()
  return lower.startsWith('the ') ? lower : `the ${lower}`
}

/** Step 3 intellectualProperty → prose for Section 6 */
function ipOwnershipPhrase(ip) {
  switch (ip) {
    case 'Yes — trade secrets':
      return 'proprietary methods and trade secrets'
    case 'Yes — patents':
      return 'patents and proprietary inventions'
    case 'Yes — methods':
      return 'proprietary methods'
    case 'No':
      return 'shared information'
    default:
      return 'proprietary methods and trade secrets'
  }
}

/** Step 2 title without parenthetical, e.g. "Non-Disclosure Agreement (NDA)" → "Non-Disclosure Agreement" */
function agreementProseTitle(title) {
  if (!title) return 'Non-Disclosure Agreement'
  return title.replace(/\s*\([^)]*\)/, '').trim()
}

function buildDefaultSections() {
  const a = agreement.value
  const partnerName = a.partner?.name || 'the Receiving Party'
  const proseTitle = agreementProseTitle(a.agreementTypeTitle)
  const purpose = withThe(a.purpose)
  const governingLaw = a.governingLaw || 'California'
  const ipPhrase = ipOwnershipPhrase(a.intellectualProperty)

  return {
    sec1: `This ${proseTitle} is entered into as of the date of last signature by ${a.myCompany}, represented by ${a.initiatorName} (${a.initiatorTitle}) (“Disclosing Party”), and ${partnerName}, represented by ${a.contactName} (${a.contactTitle}) (“Receiving Party”), collectively the “Parties.”`,

    sec2:
      '“Confidential Information” means any non-public information disclosed by either Party, including trade secrets, business plans, financial data, and technical information in any form…',

    sec3: `Each Party agrees to hold the other’s Confidential Information in strict confidence, use it solely for ${purpose}, and not disclose to any third party without prior written consent…`,

    sec4: `This Agreement shall remain in effect from ${formatDisplayDate(a.startDate)} to ${formatDisplayDate(a.endDate)} (${durationLabel()}), governed by the laws of the State of ${governingLaw}.`,

    sec5:
      'Each Party acknowledges that breach may cause irreparable harm, entitling the non-breaching Party to seek equitable relief in addition to legal remedies available at law…',

    sec6: `${a.myCompany} retains exclusive ownership of all ${ipPhrase} disclosed during ${purpose}. ${partnerName} shall implement reasonable safeguards to prevent unauthorized access. Derivative insights arising from shared information remain the sole property of the originating Party for the duration of this Agreement under ${governingLaw} law.`,
  }
}

onMounted(() => {
  const defaults = buildDefaultSections()
  for (const [key, text] of Object.entries(defaults)) {
    if (!agreement.value.sections[key]) {
      agreement.value.sections[key] = text
    }
  }
})

function toggleEdit(id) {
  editingSection.value = id
  tempText.value = agreement.value.sections[id] || ''
  aiPrompt.value = ''
}

function saveEdit(id) {
  agreement.value.sections[id] = tempText.value
  editingSection.value = null
  tempText.value = ''
  aiPrompt.value = ''
}

function cancelEdit() {
  editingSection.value = null
  tempText.value = ''
  aiPrompt.value = ''
}

function aiRewrite(id) {
  const prompt = aiPrompt.value.trim()
  if (!prompt) return

  // Placeholder until an AI rewrite API is available — applies the prompt as an inline revision note.
  const base = tempText.value || agreement.value.sections[id] || ''
  tempText.value = `${base}\n\n[Revised per your request: ${prompt}]`
  aiPrompt.value = ''
}
</script>
