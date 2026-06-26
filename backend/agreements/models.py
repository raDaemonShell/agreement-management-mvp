from django.db import models
import uuid


class Partner(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    company_name = models.CharField(max_length=100)

    industry = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    avatar = models.CharField(max_length=5)

    background = models.CharField(max_length=20)

    color = models.CharField(max_length=20)

class Agreement(models.Model):

    STATUS_CHOICES = [
        ('DRAFT','Draft'),
        ('SENT','Awaiting Signature'),
        ('SIGNED','Signed')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)

    # Initiator
    initiator_name = models.CharField(max_length=100)
    initiator_title = models.CharField(max_length=100)
    initiator_company = models.CharField(max_length=200, blank=True) 
    initiator_location = models.CharField(max_length=200, blank=True) 
    initiator_email = models.EmailField(blank=True)                   
    initiator_phone = models.CharField(max_length=30, blank=True)    

    # Contact (counterparty)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=30, blank=True)
    counterparty_signature = models.CharField(max_length=200, blank=True)
    counterparty_signed_at = models.DateTimeField(null=True, blank=True)

    agreement_type = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    intellectual_property = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    governing_law = models.CharField(max_length=100)
    link_expiration_days = models.IntegerField(default=7)

    # Preview sections
    section_1 = models.TextField(blank=True)
    section_2 = models.TextField(blank=True)
    section_3 = models.TextField(blank=True)
    section_4 = models.TextField(blank=True)
    section_5 = models.TextField(blank=True)
    section_6 = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )
    initiator_signed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # OTP email
    otp_code = models.CharField(max_length=6, blank=True)
    otp_expires_at = models.DateTimeField(null=True, blank=True)