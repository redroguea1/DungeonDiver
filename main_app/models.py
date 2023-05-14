from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

JOBS = (
    ('F', 'Fighter'),
    ('C', 'Cleric'),
    ('P', 'Paladin'),
    ('R', 'Rogue'),
    ('S', 'Sorcerer'),
)


class Diver(models.Model):
    name = models.CharField(max_length=50, default='')
    race = models.CharField(max_length=75, default='')
    job = models.CharField(
        max_length=20, 
        )
    backstory = models.TextField(max_length=250, default='')
    level = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        charString = (self.name + ", JOB:" + self.job) 
        return charString 
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'diver_id': self.id})
    
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    diver = models.ForeignKey(Diver, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return ("name:" + self.name)

    def get_absolute_url(self):
        return reverse('items_detail', kwargs={'pk': self.id})