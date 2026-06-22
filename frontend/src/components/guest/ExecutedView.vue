<template>
  <div class="screen" id="s5">
    <div class="screen-strip">Screen 5 &mdash; Execution confirmed</div>
    <div class="page-wrap">
      <div class="vm-card">
        <div class="executed-header">
          <div class="success-circle">
            <i class="ti ti-check" style="font-size: 22px; color: #27500a"></i>
          </div>
          <div class="fw-700 mb-1" style="font-size: 16px; color: var(--neutral-12)">
            Agreement executed
          </div>
          <div style="font-size: 12px; color: var(--neutral-7); line-height: 1.6">
            Both parties have signed. Copies sent to john@techventures.com and
            maria@riverabuilds.com
          </div>
        </div>

        <div class="exe-parties">
          <div class="exe-party">
            <div class="exe-party__name">John Doe</div>
            <div class="exe-party__co">TechVentures Inc</div>
            <div class="exe-party__sig">
              <i class="ti ti-check" style="font-size: 10px"></i> Signed Jun 1, 2026
            </div>
          </div>
          <div class="exe-party">
            <div class="exe-party__name">Maria Rivera</div>
            <div class="exe-party__co">Rivera Builds LLC</div>
            <div class="exe-party__sig">
              <i class="ti ti-check" style="font-size: 10px"></i> Signed Jun 3, 2026
            </div>
          </div>
        </div>

        <div class="audit-block">
          <div class="audit-title">
            <i class="ti ti-shield-check" style="font-size: 15px; color: #27500a"></i> Signing audit
            record &mdash; Rivera Builds LLC
          </div>
          <div class="audit-row">
            <span class="audit-key">Signatory</span
            ><span class="audit-val">Maria Rivera &middot; Owner</span>
          </div>
          <div class="audit-row">
            <span class="audit-key">Email</span
            ><span class="audit-val">maria@riverabuilds.com</span>
          </div>
          <div class="audit-row">
            <span class="audit-key">Email verified</span
            ><span class="audit-val audit-val--ok">Yes &middot; OTP confirmed</span>
          </div>
          <div class="audit-row">
            <span class="audit-key">IP address</span><span class="audit-val">192.168.4.21</span>
          </div>
          <div class="audit-row">
            <span class="audit-key">Timestamp</span
            ><span class="audit-val">Jun 3, 2026 &middot; 2:17 PM PST</span>
          </div>
          <div class="audit-row">
            <span class="audit-key">Device</span
            ><span class="audit-val">Chrome 124 &middot; macOS 14.4</span>
          </div>
          <div class="audit-row">
            <span class="audit-key">Agreement ID</span
            ><span class="audit-val audit-val--mono">nda-jd-rb-x9k2m</span>
          </div>
        </div>

        <div class="executed-actions">
          <button class="vm-btn flex-grow-1" style="justify-content: center">
            <i class="ti ti-download"></i> Download signed PDF
          </button>
          <button class="vm-btn flex-grow-1" style="justify-content: center">
            <i class="ti ti-mail"></i> Email me a copy
          </button>
        </div>

        <div class="account-nudge">
          <div>
            <div class="account-nudge__title">Manage your agreements on Varmodel</div>
            <div class="account-nudge__sub">
              Create a free account to store, track, and send your own agreements
            </div>
          </div>
          <button class="vm-btn vm-btn--primary" style="white-space: nowrap; font-size: 12px">
            Sign up free
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
