from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=12)
    lastname=models.CharField(max_length=5)
    age=models.IntegerField()
    salary=models.IntegerField()
    profilePictures=models.ImageField(upload_to='pics')

class details(models.Model):
    package_no = models.IntegerField()
    destination_place = models.CharField(max_length=15)
    no_of_days = models.IntegerField()
    stay_charge = models.IntegerField()
    food_charge = models.IntegerField()
    car_charge = models.IntegerField()
    airlines_charge = models.IntegerField()

class package(models.Model):
    #username = models.CharField(max_length=10)
    #password = models.CharField(max_length=10)
    place = models.CharField(max_length=12)
    wish_to_stay = models.CharField(max_length=3)
    no_of_days = models.IntegerField()
    no_of_adults = models.IntegerField()
    no_of_childrens = models.IntegerField()
    no_of_rooms = models.IntegerField()
    want_for_meal = models.CharField(max_length=3)
    mode_of_travel_car_flight = models.CharField(max_length=6, null=True)
    departure_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=20, null=True)


