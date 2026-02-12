import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Therapist(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    avatar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Service(BaseModel):
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Location(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceAddon(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class CommissionRule(BaseModel):
    COMMISSION_TYPE_CHOICES = (
        ("percentage", "Percentage"),
        ("fixed", "Fixed"),
    )

    therapist = models.ForeignKey(
        Therapist, on_delete=models.CASCADE, related_name="commission_rules"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="commission_rules"
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="commission_rules"
    )

    commission_type = models.CharField(max_length=20, choices=COMMISSION_TYPE_CHOICES)
    commission_value = models.DecimalField(max_digits=10, decimal_places=2)
    vat_included = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.therapist} - {self.service}"


class CommissionEntry(models.Model):
    COMMISSION_TYPE_CHOICES = (
        ("percentage", "Percentage"),
        ("fixed", "Fixed"),
    )

    STATUS_CHOICES = (
        ("paid", "Paid"),
        ("unpaid", "Unpaid"),
    )

    INVOICE_STATUS_CHOICES = (
        ("paid", "Paid"),
        ("unpaid", "Unpaid"),
    )

    PAYMENT_METHOD_CHOICES = (
        ("card", "Card"),
        ("cash", "Cash"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appointment_id = models.CharField(max_length=255)
    date = models.DateField()
    client_name = models.CharField(max_length=255, blank=True, null=True)

    therapist = models.ForeignKey(
        Therapist, on_delete=models.SET_NULL, null=True, blank=True, related_name="commission_entries"
    )
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True, related_name="commission_entries"
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="commission_entries"
    )

    add_ons = models.JSONField(default=list, blank=True)

    service_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    add_ons_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    commission_type = models.CharField(max_length=20, choices=COMMISSION_TYPE_CHOICES)
    commission_value = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="unpaid")
    invoice_status = models.CharField(max_length=20, choices=INVOICE_STATUS_CHOICES, default="unpaid")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, blank=True, null=True)
    cash_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    card_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appointment_id} - {self.status}"

