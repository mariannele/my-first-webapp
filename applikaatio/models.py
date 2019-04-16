from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Businesstrip(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    #if user is deleted, his posts are deleted, but if post is deleted, the user is not.
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    travel_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200, default=None)
    travel_destination = models.ManyToManyField("Traveldestination", default=None)
    company = models.ManyToManyField("Businesspartner", default=None)

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

    content = models.TextField(blank = True)
      
    TRIPTYPE_CHOICES = (
        ('ONE_WAY', 'One way'),
        ('RETURN', 'Return trip')
    )

    return_trip = models.CharField(max_length=20, choices=TRIPTYPE_CHOICES, 
    default="RETURN")

    def __str__(self):
        return f'{self.travel_date} / ({self.title})'

    class Meta:
        ordering = ('travel_date',)


class Businesspartner(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Traveldestination(models.Model):
    city_name = models.CharField(max_length=50, blank=True, null=True)
    #models.ForeignKey('Businesstrip', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name