# Generated by Django 5.0.6 on 2024-06-25 09:30


import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nifuate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'Not Specified')], default='NOT_SPECIFIED', max_length=10)),
                
            ],
        ),
    ]
