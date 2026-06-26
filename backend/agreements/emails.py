import random
import string
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import base64
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition


def generate_otp():
    return ''.join(random.choices(string.digits, k=6))


def send_otp_email(agreement):
    # Generate and save OTP
    otp = generate_otp()
    agreement.otp_code = otp
    agreement.otp_expires_at = timezone.now() + timedelta(minutes=15)
    agreement.save(update_fields=['otp_code', 'otp_expires_at'])

    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

    mail = Mail(
        from_email=settings.FROM_EMAIL,
        to_emails=agreement.contact_email,
        subject='Your verification code — Varmodel',
        html_content=f"""
        <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 24px;">
          <div style="margin-bottom:24px; padding-bottom:16px; border-bottom:2px solid #7c3aed;">
            <div style="font-size:14px; font-weight:700; color:#111;">Varmodel</div>
            <div style="font-size:11px; color:#9e9e9e;">Secure agreement platform</div>
          </div>

          <h2 style="color:#7c3aed; font-size:18px; margin-bottom:8px;">
            Your verification code
          </h2>

          <p style="color:#424242; font-size:14px; line-height:1.6; margin-bottom:24px;">
            Hi <strong>{agreement.contact_name}</strong>,<br><br>
            Enter this code to verify your identity before signing
            <strong>{agreement.title}</strong>.
          </p>

          <div style="text-align:center; margin-bottom:24px;">
            <div style="display:inline-block; background:#ede9fe; border:2px solid #7c3aed;
                        border-radius:12px; padding:20px 40px;">
              <div style="font-size:36px; font-weight:700; color:#7c3aed;
                          letter-spacing:12px;">{otp}</div>
            </div>
          </div>

          <p style="font-size:12px; color:#757575; line-height:1.6; text-align:center;">
            This code expires in <strong>15 minutes</strong>.<br>
            If you did not request this, please ignore this email.
          </p>

          <hr style="border:none; border-top:1px solid #e0e0e0; margin:20px 0;">
          <p style="font-size:10px; color:#bdbdbd; text-align:center;">
            Sent via Varmodel &middot; Secure signing portal
          </p>
        </div>
        """
    )

    sg.send(mail)


def send_agreement_emails(agreement):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    frontend_url = settings.FRONTEND_URL
    sign_link = f"{frontend_url}/sign/{agreement.id}"

    counterparty_email = Mail(
        from_email=settings.FROM_EMAIL,
        to_emails=agreement.contact_email,
        subject=f"You have an agreement to sign — {agreement.title}",
        html_content=f"""
        <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 24px;">
          <div style="margin-bottom:24px; padding-bottom:16px; border-bottom:2px solid #7c3aed;">
            <div style="font-size:14px; font-weight:700; color:#111;">Varmodel</div>
            <div style="font-size:11px; color:#9e9e9e;">Secure agreement platform</div>
          </div>
          <h2 style="color:#7c3aed; font-size:18px; margin-bottom:8px;">Agreement Ready to Sign</h2>
          <p style="color:#424242; font-size:14px; line-height:1.6; margin-bottom:16px;">
            Hi <strong>{agreement.contact_name}</strong>,<br><br>
            <strong>{agreement.initiator_name}</strong> from
            <strong>{agreement.initiator_company}</strong>
            has sent you an agreement to review and sign.
          </p>
          <div style="background:#ede9fe; border-left:3px solid #7c3aed; padding:12px 16px;
                      border-radius:0 8px 8px 0; margin-bottom:24px;">
            <div style="font-size:13px; font-weight:600; color:#3c3489;">{agreement.title}</div>
            <div style="font-size:12px; color:#5b21b6; margin-top:4px;">
              {agreement.agreement_type} &middot; {agreement.start_date} – {agreement.end_date}
            </div>
          </div>
          <div style="text-align:center; margin-bottom:24px;">
            <a href="{sign_link}"
               style="background:#7c3aed; color:white; padding:14px 28px; border-radius:8px;
                      text-decoration:none; font-weight:600; font-size:14px; display:inline-block;">
              Review &amp; Sign Agreement
            </a>
          </div>
          <p style="font-size:11px; color:#9e9e9e;">
            This link expires in <strong>{agreement.link_expiration_days} days</strong>.
          </p>
          <hr style="border:none; border-top:1px solid #e0e0e0; margin:20px 0;">
          <p style="font-size:10px; color:#bdbdbd; text-align:center;">
            Sent via Varmodel &middot; Secure signing portal
          </p>
        </div>
        """
    )

    if agreement.initiator_email:
        initiator_mail = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=agreement.initiator_email,
            subject=f"Agreement sent — awaiting signature from {agreement.contact_name}",
            html_content=f"""
            <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 24px;">
              <div style="margin-bottom:24px; padding-bottom:16px; border-bottom:2px solid #7c3aed;">
                <div style="font-size:14px; font-weight:700; color:#111;">Varmodel</div>
              </div>
              <h2 style="color:#7c3aed;">Agreement Sent Successfully</h2>
              <p style="color:#424242; font-size:14px; line-height:1.6;">
                Hi <strong>{agreement.initiator_name}</strong>,<br><br>
                Your agreement has been sent to <strong>{agreement.contact_name}</strong>
                at <strong>{agreement.contact_email}</strong> for signature.
              </p>
              <p style="font-size:12px; color:#757575;">
                You'll receive another email once they've signed.
              </p>
              <hr style="border:none; border-top:1px solid #e0e0e0; margin:20px 0;">
              <p style="font-size:10px; color:#bdbdbd; text-align:center;">
                Sent via Varmodel
              </p>
            </div>
            """
        )
        sg.send(initiator_mail)

    sg.send(counterparty_email)

def send_signed_emails(agreement):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

    signed_date = agreement.counterparty_signed_at.strftime('%b %d, %Y') if agreement.counterparty_signed_at else 'Today'

    html = f"""
    <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 24px;">
      <div style="margin-bottom:24px; padding-bottom:16px; border-bottom:2px solid #7c3aed;">
        <div style="font-size:14px; font-weight:700; color:#111;">Varmodel</div>
        <div style="font-size:11px; color:#9e9e9e;">Secure agreement platform</div>
      </div>

      <div style="text-align:center; margin-bottom:24px;">
        <div style="width:52px; height:52px; border-radius:50%; background:#eaf3de;
                    border:2px solid #97c459; margin:0 auto 12px; display:flex;
                    align-items:center; justify-content:center; font-size:24px;">✓</div>
        <h2 style="color:#27500a; font-size:18px; margin:0;">Agreement Fully Executed</h2>
      </div>

      <p style="color:#424242; font-size:14px; line-height:1.6; margin-bottom:16px;">
        Both parties have signed <strong>{agreement.title}</strong>.
      </p>

      <div style="background:#eaf3de; border-left:3px solid #97c459; padding:12px 16px;
                  border-radius:0 8px 8px 0; margin-bottom:24px;">
        <div style="font-size:12px; color:#27500a;">
          <strong>{agreement.initiator_name}</strong> ({agreement.initiator_company}) — Signed<br>
          <strong>{agreement.contact_name}</strong> ({agreement.partner.company_name if agreement.partner else ''}) — Signed {signed_date}
        </div>
      </div>

      <hr style="border:none; border-top:1px solid #e0e0e0; margin:20px 0;">
      <p style="font-size:10px; color:#bdbdbd; text-align:center;">
        Sent via Varmodel &middot; Secure signing portal
      </p>
    </div>
    """

    recipients = [agreement.contact_email]
    if agreement.initiator_email:
        recipients.append(agreement.initiator_email)

    for email in recipients:
        mail = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=email,
            subject=f"Agreement fully executed — {agreement.title}",
            html_content=html
        )
        sg.send(mail)

def send_pdf_copy_email(agreement, to_email, pdf_path):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

    # Read and encode PDF
    with open(pdf_path, 'rb') as f:
        pdf_data = base64.b64encode(f.read()).decode()

    filename = f"{agreement.title}.pdf"

    mail = Mail(
        from_email=settings.FROM_EMAIL,
        to_emails=to_email,
        subject=f"Your signed agreement — {agreement.title}",
        html_content=f"""
        <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 24px;">
          <div style="margin-bottom:24px; padding-bottom:16px; border-bottom:2px solid #7c3aed;">
            <div style="font-size:14px; font-weight:700; color:#111;">Varmodel</div>
            <div style="font-size:11px; color:#9e9e9e;">Secure agreement platform</div>
          </div>

          <div style="text-align:center; margin-bottom:24px;">
            <div style="width:52px; height:52px; border-radius:50%; background:#eaf3de;
                        border:2px solid #97c459; margin:0 auto 12px; line-height:52px;
                        font-size:24px; color:#27500a; text-align:center;">✓</div>
            <h2 style="color:#27500a; font-size:18px; margin:0;">
              Signed Agreement — Your Copy
            </h2>
          </div>

          <p style="color:#424242; font-size:14px; line-height:1.6; margin-bottom:16px;">
            Hi <strong>{agreement.contact_name}</strong>,<br><br>
            Please find attached your fully executed copy of
            <strong>{agreement.title}</strong>.
          </p>

          <div style="background:#f5f5f5; border-radius:8px; padding:12px 16px;
                      margin-bottom:24px;">
            <div style="font-size:12px; color:#424242; line-height:1.8;">
              <strong>Agreement:</strong> {agreement.title}<br>
              <strong>Type:</strong> {agreement.agreement_type}<br>
              <strong>Parties:</strong> {agreement.initiator_company} &amp; {agreement.partner.company_name if agreement.partner else agreement.contact_name}<br>
              <strong>Period:</strong> {agreement.start_date} – {agreement.end_date}<br>
              <strong>Governing law:</strong> {agreement.governing_law}
            </div>
          </div>

          <p style="font-size:12px; color:#757575; line-height:1.6;">
            Both parties have signed this agreement. Please keep this copy for your records.
          </p>

          <hr style="border:none; border-top:1px solid #e0e0e0; margin:20px 0;">
          <p style="font-size:10px; color:#bdbdbd; text-align:center;">
            Sent via Varmodel &middot; Secure signing portal &middot;
            Varmodel is not a law firm. This is not legal advice.
          </p>
        </div>
        """
    )

    # Attach PDF
    attachment = Attachment(
        FileContent(pdf_data),
        FileName(filename),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    mail.attachment = attachment

    sg.send(mail)