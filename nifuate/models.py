from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Logo(models.Model):
    image=models.ImageField('upload_to=logo')

class Cause(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='causes')
    description=models.TextField(max_length=500)
    target_amount=models.DecimalField(max_digits=6,decimal_places=2)
    collected_amount=models.DecimalField(max_digits=6,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)