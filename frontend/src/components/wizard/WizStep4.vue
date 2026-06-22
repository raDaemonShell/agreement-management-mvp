<template>
  <div class="wizard-screen" id="ws4">
    <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
      Review your agreement
    </div>
    <div class="neutral-7 mb-4" style="font-size: 12px">
      Click “Edit” on any section to modify content or use AI rewrite to replace a whole section.
    </div>
    <div class="vm-notice vm-notice--warning">
      <i class="ti ti-alert-triangle"></i> Starting point only. Varmodel is not liable for
      omissions. Consult an attorney before signing.
    </div>
    <div class="parties-card">
      <div class="parties-card__title"><i class="ti ti-users"></i> Parties to this agreement</div>
      <div class="parties-grid">
        <div class="party-block">
          <div class="party-block__label">Disclosing party</div>
          <div class="party-block__name">{{ agreement.myCompany }}</div>
          <div class="party-block__loc">{{ agreement.myCompanyLocation }}</div>
          <div class="party-block__contact">
            <i class="ti ti-user" style="font-size: 12px"></i> {{ agreement.initiatorName }}

            ·

            {{ agreement.initiatorTitle }}
          </div>
        </div>
        <div class="party-block">
          <div class="party-block__label">Receiving party</div>
          <div class="party-block__name">{{ agreement.partner?.name }}</div>
          <div class="party-block__loc">{{ agreement.partner?.loc }}</div>
          <div class="party-block__contact">
            <i class="ti ti-user" style="font-size: 12px"></i> {{ agreement.contactName }}

            ·

            {{ agreement.contactTitle }}
          </div>
        </div>
      </div>
    </div>
    <div class="contract-preview">
      <div class="contract-preview__header">
        <span class="vm-card__title">{{ agreementTitle }}</span
        ><span class="vm-pill vm-pill--draft">Draft</span>
      </div>
      <div class="sec-block" id="sec1">
        <div class="sec-block__top">
          <span class="sec-block__label">Section 1 — Parties</span
          ><button class="vm-btn vm-btn--sm" onclick="toggleEdit('sec1')">
            <i class="ti ti-edit"></i> Edit
          </button>
        </div>
        <div class="sec-block__body">
          This

          {{ agreement.agreementTypeTitle }}

          is entered into between Your Company and

          {{ agreement.partner?.name }}

          represented by

          {{ agreement.initiatorName }}

          and

          {{ agreement.contactName }}

          respectively.
        </div>
        <div class="sec-editor" id="sec1-editor">
          <textarea class="vm-textarea" id="sec1-ta" rows="3"></textarea>
          <div class="sec-editor__actions">
            <input
              class="vm-ai-prompt"
              id="sec1-ai"
              placeholder="Describe a change for AI to rewrite…"
            /><button class="vm-btn vm-btn--sm vm-btn--outline-primary" onclick="aiRewrite('sec1')">
              <i class="ti ti-sparkles"></i> Rewrite</button
            ><button class="vm-btn vm-btn--sm vm-btn--primary" onclick="saveEdit('sec1')">
              <i class="ti ti-check"></i> Save</button
            ><button class="vm-btn vm-btn--sm" onclick="cancelEdit('sec1')">Cancel</button>
          </div>
        </div>
      </div>
      <div class="sec-block" id="sec2">
        <div class="sec-block__top">
          <span class="sec-block__label">Section 2 — Confidential information</span
          ><button class="vm-btn vm-btn--sm" onclick="toggleEdit('sec2')">
            <i class="ti ti-edit"></i> Edit
          </button>
        </div>
        <div class="sec-block__body">
          The parties agree to protect all confidential information exchanged throughout this
          agreement. Protected information includes business information, technical information,
          documents, financial information, and proprietary materials.
        </div>
        <div class="sec-editor" id="sec2-editor">
          <textarea class="vm-textarea" id="sec2-ta" rows="3"></textarea>
          <div class="sec-editor__actions">
            <input class="vm-ai-prompt" id="sec2-ai" placeholder="Describe a change…" /><button
              class="vm-btn vm-btn--sm vm-btn--outline-primary"
              onclick="aiRewrite('sec2')"
            >
              <i class="ti ti-sparkles"></i> Rewrite</button
            ><button class="vm-btn vm-btn--sm vm-btn--primary" onclick="saveEdit('sec2')">
              <i class="ti ti-check"></i> Save</button
            ><button class="vm-btn vm-btn--sm" onclick="cancelEdit('sec2')">Cancel</button>
          </div>
        </div>
      </div>
      <div class="sec-block" id="sec3">
        <div class="sec-block__top">
          <span class="sec-block__label">Section 3 — Obligations</span
          ><button class="vm-btn vm-btn--sm" onclick="toggleEdit('sec3')">
            <i class="ti ti-edit"></i> Edit
          </button>
        </div>
        <div class="sec-block__body">
          This agreement is primarily intended for

          {{ agreement.purpose }}. The receiving party agrees to properly safeguard

          {{ agreement.intellectualProperty }}

          throughout the duration of the agreement.
        </div>
        <div class="sec-editor" id="sec3-editor">
          <textarea class="vm-textarea" id="sec3-ta" rows="3"></textarea>
          <div class="sec-editor__actions">
            <input class="vm-ai-prompt" id="sec3-ai" placeholder="Describe a change…" /><button
              class="vm-btn vm-btn--sm vm-btn--outline-primary"
              onclick="aiRewrite('sec3')"
            >
              <i class="ti ti-sparkles"></i> Rewrite</button
            ><button class="vm-btn vm-btn--sm vm-btn--primary" onclick="saveEdit('sec3')">
              <i class="ti ti-check"></i> Save</button
            ><button class="vm-btn vm-btn--sm" onclick="cancelEdit('sec3')">Cancel</button>
          </div>
        </div>
      </div>
      <div class="sec-block" id="sec4">
        <div class="sec-block__top">
          <span class="sec-block__label">Section 4 — Term</span
          ><button class="vm-btn vm-btn--sm" onclick="toggleEdit('sec4')">
            <i class="ti ti-edit"></i> Edit
          </button>
        </div>
        <div class="sec-block__body">
          This agreement shall remain in effect from

          {{ agreement.startDate }}

          to

          {{ agreement.endDate }}

          and shall be governed by

          {{ agreement.governingLaw }}

          law.
        </div>
        <div class="sec-editor" id="sec4-editor">
          <textarea class="vm-textarea" id="sec4-ta" rows="2"></textarea>
          <div class="sec-editor__actions">
            <input class="vm-ai-prompt" id="sec4-ai" placeholder="Describe a change…" /><button
              class="vm-btn vm-btn--sm vm-btn--outline-primary"
              onclick="aiRewrite('sec4')"
            >
              <i class="ti ti-sparkles"></i> Rewrite</button
            ><button class="vm-btn vm-btn--sm vm-btn--primary" onclick="saveEdit('sec4')">
              <i class="ti ti-check"></i> Save</button
            ><button class="vm-btn vm-btn--sm" onclick="cancelEdit('sec4')">Cancel</button>
          </div>
        </div>
      </div>
      <div class="sec-block" id="sec5">
        <div class="sec-block__top">
          <span class="sec-block__label">Section 5 — Remedies</span
          ><button class="vm-btn vm-btn--sm" onclick="toggleEdit('sec5')">
            <i class="ti ti-edit"></i> Edit
          </button>
        </div>
        <div class="sec-block__body">
          If either party breaches this agreement, the non-breaching party may pursue legal and
          equitable remedies available under governing law.
        </div>
        <div class="sec-editor" id="sec5-editor">
          <textarea class="vm-textarea" id="sec5-ta" rows="2"></textarea>
          <div class="sec-editor__actions">
            <input class="vm-ai-prompt" id="sec5-ai" placeholder="Describe a change…" /><button
              class="vm-btn vm-btn--sm vm-btn--outline-primary"
              onclick="aiRewrite('sec5')"
            >
              <i class="ti ti-sparkles"></i> Rewrite</button
            ><button class="vm-btn vm-btn--sm vm-btn--primary" onclick="saveEdit('sec5')">
              <i class="ti ti-check"></i> Save</button
            ><button class="vm-btn vm-btn--sm" onclick="cancelEdit('sec5')">Cancel</button>
          </div>
        </div>
      </div>
      <div class="sec-block">
        <div class="sec-block__top">
          <span class="sec-block__label">Section 6 — Special provisions</span
          ><button class="vm-btn vm-btn--sm vm-btn--outline-primary">
            <i class="ti ti-sparkles"></i> AI rewrite
          </button>
        </div>
        <div class="ai-block">
          <div class="ai-block__label">
            <i class="ti ti-sparkles"></i> AI-generated from your answers
          </div>
          <div class="ai-block__body">
            Special protections have been generated based on: Purpose:
            {{ agreement.purpose }}

            Protected assets:
            {{ agreement.intellectualProperty }}

            Governing law:
            {{ agreement.governingLaw }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { inject, computed } from 'vue'

const agreement = inject('agreement')

const agreementTitle = computed(() => {
  if (!agreement.value.agreementTypeTitle || !agreement.value.partner) {
    return 'New Agreement'
  }

  return `${agreement.value.agreementTypeTitle} × ${agreement.value.partner.name}`
})
</script>
