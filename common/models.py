from django.db import models

# Create your models here.

class contactus (models.Model):
    name =models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    message =models.CharField(max_length=250)
