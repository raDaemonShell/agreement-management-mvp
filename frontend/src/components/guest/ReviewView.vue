<template>
  <div class="screen-strip">Screen 2 — Agreement review portal</div>
  <div class="page-wrap--wide">
    <div
      class="vm-notice vm-notice--purple"
      style="margin: 12px 16px; border-radius: var(--radius-md)"
    >
      <i class="ti ti-mail" style="font-size: 18px; color: #7c3aed; flex-shrink: 0"></i>
      <div>
        <div class="fw-500 mb-1" style="color: #3c3489">
          {{ agreement.initiator_name }} from {{ agreement.initiator_company }} has requested your
          signature
        </div>
        <div style="color: #5b21b6; font-size: 11px">
          Review the full agreement below. You may forward this link to your attorney before
          signing.
        </div>
      </div>
    </div>

    <div
      class="doc-layout"
      style="background: var(--color-white); border-top: 1px solid var(--border-color-light)"
    >
      <div class="doc-main">
        <div class="doc-header">
          <div class="doc-title">{{ agreementTypeTitle }}</div>
          <div class="doc-sub">
            {{ agreement.initiator_company }} &times; {{ agreement.contact_name }} &middot;
            {{ startDate }} &ndash; {{ endDate }} &middot; {{ agreement.governing_law }} law
          </div>
        </div>

        <div class="doc-parties">
          <div class="doc-party">
            <div class="doc-party__badge">Disclosing party</div>
            <div class="doc-party__name">{{ agreement.initiator_company }}</div>
            <div class="doc-party__loc">{{ agreement.initiator_location }}</div>
            <div class="doc-party__contact">
              <i class="ti ti-user" style="font-size: 10px"></i>
              {{ agreement.initiator_name }} &middot; {{ agreement.initiator_title }}
            </div>
          </div>
          <div class="doc-party doc-party--you">
            <div class="doc-party__badge doc-party__badge--you">Receiving party (you)</div>
            <div class="doc-party__name">{{ agreement.partner?.name }}</div>
            <div class="doc-party__loc">{{ agreement.partner?.loc }}</div>
            <div class="doc-party__contact">
              <i class="ti ti-user" style="font-size: 10px"></i>
              {{ agreement.contact_name }} &middot; {{ agreement.contact_title }}
            </div>
          </div>
        </div>

        <div class="doc-sec">
          <div class="doc-sec__title">1. Parties</div>
          <div class="doc-sec__body">
            This {{ agreementTypeTitle }} is entered into as of the date of last signature by
            {{ agreement.initiator_company }}, represented by {{ agreement.initiator_name }} ({{
              agreement.initiator_title
            }}) (&ldquo;Disclosing Party&rdquo;), and {{ agreement.contact_name }}, represented by
            {{ agreement.contact_name }} ({{ agreement.contact_title }}) (&ldquo;Receiving
            Party&rdquo;), collectively the &ldquo;Parties.&rdquo;
          </div>
        </div>

        <div class="doc-sec">
          <div class="doc-sec__title">2. Confidential information</div>
          <div class="doc-sec__body">
            &ldquo;Confidential Information&rdquo; means any non-public information disclosed by
            either Party, including but not limited to trade secrets, business plans, financial
            data, and technical information in any form&hellip;
          </div>
        </div>

        <div class="doc-sec">
          <div class="doc-sec__title">3. Obligations</div>
          <div class="doc-sec__body">
            Each Party agrees to hold the other&rsquo;s Confidential Information in strict
            confidence, use it solely for the {{ agreement.purpose }}, and not disclose to any third
            party without prior written consent&hellip;
          </div>
        </div>

        <div class="doc-sec">
          <div class="doc-sec__title">4. Term</div>
          <div class="doc-sec__body">
            This Agreement shall remain in effect from {{ startDate }} to {{ endDate }} ({{
              duration
            }}), governed by the laws of the State of {{ agreement.governing_law }}.
          </div>
        </div>

        <div class="doc-sec">
          <div class="doc-sec__title">5. Remedies</div>
          <div class="doc-sec__body">
            Each Party acknowledges that breach may cause irreparable harm, entitling the
            non-breaching Party to seek equitable relief in addition to legal remedies available at
            law&hellip;
          </div>
        </div>

        <div class="doc-ai-block">
          <div class="doc-ai-block__label">
            <i class="ti ti-sparkles" style="font-size: 9px"></i> Section 6 &mdash; Special
            provisions
          </div>
          <div class="doc-ai-block__body">
            {{ agreement.initiator_company }} retains exclusive ownership of all
            {{ agreement.intellectual_property }} disclosed during the {{ agreement.purpose }}.
            {{ agreement.contact_name }} shall implement reasonable safeguards to prevent
            unauthorized access. Derivative insights arising from shared information remain the sole
            property of the originating Party for the duration of this Agreement under
            {{ agreement.governing_law }} law.
          </div>
        </div>

        <div class="d-flex gap-2 mt-3">
          <button class="vm-btn vm-btn--sm"><i class="ti ti-share"></i> Forward to counsel</button>
          <button class="vm-btn vm-btn--sm"><i class="ti ti-download"></i> Download PDF</button>
        </div>
      </div>

      <div class="doc-sidebar">
        <div class="sidebar-section">
          <span class="sidebar-label">Signature status</span>
          <div class="sig-slot">
            <div class="sig-slot__label">{{ agreement.initiator_company }} &mdash; signed</div>
            <div class="sig-slot__name">{{ agreement.initiator_name }}</div>
            <div class="sig-slot__meta">
              <i class="ti ti-check" style="font-size: 10px; color: #27500a"></i>
              {{ initiatorSignedDate }}
            </div>
          </div>
          <div class="sig-slot sig-slot--you">
            <div class="sig-slot__label sig-slot__label--you">
              {{ agreement.contact_name }} &mdash; awaiting you
            </div>
            <div class="sig-slot__blank"></div>
            <div class="sig-slot__meta sig-slot__meta--you">Your signature needed</div>
          </div>
        </div>

        <div class="sidebar-section">
          <span class="sidebar-label">Agreement details</span>
          <div class="detail-row">
            Type: <strong>{{ agreement.agreement_type }}</strong
            ><br />
            Period: <strong>{{ duration }}</strong
            ><br />
            Law: <strong>{{ agreement.governing_law }}</strong
            ><br />
            Expires: <strong style="color: #854f0b">{{ expiryDate }}</strong>
          </div>
        </div>

        <button class="vm-btn vm-btn--primary vm-btn--block mb-2" @click="$emit('next')">
          <i class="ti ti-writing"></i> Proceed to sign
        </button>
        <button class="vm-btn vm-btn--block mb-3">
          <i class="ti ti-share"></i> Forward to attorney
        </button>
        <div
          style="
            background: #fffbe6;
            border: 1px solid #e6c200;
            border-radius: var(--radius-md);
            padding: 8px 10px;
            font-size: 10px;
            color: #7a5c00;
            line-height: 1.5;
          "
        >
          Not a lawyer? We recommend sharing this link with your counsel before signing.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  agreement: Object,
})

defineEmits(['next'])

const agreementTypeMap = {
  NDA: 'Non-Disclosure Agreement',
  MSA: 'Master Services Agreement',
  TEAMING: 'Teaming Agreement',
  SUBCONTRACTOR: 'Subcontractor Agreement',
  LOI: 'Letter of Intent',
}

const agreementTypeTitle = computed(
  () => agreementTypeMap[props.agreement.agreement_type] || props.agreement.agreement_type,
)

const fmt = (dateStr) =>
  new Date(dateStr).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })

const startDate = computed(() => fmt(props.agreement.start_date))
const endDate = computed(() => fmt(props.agreement.end_date))
const initiatorSignedDate = computed(() =>
  fmt(props.agreement.initiator_signed_at || props.agreement.created_at),
)

const expiryDate = computed(() => {
  const d = new Date(props.agreement.created_at)
  d.setDate(d.getDate() + props.agreement.link_expiration_days)
  return fmt(d)
})

const duration = computed(() => {
  const start = new Date(props.agreement.start_date)
  const end = new Date(props.agreement.end_date)
  const days = Math.ceil((end - start) / (1000 * 60 * 60 * 24))
  const years = Math.floor(days / 365)
  if (years >= 1) return `${years} year${years > 1 ? 's' : ''}`
  return `${days} days`
})
</script>
