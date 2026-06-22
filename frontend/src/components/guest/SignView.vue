<template>
  <div class="screen" id="s4">
    <div class="screen-strip">Screen 4 &mdash; Signature capture</div>
    <div class="page-wrap">
      <div class="vm-card">
        <div class="vm-card__header">
          <div>
            <div class="vm-card__title">Sign the agreement</div>
            <div style="font-size: 11px; color: var(--neutral-6); margin-top: 2px">
              By signing, you confirm you have read and agree to all terms.
            </div>
          </div>
          <span class="vm-pill vm-pill--info" style="font-size: 10px"
            >NDA &middot; TechVentures &times; Rivera Builds</span
          >
        </div>
        <div class="p-5">
          <span class="sidebar-label">Signature status</span>
          <div class="sign-parties mt-2">
            <div class="sign-slot">
              <div class="sign-slot__label">TechVentures Inc</div>
              <div class="sig-display">John Doe</div>
              <div class="sig-check">
                <i class="ti ti-check" style="font-size: 11px"></i> Signed Jun 1, 2026
              </div>
            </div>
            <div class="sign-slot sign-slot--active">
              <div class="sign-slot__label sign-slot__label--active">
                Rivera Builds LLC &mdash; your signature
              </div>
              <input
                class="sig-input"
                id="sig-field"
                placeholder="Type your full legal name"
                value="Maria Rivera"
              />
              <div class="sig-hint">Your typed name constitutes a legal signature</div>
            </div>
          </div>

          <span class="sidebar-label">Captured at signing</span>
          <div class="capture-grid mt-2">
            <div class="capture-item">
              <div class="capture-item__label">Full name</div>
              <div class="capture-item__value">Maria Rivera</div>
            </div>
            <div class="capture-item">
              <div class="capture-item__label">Email</div>
              <div class="capture-item__value">maria@riverabuilds.com</div>
            </div>
            <div class="capture-item">
              <div class="capture-item__label">IP address</div>
              <div class="capture-item__value">192.168.4.21</div>
            </div>
            <div class="capture-item">
              <div class="capture-item__label">Timestamp</div>
              <div class="capture-item__value">Jun 3, 2026 &middot; 2:17 PM PST</div>
            </div>
            <div class="capture-item">
              <div class="capture-item__label">Device</div>
              <div class="capture-item__value">Chrome 124 &middot; macOS</div>
            </div>
            <div class="capture-item">
              <div class="capture-item__label">Identity</div>
              <div class="capture-item__value capture-item__value--ok">
                <i class="ti ti-circle-check" style="font-size: 12px"></i> Email verified
              </div>
            </div>
          </div>

          <div class="legal-confirm" id="confirm-box" onclick="toggleConfirm()">
            <div class="checkbox" id="chk"></div>
            <div style="font-size: 12px; color: var(--neutral-7); line-height: 1.6">
              I confirm I have read the full agreement, I agree to all terms, and I understand that
              my typed name constitutes a legally binding signature.
            </div>
          </div>

          <button class="vm-btn vm-btn--primary vm-btn--lg vm-btn--block mb-2" onclick="goTo(5)">
            <i class="ti ti-writing" style="font-size: 16px"></i> Sign &amp; execute agreement
          </button>
          <div
            style="font-size: 10px; color: var(--neutral-5); text-align: center; line-height: 1.5"
          >
            Varmodel is not a law firm. This is not legal advice. Audit data is shared with both
            parties upon execution.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
