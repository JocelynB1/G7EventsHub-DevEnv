from django.contrib import admin
from .models import Details
# Register your models here.
@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display=["user","date_of_birth","phone_number","city","address"]
