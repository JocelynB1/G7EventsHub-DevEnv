from django.db import models
from django.conf import settings
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Detail(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True,null=True)
    phone_number= models.CharField(max_length=10)
    city= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Details for {self.user.username}'

#date must bee after today, cant have two sessions i same session in one day
# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    address= models.CharField(max_length=500)
    room_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Speaker(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return f'{self.name},{self.email}'

class Event(models.Model):
    # HOURS=[
    # ("0 ","0 "),
    # ("1 ","1 "),
    # ("2 ","2 "),
    # ("3 ","3 "),
    # ("4 ","4 "),
    # ("5 ","5 "),
    # ("6 ","6 "),
    # ("7 ","7 "),
    # ("8 ","8 "),
    # ("9 ","9 "),
    # ("10 ","10 "),
    # ("11 ","11 "),
    # ("12 ","12 "),
    # ("13 ","13 "),
    # ("14 ","14 "),
    # ("15 ","15 "),
    # ("16 ","16 "),
    # ("17 ","17 "),
    # ("18 ","18 "),
    # ("19 ","19 "),
    # ("20 ","20 "),
    # ("21 ","21 "),
    # ("22 ","22 "),
    # ("23 ","23 "),
    #  ]
    
    location=models.ForeignKey(to=Location,  on_delete=models.CASCADE)
    tag_line=models.CharField(max_length=500)
    title=models.CharField(max_length=100)
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    session_choices=(
        ("Morning","Morning"),
        ("Midmorning","Midmorning"),
        ("Afternoon","Afternoon")
        )
    session=models.CharField(max_length=100,choices=session_choices)
    # total_events=this.objects.Count()
    # start_date=models.DateField(validators=[MinValueValidator(limit_value=date.today)])
    # start_hour=models.CharField(max_length=5,choices=HOURS,blank=True)
    # start_minutes=models.PositiveIntegerField(validators=[MaxValueValidator(59)])
    # end_date=models.DateField(validators=[MinValueValidator(limit_value=date.today)])
    # end_hour=models.CharField(max_length=5,choices=HOURS,blank=True)
    # end_minutes=models.PositiveIntegerField(validators=[MaxValueValidator(59)])

  
    def __str__(self):
        return f'{self.title}'


class Session(models.Model):
    description=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.description}'


class Booking(models.Model):
    user=models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    event=models.ForeignKey(to=Event, on_delete=models.CASCADE)
    seats=models.IntegerField()
    
    # @property
    # def available_seats():
    #     self.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
    #     pass
    


