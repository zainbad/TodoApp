from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
				"class": "form-control",
			})



class todoForm(forms.ModelForm):
	class Meta:
		model = Todo_list
		fields = ['name']

	def __init__(self, *args, **kwargs):
		super(todoForm, self).__init__(*args, **kwargs)
		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
				"class": "form-control",
			})


class taskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name']

		def __init__(self, *args, **kwargs):
			super(taskForm, self).__init__(*args, **kwargs)
			for name in self.fields.keys():
				self.fields[name].widget.attrs.update({
					"class": "form-control",
				})
