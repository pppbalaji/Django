#import floppyforms as forms

from django import forms
from django.forms.extras.widgets import SelectDateWidget




    

class ProfileForm(forms.Form):
	First_Name = forms.CharField()
	Last_Name = forms.CharField()
	Date= forms.DateField(widget=SelectDateWidget)
	Email=forms.EmailField()
	Phone=forms.CharField()
	
	
	
	
	
	




	
