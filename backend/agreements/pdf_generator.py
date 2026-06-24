import os
from django.conf import settings
from django.utils import timezone
from weasyprint import HTML, CSS


def format_initiator_signed_meta(agreement):
    signed_at = agreement.initiator_signed_at or agreement.created_at
    local = timezone.localtime(signed_at) if timezone.is_aware(signed_at) else signed_at
    date_str = local.strftime('%b %d, %Y')
    time_str = local.strftime('%I:%M %p')
    tz = local.strftime('%Z') or 'UTC'
    return f"{agreement.initiator_title} &middot; {date_str} &middot; {time_str} {tz}"


def generate_agreement_pdf(agreement):
    pdf_dir = os.path.join(settings.MEDIA_ROOT, 'agreements')
    os.makedirs(pdf_dir, exist_ok=True)
    filepath = os.path.join(pdf_dir, f"{agreement.id}.pdf")

    partner_name = agreement.partner.company_name if agreement.partner else 'N/A'
    partner_loc = agreement.partner.location if agreement.partner else ''

    agreement_type_map = {
        'NDA': 'Non-Disclosure Agreement',
        'MSA': 'Master Services Agreement',
        'TEAMING': 'Teaming Agreement',
        'SUBCONTRACTOR': 'Subcontractor Agreement',
        'LOI': 'Letter of Intent',
    }
    agreement_type_title = agreement_type_map.get(
        agreement.agreement_type, agreement.agreement_type
    )
    initiator_signed_meta = format_initiator_signed_meta(agreement)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

      * {{ box-sizing: border-box; margin: 0; padding: 0; }}

      body {{
        font-family: Roboto, sans-serif;
        font-size: 10px;
        color: #212121;
        padding: 40px;
        line-height: 1.5;
      }}

      /* Title */
      .pdf-title {{
        font-size: 16px;
        font-weight: 700;
        text-align: center;
        color: #111111;
        margin-bottom: 4px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
      }}
      .pdf-subtitle {{
        font-size: 9px;
        text-align: center;
        color: #9e9e9e;
        margin-bottom: 16px;
      }}

      hr {{
        border: none;
        border-top: 1px solid #e0e0e0;
        margin-bottom: 16px;
      }}

      /* Parties */
      .pdf-parties {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 20px;
      }}
      .pdf-party {{
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 10px 12px;
        background: #fafafa;
      }}
      .pdf-party__badge {{
        font-size: 8px;
        font-weight: 700;
        color: #9e9e9e;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 3px;
      }}
      .pdf-party__name {{
        font-size: 12px;
        font-weight: 700;
        color: #111111;
        margin-bottom: 2px;
      }}
      .pdf-party__loc {{
        font-size: 9px;
        color: #9e9e9e;
        margin-bottom: 6px;
      }}
      .pdf-party__contact {{
        margin-top: 6px;
        padding-top: 6px;
        border-top: 1px solid #e8e8e8;
      }}
      .pdf-party__contact-badge {{
        font-size: 8px;
        font-weight: 700;
        color: #9e9e9e;
        text-transform: uppercase;
        margin-bottom: 2px;
      }}
      .pdf-party__contact-name {{
        font-size: 10px;
        font-weight: 500;
        color: #212121;
      }}
      .pdf-party__contact-title {{
        font-size: 9px;
        color: #757575;
      }}

      /* Sections */
      .pdf-sec {{ margin-bottom: 12px; }}
      .pdf-sec__title {{
        font-size: 9px;
        font-weight: 700;
        color: #212121;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
        padding-bottom: 3px;
        border-bottom: 0.5px solid #e0e0e0;
      }}
      .pdf-sec__body {{
        font-size: 10px;
        color: #757575;
        line-height: 1.6;
      }}

      /* AI block */
      .pdf-ai-block {{
        background: #ede9fe;
        border-left: 2px solid #7c3aed;
        padding: 10px 12px;
        border-radius: 0 6px 6px 0;
        margin-bottom: 20px;
      }}
      .pdf-ai-block__label {{
        font-size: 8px;
        font-weight: 700;
        color: #7c3aed;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 4px;
      }}
      .pdf-ai-block__body {{
        font-size: 10px;
        color: #3c3489;
        line-height: 1.6;
      }}

      /* Signature row */
      .pdf-sig-row {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 16px;
      }}
      .pdf-sig-box {{
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 10px 12px;
      }}
      .pdf-sig-box__label {{
        font-size: 9px;
        color: #9e9e9e;
        margin-bottom: 6px;
      }}
      .pdf-sig-box__name {{
        font-size: 14px;
        font-style: italic;
        color: #212121;
        font-family: Georgia, serif;
        margin-bottom: 4px;
        padding-bottom: 6px;
        border-bottom: 1px solid #e0e0e0;
      }}
      .pdf-sig-box__blank {{
        height: 24px;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 4px;
      }}
      .pdf-sig-box__meta {{
        font-size: 8px;
        color: #9e9e9e;
      }}

      /* Disclaimer */
      .pdf-disclaimer {{
        font-size: 8px;
        color: #9e9e9e;
        line-height: 1.5;
        border-top: 1px solid #e0e0e0;
        padding-top: 10px;
      }}

      /* Varmodel header bar */
      .pdf-header-bar {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 24px;
        padding-bottom: 12px;
        border-bottom: 2px solid #7c3aed;
      }}
      .pdf-header-bar__logo {{
        width: 28px;
        height: 28px;
        border-radius: 7px;
        background: #7c3aed;
        color: #ede9fe;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        font-weight: 700;
      }}
      .pdf-header-bar__name {{
        font-size: 14px;
        font-weight: 700;
        color: #111111;
      }}
      .pdf-header-bar__sub {{
        font-size: 10px;
        color: #9e9e9e;
      }}
      .pdf-draft-badge {{
        background: #ede9fe;
        color: #7c3aed;
        font-size: 9px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 100px;
      }}
    </style>
    </head>
    <body>

      <!-- Title -->
      <div class="pdf-title">{agreement_type_title}</div>
      <div class="pdf-subtitle">
        Generated via Varmodel &middot; Draft &middot;
        {agreement.start_date} &ndash; {agreement.end_date} &middot;
        Governed by {agreement.governing_law} law
      </div>
      <hr>

      <!-- Parties -->
      <div class="pdf-parties">
        <div class="pdf-party">
          <div class="pdf-party__badge">Disclosing Party</div>
          <div class="pdf-party__name">{agreement.initiator_company or agreement.initiator_name}</div>
          <div class="pdf-party__loc">{agreement.initiator_location or ''}</div>
          <div class="pdf-party__contact">
            <div class="pdf-party__contact-badge">Signing contact</div>
            <div class="pdf-party__contact-name">{agreement.initiator_name}</div>
            <div class="pdf-party__contact-title">{agreement.initiator_title}</div>
          </div>
        </div>
        <div class="pdf-party">
          <div class="pdf-party__badge">Receiving Party</div>
          <div class="pdf-party__name">{partner_name}</div>
          <div class="pdf-party__loc">{partner_loc}</div>
          <div class="pdf-party__contact">
          <div class="pdf-party__contact-badge">Signing contact</div>
          <div class="pdf-party__contact-name">{agreement.contact_name}</div>
          <div class="pdf-party__contact-title">{agreement.contact_title}</div>
          </div>
        </div>
      </div>

<!-- Section 1 -->
      <div class="pdf-sec">
        <div class="pdf-sec__title">1. Parties</div>
        <div class="pdf-sec__body">{agreement.section_1 or f"This {agreement_type_title} is entered into between {agreement.initiator_company or agreement.initiator_name} and {partner_name}, represented by {agreement.initiator_name} and {agreement.contact_name}."}</div>
      </div>

      <!-- Section 2 -->
      <div class="pdf-sec">
        <div class="pdf-sec__title">2. Confidential Information</div>
        <div class="pdf-sec__body">{agreement.section_2 or '"Confidential Information" means any non-public information disclosed by either Party, including trade secrets, business plans, financial data, and technical information in any form...'}</div>
      </div>

      <!-- Section 3 -->
      <div class="pdf-sec">
        <div class="pdf-sec__title">3. Obligations</div>
        <div class="pdf-sec__body">{agreement.section_3 or f"Each Party agrees to hold the other's Confidential Information in strict confidence, use it solely for the {agreement.purpose}, and not disclose to any third party without prior written consent..."}</div>
      </div>

      <!-- Section 4 -->
      <div class="pdf-sec">
        <div class="pdf-sec__title">4. Term</div>
        <div class="pdf-sec__body">{agreement.section_4 or f"This Agreement shall remain in effect from {agreement.start_date} to {agreement.end_date}, governed by {agreement.governing_law} law."}</div>
      </div>

      <!-- Section 5 -->
      <div class="pdf-sec">
        <div class="pdf-sec__title">5. Remedies</div>
        <div class="pdf-sec__body">{agreement.section_5 or "Each Party acknowledges that breach may cause irreparable harm, entitling the non-breaching Party to seek equitable relief in addition to legal remedies..."}</div>
      </div>

      <!-- Section 6 AI block -->
      <div class="pdf-ai-block">
        <div class="pdf-ai-block__label">&#10022; Section 6 — Special Provisions (AI-assisted)</div>
        <div class="pdf-ai-block__body">{agreement.section_6 or f"{partner_name} will protect {agreement.intellectual_property} throughout the duration of this agreement for {agreement.purpose} under {agreement.governing_law} law."}</div>
      </div>

      <!-- Signatures -->
      <div class="pdf-sig-row">
        <div class="pdf-sig-box">
          <div class="pdf-sig-box__label">
            Signature — {agreement.initiator_company or agreement.initiator_name}
          </div>
          <div class="pdf-sig-box__name">{agreement.initiator_name}</div>
          <div class="pdf-sig-box__meta">
            {initiator_signed_meta}
          </div>
        </div>
        <div class="pdf-sig-box">
          <div class="pdf-sig-box__label">Signature — {partner_name}</div>
          <div class="pdf-sig-box__blank"></div>
          <div class="pdf-sig-box__meta">
            {agreement.contact_name} &middot; {agreement.contact_title} &middot;
            Awaiting signature
          </div>
        </div>
      </div>

      <!-- Disclaimer -->
      <div class="pdf-disclaimer">
        &#9888; Generated as a starting point. Varmodel Inc is not a law firm and this is not
        legal advice. Consult an attorney prior to execution.
      </div>

    </body>
    </html>
    """

    HTML(string=html_content).write_pdf(filepath)
    return filepath