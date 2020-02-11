from django import forms
from django.contrib.auth.models import User
from QuizApp.models import *
class SignUpForm(forms.ModelForm):
	phone=forms.IntegerField()
	branch=forms.CharField(max_length=255)
	class Meta:
		model=User
		fields=('username','email','phone','password','branch')
		widgets={
		'password':forms.PasswordInput(),
		}


class contactform(forms.ModelForm):
	Message=forms.CharField(widget=forms.Textarea)
	class Meta:
		model=contact_form
		fields=('Name','Email','Subject','Message')

