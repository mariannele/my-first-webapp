from django.conf import settings
from django.db import models
from django.utils import timezone

class Businesstrip(models.Model):
    #objects = models.Manager()
    travel_date = models.DateField(default=timezone.now)
    departure = models.CharField(max_length=20)
    destination = models.ManyToManyField("Traveldestination", blank = True)
    company = models.ManyToManyField("Businesspartner", blank = True)

    CUSTOMER_MEETING = 'CUSTOMER_MEETING'
    SUPPLIER_MEETING = 'SUPPLIER_MEETING'
    OTHER_MEETING = 'OTHER_MEETING'
    INTERNAL_MEETING = 'INTERNAL_MEETING'
    OFFICE_DAY = 'OFFICE_DAY'
    TRADE_FAIR = 'TRADE_FAIR'    
    REASON_CHOICES = (
        (CUSTOMER_MEETING, 'Customer meeting'),
        (SUPPLIER_MEETING, 'Supplier meeting'),
        (OTHER_MEETING, 'Other meeting'),
        (INTERNAL_MEETING, 'Internal meeting'),
        (OFFICE_DAY, 'Office day'),
        (TRADE_FAIR, 'Trade fair'),
    )
    
    reason = models.CharField(max_length=20, choices=REASON_CHOICES,
    default=CUSTOMER_MEETING)

    agenda = models.CharField(max_length=200, blank=True, null=True)
      
    TRIPTYPE_CHOICES = (
        ('ONE_WAY', 'One way'),
        ('RETURN', 'Return trip')
    )

    return_trip = models.CharField(max_length=20, choices=TRIPTYPE_CHOICES, 
    default="RETURN")

    total_km = models.IntegerField()
    km_allowance_eur = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.travel_date} / {self.destination} ({self.reason})'


class Businesspartner(models.Model):
    #objects = models.Manager()
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Traveldestination(models.Model):
    city_name = models.CharField(max_length=25)

    def __str__(self):
        return self.city_name