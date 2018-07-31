from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
	# inline class
	class Meta():
		# create model attribute and assign it to User
		model = User
		# use all fields
		fields = '__all__'