from django.db import models

# Create your models here.


class CustomerLogin(models.Model):
    fullname = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.fullname


class OwnerLogin(models.Model):
    fullname = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    pincode = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.fullname
