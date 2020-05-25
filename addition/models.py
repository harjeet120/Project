from django.db import models

# Create your models here.

class bookings(models.Model):

    no_of_adults = models.IntegerField()
    no_of_childrens = models.IntegerField()
    no_of_rooms = models.IntegerField()
    want_for_meal = models.CharField(max_length=20)
    mode_of_travel_car_flight = models.CharField(max_length=6)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=20)