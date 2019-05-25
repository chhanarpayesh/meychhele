from django.contrib import admin

# Register your models here.
from .models import CinemaBook, DesignShot, LocationShot, FoodShot
admin.site.register(CinemaBook)
admin.site.register(DesignShot)
admin.site.register(LocationShot)
admin.site.register(FoodShot)
