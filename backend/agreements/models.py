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

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        max_length=200
    )

    partner = models.ForeignKey(
        Partner,
        on_delete=models.SET_NULL,
        null=True
    )

    contact_name = models.CharField(
        max_length=100
    )

    contact_title = models.CharField(
        max_length=100
    )

    contact_email = models.EmailField()

    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )

    initiator_name = models.CharField(
        max_length=100
    )

    initiator_title = models.CharField(
        max_length=100
    )

    agreement_type = models.CharField(
        max_length=100
    )

    purpose = models.CharField(
        max_length=100
    )

    intellectual_property = models.CharField(
        max_length=100
    )

    start_date = models.DateField()

    end_date = models.DateField()

    governing_law = models.CharField(
        max_length=100
    )

    link_expiration_days = models.IntegerField(
        default=7
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    