from . import views
from django.contrib import admin
from django.urls import  path


urlpatterns = [
    path('',views.profile, name='profile'),
    path('login/',views.loginpage, name='login'),
    path('sdata/',views.sdata, name='sdata'),
    path('tdata/',views.tdata, name='tdata'),
]
