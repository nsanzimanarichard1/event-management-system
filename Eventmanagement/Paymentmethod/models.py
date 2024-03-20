from django.db import models
from Participant.models import Participant
from Event.models import Event
# Create your models here.

PAYMENT_STATUS = (
    ('PAID', 'Paid'),
    ('PENDING', 'Pending'),
    ('FAILED', 'Failed'),
)


class Payment(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #amount_paid = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=70)
    #payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200)
    payment_status = models.CharField(
        max_length=10, choices=PAYMENT_STATUS, default='PENDING'
    )
    def __str__(self):
        return self.payment_status