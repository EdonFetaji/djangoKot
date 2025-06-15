from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Baker(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname} | {self.phone_number}'


class Cake(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='cake_images/', null=True, blank=True)
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE, null=True, blank=True, related_name='cakes')

    def __str__(self):
        return self.name
