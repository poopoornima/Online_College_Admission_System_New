from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=122, default="")
    father = models.CharField(max_length=122, default="")
    mother = models.CharField(max_length=122, default="")
    email = models.CharField(max_length=122, default="")
    phone = models.CharField(max_length=12, default="")
    ApplicationNumber = models.CharField(max_length=12, default="")
    Percentile = models.CharField(max_length=12, default="")
    Address1 = models.TextField(default="")
    file = models.FileField( default="")
    file1 = models.FileField( default="")

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
