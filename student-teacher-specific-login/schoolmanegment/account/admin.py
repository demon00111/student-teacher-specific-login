from django.contrib import admin

from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['gender','mobile_number','hobby','dob','user_type']