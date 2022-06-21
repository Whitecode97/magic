from django.db import models

# Create your models here.

class Booking (models.Model):
    customerName = models.CharField(max_length=10000, blank=True)
    customerEmail = models.EmailField(blank=True)
    custOccupation = models.CharField(max_length=10000, blank=True)
    rNumber =models.CharField(max_length=10, blank=True, null=False,
   default=00000)
    numberOfNight = models.IntegerField(null=True, blank=True, default=000)
    checkIn = models.DateField( blank=True)
    checkOut = models.DateField(blank=True)
    bill = models.CharField(max_length=10000, blank=True)
    
    def __str__(self):
            return self.customerName