from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Logo(models.Model):
    image=models.ImageField('upload_to=logo')


class OnlineMember(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    NOT_SPECIFIED = 'N'    

    GENGER_CHOICES = [
   (MALE, 'Male'),
   (FEMALE, 'Female'),
   (OTHER, 'Other'),
   (NOT_SPECIFIED, 'Not Specified'),    
]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=PhoneNumberField() 
    gender=models.CharField(max_length=10,choices=GENGER_CHOICES,default='NOT_SPECIFIED')
    


    def __str__(self):
        return f"{self.first_name} {self.get_gender_display()} {self.country.name}"
