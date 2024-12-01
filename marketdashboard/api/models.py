from django.db import models

class Instrument(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    exchange = models.CharField(max_length=15)
    currency = models.CharField(max_length=15)
    sector = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    description = models.TextField()
    asset_type = models.CharField(max_length=30)
    website = models.CharField(max_length=50)