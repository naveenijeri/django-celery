from django.db import models

# Create your models here.
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE) #
    name = models.CharField(max_length=100)

#Note:
#on_delete=models.CASCADE:You have 2 models i.e., Car and Company. You delete the company, you also delete the cars made by that company.
#on_delete=models.PROTECT:You have 2 models. Car and Company. You delete the company, Django says, Hold up. Can't do it ... So everything remains.

# null
# If True, Django will store empty values as NULL in the database. Default is False.
# blank
# If True, the field is allowed to be blank. Default is False.

# Note that this is different than null. null is purely database-related, whereas blank is validation-related. If a field has blank=True, form validation will allow entry of an empty value. If a field has blank=False, the field will be required.

#####PRIMARY KEY################
from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

#######RELATIONSHIP#############
#many-to-one, many-to-many and one-to-one

######Many-to-one relationships######
#ForeignKey requires a positional argument: the class to which the model is related.
#For example, if a Car model has a Manufacturer – that is, a Manufacturer makes multiple cars but each Car only has one Manufacturer – use the following definitions:

# from django.db import models

# class Manufacturer(models.Model):
#    company_name = models.CharField(max_length=255)

# class Car(models.Model):
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

######Many-to-many relationships##########
#one intermediatery table is created with the reference ids

####one-to-one relationships###

##############################################################################
####Model methods#######
class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

######Overriding predefined model methods#####
#In particular you’ll often want to change the way save() and delete() work.

class Blog(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.name == "Nikil":
            return "Nikhil dosen't have own blog"
        super().save(*args, **kwargs)

#######Model inheritance#######
#1)Abstract Base Classes
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True)

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

#2)Multi-table inheritance
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)