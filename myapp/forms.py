from django import forms
from .models import task


class Formtask(forms.ModelForm):
	class Meta:
		model = task
		fields = ['title','description','important']