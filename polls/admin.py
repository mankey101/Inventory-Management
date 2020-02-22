from django.contrib import admin

from .models import RoomResource, RoomBooking
# Register your models here.

admin.site.register(RoomResource)
admin.site.register(RoomBooking)
