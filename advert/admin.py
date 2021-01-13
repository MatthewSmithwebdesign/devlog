from django.contrib import admin
from advert.models import Advert
# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    pass


admin.site.register(Advert, AdvertAdmin)