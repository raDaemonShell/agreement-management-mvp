<template>
  <div class="wizard-screen" id="ws7">
    <div class="done-screen">
      <div class="done-screen__circle">
        <i class="ti ti-check" style="font-size: 22px; color: #27500a"></i>
      </div>
      <div class="done-screen__title">Agreement executed</div>
      <div class="done-screen__sub">
        Signed PDFs sent to john@techventures.com and maria@riverabuilds.com
      </div>
      <div class="done-parties">
        <div class="done-party">
          <div class="done-party__name">John Doe</div>
          <div class="done-party__co">TechVentures Inc</div>
          <div class="done-party__status"><i class="ti ti-check"></i> Signed Jun 1</div>
        </div>
        <div class="done-party">
          <div class="done-party__name">Maria Rivera</div>
          <div class="done-party__co">Rivera Builds LLC</div>
          <div class="done-party__status"><i class="ti ti-check"></i> Signed Jun 3</div>
        </div>
      </div>
      <div class="d-flex justify-center gap-3">
        <button class="vm-btn"><i class="ti ti-download"></i> Download PDF</button
        ><button class="vm-btn" onclick="showPage('home')">
          <i class="ti ti-folder"></i> View in agreements
        </button>
      </div>
    </div>
  </div>
</template>
