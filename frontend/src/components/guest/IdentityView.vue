<template>
  <div class="screen" id="s3">
    <div class="screen-strip">Screen 3 &mdash; Identity verification</div>
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
            <label class="vm-label"
              ><i class="ti ti-user" style="font-size: 13px"></i> Full name</label
            >
            <input class="vm-input vm-input--readonly" value="Maria Rivera" readonly />
          </div>
          <div class="mb-3">
            <label class="vm-label"
              ><i class="ti ti-building" style="font-size: 13px"></i> Company</label
            >
            <input class="vm-input vm-input--readonly" value="Rivera Builds LLC" readonly />
          </div>
          <div class="mb-4">
            <label class="vm-label"
              ><i class="ti ti-mail" style="font-size: 13px"></i> Email address
              <span style="color: var(--color-danger)">*</span></label
            >
            <input class="vm-input vm-input--verified" value="maria@riverabuilds.com" readonly />
            <div class="verify-strip">
              <i class="ti ti-circle-check" style="font-size: 13px"></i> Email matches invitation
              &middot; Verification code sent
            </div>
          </div>

          <div class="fw-500 mb-2" style="font-size: 12px; color: var(--neutral-11)">
            Enter the 6-digit code sent to maria@riverabuilds.com
          </div>
          <div class="otp-grid">
            <div class="otp-box otp-box--filled">4</div>
            <div class="otp-box otp-box--filled">7</div>
            <div class="otp-box otp-box--filled">2</div>
            <div class="otp-box otp-box--filled">9</div>
            <div class="otp-box otp-box--filled">1</div>
            <div class="otp-box otp-box--filled">6</div>
          </div>

          <div class="vm-notice vm-notice--info mb-4" style="border-radius: var(--radius-md)">
            <i class="ti ti-info-circle" style="font-size: 14px; flex-shrink: 0"></i>
            Your email, IP address, device, and timestamp are recorded at signing as part of the
            audit trail. This data is included in the signed PDF shared with both parties.
          </div>

          <button class="vm-btn vm-btn--primary vm-btn--lg vm-btn--block mb-2" onclick="goTo(4)">
            <i class="ti ti-arrow-right" style="font-size: 16px"></i> Continue to signature
          </button>
          <div
            style="font-size: 10px; color: var(--neutral-6); text-align: center; margin-top: 6px"
          >
            Didn&rsquo;t receive the code?
            <span style="color: var(--primary); cursor: pointer">Resend</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
