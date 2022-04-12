from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import Profile

class UserUpdateForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email']

class TeacherForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ['username' ,'email','user_type' ]

class UserType(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['user_type']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['id','gender','mobile_number','hobby','dob','user_type']