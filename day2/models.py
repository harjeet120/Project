from django.db import models

# Create your models here.
class booking(models.Model):
    username = models.CharField(max_length=10)
    no_of_adults = models.IntegerField()
    no_of_childrens = models.IntegerField()
    no_of_rooms = models.IntegerField()
    want_for_meal = models.CharField(max_length=20)
    mode_of_travel_car_flight = models.CharField(max_length=6)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=20)

class packagedetails(models.Model):
    PackageID = models.IntegerField()
    DestinationPlaces = models.CharField(max_length=40)
    NumberofDays = models.CharField(max_length=3)
    StayCharge = models.CharField(max_length=12)
    FoodCharge = models.CharField(max_length=12)
    CarCharge = models.CharField(max_length=12)
    FlightCharge = models.CharField(max_length=12)
    PlacestoVisit = models.CharField(max_length=100)


