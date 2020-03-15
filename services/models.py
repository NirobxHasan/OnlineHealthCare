from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=160)
    def __str__(self):
        return self.name

class Eprescription(models.Model):
    pname=models.ForeignKey(User,on_delete=models.CASCADE)    
    Medicine = models.ManyToManyField(Medicine)
    date_posted = models.DateTimeField(default=timezone.now)
# class Tags(models.Model):
    