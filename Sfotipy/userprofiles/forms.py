from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailForm()

	class Meta:
		model = User 
		fields  = ('username','email')
