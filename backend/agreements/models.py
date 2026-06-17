import uuid

from django.db import models


class AgreementStatus(models.TextChoices):

    DRAFT = "DRAFT", "Draft"

    SENT = "SENT", "Awaiting Signature"

    SIGNED = "SIGNED", "Signed"

    EXPIRED = "EXPIRED", "Expired"

    CANCELLED = "CANCELLED", "Cancelled"


class AgreementType(models.TextChoices):

    NDA = "NDA", "NDA"

    MSA = "MSA", "MSA"

    TEAMING = "TEAMING", "Teaming Agreement"

    SUBCONTRACTOR = "SUBCONTRACTOR", "Subcontractor Agreement"

    LICENSING = "LICENSING", "Licensing Agreement"

    LOI = "LOI", "Letter Of Intent"

    WORK_ORDER = "WORK_ORDER", "Work Order"


class Agreement(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        max_length=255
    )

    agreement_type = models.CharField(
        max_length=30,
        choices=AgreementType.choices
    )

    status = models.CharField(
        max_length=20,
        choices=AgreementStatus.choices,
        default=AgreementStatus.DRAFT
    )

    initiator_name = models.CharField(
        max_length=255
    )

    initiator_title = models.CharField(
        max_length=255
    )

    counterparty_company = models.CharField(
        max_length=255
    )

    counterparty_contact_name = models.CharField(
        max_length=255
    )

    counterparty_contact_title = models.CharField(
        max_length=255
    )

    counterparty_email = models.EmailField()

    start_date = models.DateField()

    end_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title