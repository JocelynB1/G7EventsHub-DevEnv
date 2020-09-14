from django.db import models
from django.conf import settings
from django.contrib import admin


# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    address= models.CharField(max_length=500)
    room_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Event(models.Model):
    location=models.ForeignKey(to=Location,  on_delete=models.CASCADE)
    # location=models.ForeignKey(to=Location,to_field=Location.name,)    
    name=models.CharField(max_length=100)
    tag_line=models.CharField(max_length=500)
    title=models.CharField(max_length=100)
    # start_time=models.DateTimeField()
    # end_time=models.DateTimeField()

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
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    event=models.ForeignKey(to=Event, on_delete=models.CASCADE)
    session=models.ForeignKey(to=Session, on_delete=models.CASCADE)
    seats=models.IntegerField()
    
    # @property
    # def available_seats():
    #     self.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
    #     pass
    


