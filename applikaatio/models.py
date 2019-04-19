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
    city_name = models.CharField(max_length=50, default=None)

    CITY_HOLIDAY = 'CITY_HOLIDAY'
    BEACH_HOLIDAY = 'BEACH_HOLIDAY'
    ACTIVITY_VACATION = 'ACTIVITY_VACATION'
    FAMILY_HOLIDAY = 'FAMILY_HOLIDAY'
    BUSINESS_TRIP = 'BUSINESS_TRIP'     
    TRIPTYPE_CHOICES = (
        (CITY_HOLIDAY, 'City holiday'),
        (BEACH_HOLIDAY, 'Beach holiday'),
        (ACTIVITY_VACATION, 'Activity vacation'),
        (FAMILY_HOLIDAY, 'Family holiday'),
        (BUSINESS_TRIP, 'Business trip'),        
    )
    
    trip_type = models.CharField(max_length=20, choices=TRIPTYPE_CHOICES,
    default=CITY_HOLIDAY)

    ACCOMMODATION_CHOICES = (
    ('HOTEL', 'Hotel'),
    ('HOSTEL', 'Hostel'),
    ('RENTAL_APPARTMENT', 'Rental appartment'),
    ('RENTAL_HOUSE', 'Rental house'),
    ('BED_N_BREAKFAST', 'Bed and breakfast'),
    ('HOLIDAY_VILLA', 'Holiday villa'),
)

    accommodation = models.CharField(max_length=20, choices=ACCOMMODATION_CHOICES, 
    default="HOTEL")

    content = models.TextField(default=None)

    def __str__(self):
        return self.city_name

    class Meta:
        ordering = ('travel_date',)


"""class Businesspartner(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name"""

"""class Traveldestination(models.Model):
    city_name = models.CharField(max_length=50, blank=True, null=True)
    #models.ForeignKey('Businesstrip', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name"""