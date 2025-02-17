from django.db import models
from django.utils.timezone import now

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(null=False, max_length=100, default='')
    def __str__(self):
        return "Name: " + self.name + ", " + \
               "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
class CarModel(models.Model):
    carMake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealerId = models.IntegerField()
    name = models.CharField(null=False, max_length=30, default='')
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    MODEL_CHOICES = [
        (SEDAN, 'SEDAN'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    type = models.CharField(
        null=False,
        max_length=20,
        choices=MODEL_CHOICES,
        default=SEDAN
    )
    year = models.DateField(null=True)
    def __str__(self):
        return "Dealer Id: " + str(self.dealerId) + ", " + \
               "Name: " + self.name + ", " + \
               "Year: " + str(self.year.year) + ", " + \
               "Type: " + self.type + ", " 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name + ", " + \
                "Address" + self.address + ", " + \
                "City" + self.city + ", " + \
                "Id" + self.id + ", " + \
                "Lat" + self.lat + ", " + \
                "Zip" + self.zip 

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        # Dealer dealership
        self.dealership = dealership
        # Dealer name
        self.name = name
        # Dealer purchase
        self.purchase = purchase
        # Dealer review
        self.review = review
        # Location purchase_date
        self.purchase_date = purchase_date
        # Location car_make
        self.car_make = car_make
        # Dealer car_model
        self.car_model = car_model
        # Dealer car_year
        self.car_year = car_year
        # Dealer sentiment
        self.sentiment = sentiment
        # Dealer id
        self.id = id

    def __str__(self):
         return "Dealership: " + self.dealership + ", " + \
                "Name" + self.name + ", " + \
                "Purchase" + self.purchase + ", " + \
                "Review" + self.review + ", " + \
                "Purchase Date" + self.purchase_date + ", " + \
                "car_make" + self.car_make + ", " + \
                "car_year" + self.car_year + ", " + \
                "sentiment" + self.sentiment + ", " + \
                "id" + self.id