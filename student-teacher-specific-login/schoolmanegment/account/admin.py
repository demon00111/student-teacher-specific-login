from django.contrib import admin

from .models import Profile

# Register your models here.
admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','gender','mobile_number','hobby','dob','user_type','caption','video']
