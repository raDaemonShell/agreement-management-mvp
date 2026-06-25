from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_agreement_emails(agreement):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    frontend_url = settings.FRONTEND_URL
    sign_link = f"{frontend_url}/sign/{agreement.id}"

    # ── Email to counterparty ──
    counterparty_email = Mail(
        from_email=settings.FROM_EMAIL,
        to_emails=agreement.contact_email,
        subject=f"You have an agreement to sign — {agreement.title}",
        html_content=f"""
        <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 24px;">

          <div style="display:flex; align-items:center; gap:10px; margin-bottom:24px;
                      padding-bottom:16px; border-bottom: 2px solid #7c3aed;">
            <div style="width:32px; height:32px; border-radius:8px; background:#7c3aed;
                        color:#ede9fe; display:flex; align-items:center; justify-content:center;
                        font-size:16px; font-weight:700; text-align:center; line-height:32px;">V</div>
            <div>
              <div style="font-size:14px; font-weight:700; color:#111;">Varmodel</div>
              <div style="font-size:11px; color:#9e9e9e;">Secure agreement platform</div>
            </div>
          </div>

          <h2 style="color:#7c3aed; font-size:18px; margin-bottom:8px;">
            Agreement Ready to Sign
          </h2>

          <p style="color:#424242; font-size:14px; line-height:1.6; margin-bottom:16px;">
            Hi <strong>{agreement.contact_name}</strong>,<br><br>
            <strong>{agreement.initiator_name}</strong> from
            <strong>{agreement.initiator_company}</strong>
            has sent you an agreement to review and sign:
          </p>

          <div style="background:#ede9fe; border-left:3px solid #7c3aed; padding:12px 16px;
                      border-radius:0 8px 8px 0; margin-bottom:24px;">
            <div style="font-size:13px; font-weight:600; color:#3c3489;">
              {agreement.title}
            </div>
            <div style="font-size:12px; color:#5b21b6; margin-top:4px;">
              {agreement.agreement_type} &middot;
              {agreement.start_date} – {agreement.end_date} &middot;
              {agreement.governing_law} law
            </div>
          </div>

          <div style="text-align:center; margin-bottom:24px;">
            <a href="{sign_link}"
               style="background:#7c3aed; color:white; padding:14px 28px;
                      border-radius:8px; text-decoration:none; font-weight:600;
                      font-size:14px; display:inline-block;">
              Review &amp; Sign Agreement
            </a>
          </div>

          <div style="background:#f5f5f5; border-radius:8px; padding:12px 16px;
                      margin-bottom:16px;">
            <div style="font-size:11px; color:#757575; margin-bottom:4px;">
              Or copy this link:
            </div>
            <div style="font-size:11px; color:#424242; word-break:break-all;">
              {sign_link}
            </div>
          </div>

          <p style="font-size:11px; color:#9e9e9e; line-height:1.6;">
            This link expires in <strong>{agreement.link_expiration_days} days</strong>.
            No Varmodel account is required to review or sign.
          </p>

          <hr style="border:none; border-top:1px solid #e0e0e0; margin:20px 0;">
          <p style="font-size:10px; color:#bdbdbd; text-align:center;">
            Sent via Varmodel &middot; Secure signing portal &middot;
            Varmodel is not a law firm. This is not legal advice.
          </p>
        </div>
        """
    )

    # ── Email to initiator ──
    initiator_html = f"""
        <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 24px;">

          <div style="display:flex; align-items:center; gap:10px; margin-bottom:24px;
                      padding-bottom:16px; border-bottom: 2px solid #7c3aed;">
            <div style="width:32px; height:32px; border-radius:8px; background:#7c3aed;
                        color:#ede9fe; font-size:16px; font-weight:700; text-align:center;
                        line-height:32px;">V</div>
            <div>
              <div style="font-size:14px; font-weight:700; color:#111;">Varmodel</div>
              <div style="font-size:11px; color:#9e9e9e;">Secure agreement platform</div>
            </div>
          </div>

          <h2 style="color:#7c3aed; font-size:18px; margin-bottom:8px;">
            Agreement Sent Successfully
          </h2>

          <p style="color:#424242; font-size:14px; line-height:1.6; margin-bottom:16px;">
            Hi <strong>{agreement.initiator_name}</strong>,<br><br>
            Your agreement has been sent to
            <strong>{agreement.contact_name}</strong>
            at <strong>{agreement.contact_email}</strong> for signature.
          </p>

          <div style="background:#eaf3de; border-left:3px solid #97c459; padding:12px 16px;
                      border-radius:0 8px 8px 0; margin-bottom:24px;">
            <div style="font-size:13px; font-weight:600; color:#27500a;">
              {agreement.title}
            </div>
            <div style="font-size:12px; color:#27500a; margin-top:4px;">
              Awaiting signature from {agreement.contact_name}
            </div>
          </div>

          <p style="font-size:12px; color:#757575; line-height:1.6;">
            You'll receive another email once they've signed.
            The signing link expires in <strong>{agreement.link_expiration_days} days</strong>.
          </p>

          <hr style="border:none; border-top:1px solid #e0e0e0; margin:20px 0;">
          <p style="font-size:10px; color:#bdbdbd; text-align:center;">
            Sent via Varmodel &middot; Secure signing portal
          </p>
        </div>
    """

    # Only send to initiator if email exists
    if agreement.initiator_email:
        initiator_mail = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=agreement.initiator_email,
            subject=f"Agreement sent — awaiting signature from {agreement.contact_name}",
            html_content=initiator_html
        )
        sg.send(initiator_mail)

    sg.send(counterparty_email)