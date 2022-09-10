from django.db import models
from django.db.models import (Model, ForeignKey, PositiveSmallIntegerField,
        DecimalField, CharField, TextField, DateField, DateTimeField)



class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    
class Checkins(models.Model):
    seq = models.IntegerField()
    rm = models.CharField(max_length=6)
    mark = models.CharField(max_length=6)
    days = models.IntegerField()

    rate = DecimalField(max_digits=9, decimal_places=2)
