from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Advert(models.Model):
     advert_url =  models.URLField(max_length=200,)
     title = models.CharField(max_length=200, blank=True)
     image = ImageField(upload_to='images')