from django.db import models
from django.conf import settings

# Create your models here.

class Detail(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True,null=True)
    phone_number= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    address= models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Details for {self.user.username}'