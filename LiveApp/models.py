from django.db import models

# Create your models here.
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(("email address"), unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()