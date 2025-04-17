from django.db import models
from jayaapp.users.models import User


class Transaction(models.Model):
    CURRENCY_CHOICES = (
        ("BRL", "Brazilian Real"),
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("JPY", "Japanese Yen"),
    )

    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    origin_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    origin_value = models.DecimalField(max_digits=14, decimal_places=2)
    destination_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=6)
    destination_value = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.origin_currency} to {self.destination_currency}"
