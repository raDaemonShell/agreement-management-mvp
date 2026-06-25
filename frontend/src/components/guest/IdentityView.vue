<template>
  <div v-if="agreement">
    <!-- ← single root wrapper -->
    <div class="page-wrap">
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
            <label class="vm-label">
              <i class="ti ti-user" style="font-size: 13px"></i> Full name
            </label>
            <input class="vm-input vm-input--readonly" :value="agreement.contact_name" readonly />
          </div>
          <div class="mb-3">
            <label class="vm-label">
              <i class="ti ti-building" style="font-size: 13px"></i> Company
            </label>
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
            Your email, IP address, device, and timestamp are recorded at signing as part of the
            audit trail. This data is included in the signed PDF shared with both parties.
          </div>

          <button
            class="vm-btn vm-btn--primary vm-btn--lg vm-btn--block mb-2"
            @click="verifyAndContinue"
            :disabled="!otpComplete || verifying"
            :style="{ opacity: otpComplete && !verifying ? 1 : 0.5 }"
          >
            <i class="ti ti-arrow-right" style="font-size: 16px"></i>
            {{ verifying ? 'Verifying...' : 'Continue to signature' }}
          </button>

          <!-- error message -->
          <div
            v-if="otpError"
            style="color: var(--color-danger); font-size: 12px; text-align: center; margin-top: 8px"
          >
            {{ otpError }}
          </div>
          <div
            style="font-size: 10px; color: var(--neutral-6); text-align: center; margin-top: 6px"
          >
            Didn&rsquo;t receive the code?
            <span style="color: var(--primary); cursor: pointer" @click="resendOtp">Resend</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const otp = ref(['', '', '', '', '', ''])
const otpRefs = ref([])
const verifying = ref(false)
const otpError = ref('')

const otpComplete = computed(() => otp.value.every((d) => d !== ''))
const emit = defineEmits(['next'])
const props = defineProps({
  agreement: Object,
})

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
async function verifyAndContinue() {
  if (!otpComplete.value) return
  verifying.value = true
  otpError.value = ''

  try {
    const code = otp.value.join('')
    const response = await fetch(
      `http://127.0.0.1:8000/api/agreements/${props.agreement.id}/verify_otp/`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code }),
      },
    )

    const data = await response.json()

    if (!response.ok) {
      otpError.value = data.error || 'Invalid code. Please try again.'
      return
    }

    emit('next')
  } catch (err) {
    console.error('OTP verification error:', err)
    otpError.value = 'Something went wrong. Please try again.'
  } finally {
    verifying.value = false
  }
}
async function resendOtp() {
  await fetch(`http://127.0.0.1:8000/api/agreements/${props.agreement.id}/send_otp/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
  })
  otp.value = ['', '', '', '', '', '']
  otpError.value = ''
}
</script>
