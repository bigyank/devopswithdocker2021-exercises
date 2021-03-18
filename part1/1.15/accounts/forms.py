from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.forms import Form
from django.forms.models import ModelForm
from .models import Ambulance, Doctor, DoctorAppointment 


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email",  "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class AmbulanceForm(ModelForm):
	class Meta:
		model = Ambulance
		fields = "__all__"

		# widgets={
		# 	"name": forms.TextInput(attrs={'class':"form-control"}),   #chages the attribute of the form
		# 	"email": forms.EmailField(attrs={'class':"form-control"}),
		# 	"descriptions": forms.TextInput(attrs={'class':"form-control"}),
		# }


class DoctorAppointmentForm(ModelForm):
	class Meta:
		model = DoctorAppointment
		fields =  "__all__"



# class DocotorAppointmentForm(forms.Form):
# 	name = forms.CharField(max_length=30 )
# 	email = forms.EmailField(max_length=30 )
# 	phone = forms.DecimalField(max_digits=10 , decimal_places=0)
# 	sex = forms.ChoiceField(choices=[('Male') , 'Female' , 'Other'] )
# 	Problem =  forms.CharField(max_length=1000 )
