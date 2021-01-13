from django.db import models

# Create your models here.
class Advert(models.Model):
     advert_url =  models.URLField(max_length=200,)
     image = models.ImageField(upload_to='images')