from django.db import models
from django.conf import settings

# Create your models here.



class Location(models.Model):
    name=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    address= models.CharField(max_length=500)
    room_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

        
class Event(models.Model):
    location=models.ForeignKey(to=Location, on_delete=models.CASCADE)    
    name=models.CharField(max_length=100)
    tag_line=models.CharField(max_length=500)
    topic=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}:{self.tag_line}'


class Speaker(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f'{self.name},{self.email}'

    
class Session(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'



class Booking:
    class Meta:
        unique_together = (('user', 'location','event'),)

    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    location=models.OneToOneField(to=Location, on_delete=models.CASCADE)    
    event=models.OneToOneField(to=Event, on_delete=models.CASCADE)
    session=models.OneToOneField(to=Session, on_delete=models.CASCADE)
    seats=models.IntegerField()
    
    @property
    def available_seats():
        pass
    

