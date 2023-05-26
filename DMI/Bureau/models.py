from django.db import models

# Create your models here.
#https://www.w3schools.com/django/django_update_data.php

class Bureau(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone_no = models.IntegerField(null=True)
    joined_date = models.IntegerField(null=True)