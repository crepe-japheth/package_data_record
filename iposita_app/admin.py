from django.contrib import admin
from .models import (
   LocalPackage,
   Profile
)
# Register your models here.



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')


@admin.register(LocalPackage)
class LocalPackageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'recipient_name', 'branch')
