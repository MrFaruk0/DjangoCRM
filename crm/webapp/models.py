from django.db import models

# Create your models here.


class Client(models.Model):

    creationDate = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName + " " + self.lastName




