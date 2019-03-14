from django.conf import settings
from django.db import models
from django.utils import timezone

class Businesstrip(models.Model):
    objects = models.Manager()
    travel_date = models.DateField(default=timezone.now)
    departure = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    #round_trip = models.BooleanField(default=False)

    CUSTOMER_MEETING = 'CM'
    SUPPLIER_MEETING = 'SM'
    OTHER_MEETING = 'OM'
    INTERNAL_MEETING = 'IM'
    OFFICE_DAY = 'OD'
    TRADE_FAIR = 'TF'    
    REASON_CHOICES = (
        (CUSTOMER_MEETING, 'Customer meeting'),
        (SUPPLIER_MEETING, 'Supplier meeting'),
        (OTHER_MEETING, 'Other meeting'),
        (INTERNAL_MEETING, 'Internal meeting'),
        (OFFICE_DAY, 'Office day'),
        (TRADE_FAIR, 'Trade fair'),
    )
    
    reason = models.CharField(max_length=2, choices=REASON_CHOICES,
    default=CUSTOMER_MEETING)
      
    company = models.ManyToManyField("Businesspartner", blank = True)
    total_km = models.IntegerField()
    km_allowance_eur = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    #compensation_applied = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.travel_date} / {self.destination} ({self.reason})'


class Businesspartner(models.Model):
    objects = models.Manager()
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name