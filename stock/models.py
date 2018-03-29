from django.db import models

# Create your models here.
from django.db import models

class ticker(models.Model):
    symbol = models.CharField(null=False,max_length=50)
    date = models.DateField(null=False)
    open = models.FloatField(null=False)
    high = models.FloatField(null=False)
    low = models.FloatField(null=False)
    close = models.FloatField(null=False)
    volume = models.IntegerField(null=False)