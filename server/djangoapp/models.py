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
               "Type: " + self.type + ", " 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
