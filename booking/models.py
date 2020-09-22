from django.db import models
from django.conf import settings
from django.contrib import admin
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
#date must bee after today, cant have two sessions i same session in one day
# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    address= models.CharField(max_length=500)
    room_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

#parse date time >time
class Event(models.Model):
    HOURS=[
    ("0 am","0 am"),
    ("1 am","1 am"),
    ("2 am","2 am"),
    ("3 am","3 am"),
    ("4 am","4 am"),
    ("5 am","5 am"),
    ("6 am","6 am"),
    ("7 am","7 am"),
    ("8 am","8 am"),
    ("9 am","9 am"),
    ("10 am","10 am"),
    ("11 am","11 am"),
    ("1 pm","1 pm"),
    ("2 pm","2 pm"),
    ("3 pm","3 pm"),
    ("4 pm","4 pm"),
    ("5 pm","5 pm"),
    ("6 pm","6 pm"),
    ("7 pm","7 pm"),
    ("8 pm","8 pm"),
    ("9 pm","9 pm"),
    ("10 pm","10 pm"),
    ("11 pm","11 pm"),
     ]
    
    location=models.ForeignKey(to=Location,  on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    tag_line=models.CharField(max_length=500)
    title=models.CharField(max_length=100)
    start_date=models.DateField(validators=[MinValueValidator(limit_value=date.today)])
    start_hour=models.CharField(max_length=5,choices=HOURS,blank=True)
    start_minutes=models.PositiveIntegerField(validators=[MaxValueValidator(59)])
    end_date=models.DateField(validators=[MinValueValidator(limit_value=date.today)])
    end_hour=models.CharField(max_length=5,choices=HOURS,blank=True)
    end_minutes=models.PositiveIntegerField(validators=[MaxValueValidator(59)])


    def __str__(self):
        return f'{self.name}:{self.tag_line}'

class Speaker(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f'{self.name},{self.email}'

class Session(models.Model):
    description=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.description}'


class Booking(models.Model):
    user=models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    event=models.ForeignKey(to=Event, on_delete=models.CASCADE)
    session=models.ForeignKey(to=Session, on_delete=models.CASCADE)
    seats=models.IntegerField()
    
    # @property
    # def available_seats():
    #     self.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
    #     pass
    


