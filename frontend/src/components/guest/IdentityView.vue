<template>
  <div class="page-wrap" v-if="agreement">
    <div class="vm-card">
      <div class="vm-card__header">
        <div>
          <div class="vm-card__title">Confirm your identity</div>
          <div style="font-size: 11px; color: var(--neutral-6); margin-top: 2px">
            Before signing, we need to verify your email address. This protects both parties.
          </div>
        </div>
      </div>
      <div class="p-5">
        <div class="mb-3">
          <label class="vm-label"
            ><i class="ti ti-user" style="font-size: 13px"></i> Full name</label
          >
          <input class="vm-input vm-input--readonly" :value="agreement.contact_name" readonly />
        </div>
        <div class="mb-3">
          <label class="vm-label"
            ><i class="ti ti-building" style="font-size: 13px"></i> Company</label
          >
          <input class="vm-input vm-input--readonly" :value="agreement.partner?.name" readonly />
        </div>
        <div class="mb-4">
          <label class="vm-label">
            <i class="ti ti-mail" style="font-size: 13px"></i> Email address
            <span style="color: var(--color-danger)">*</span>
          </label>
          <input class="vm-input vm-input--verified" :value="agreement.contact_email" readonly />
          <div class="verify-strip">
            <i class="ti ti-circle-check" style="font-size: 13px"></i>
            Email matches invitation &middot; Verification code sent
          </div>
        </div>

        <div class="fw-500 mb-2" style="font-size: 12px; color: var(--neutral-11)">
          Enter the 6-digit code sent to {{ agreement.contact_email }}
        </div>
        <div class="otp-grid">
          <input
            v-for="(digit, index) in otp"
            :key="index"
            :ref="(el) => (otpRefs[index] = el)"
            class="otp-box"
            :class="{ 'otp-box--filled': digit }"
            maxlength="1"
            type="text"
            inputmode="numeric"
            :value="digit"
            @input="handleOtpInput($event, index)"
            @keydown.backspace="handleBackspace($event, index)"
            style="
              outline: none;
              text-align: center;
              width: 100%;
              font-size: 14px;
              font-weight: 500;
              cursor: text;
              box-sizing: border-box;
            "
          />
        </div>

        <div class="vm-notice vm-notice--info mb-4" style="border-radius: var(--radius-md)">
          <i class="ti ti-info-circle" style="font-size: 14px; flex-shrink: 0"></i>
          Your email, IP address, device, and timestamp are recorded at signing as part of the audit
          trail. This data is included in the signed PDF shared with both parties.
        </div>

        <button
          class="vm-btn vm-btn--primary vm-btn--lg vm-btn--block mb-2"
          @click="$emit('next')"
          :disabled="!otpComplete"
          :style="{ opacity: otpComplete ? 1 : 0.5 }"
        >
          <i class="ti ti-arrow-right" style="font-size: 16px"></i> Continue to signature
        </button>
        <div style="font-size: 10px; color: var(--neutral-6); text-align: center; margin-top: 6px">
          Didn&rsquo;t receive the code?
          <span style="color: var(--primary); cursor: pointer">Resend</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  agreement: Object,
})

defineEmits(['next'])

const otp = ref(['', '', '', '', '', ''])
const otpRefs = ref([])

const otpComplete = computed(() => otp.value.every((d) => d !== ''))

function handleOtpInput(event, index) {
  const val = event.target.value.replace(/\D/g, '')
  otp.value[index] = val
  if (val && index < 5) {
    otpRefs.value[index + 1]?.focus()
  }
}

function handleBackspace(event, index) {
  if (!otp.value[index] && index > 0) {
    otp.value[index - 1] = ''
    otpRefs.value[index - 1]?.focus()
  }
}
</script>
