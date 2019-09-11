from django import forms
from .models import Resource

class AddResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['url']
        #exclude = ["user"]

class EditResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        exclude = ["user"]

