from django.db import models

# Create your models here.
class feature(models.model):
    name = models.charfield(max_length =100)
    details = models.CharField( max_length= 1000)
    