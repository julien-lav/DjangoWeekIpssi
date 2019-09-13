from django import forms
from .models import Resource, Course
from django.contrib.auth.models import User

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        exclude = ["teacher"]

    # def __init__(self, user, *args, **kwargs):
    #     super(ResourceForm, self).__init__(*args, **kwargs)
    #     self.fields['courses'] = forms.ModelMultipleChoiceField(queryset=Course.objects.filter(teacher=user), required=False)   
    #     #self.fields['courses'].queryset = Course.objects.filter(teacher=user)
        
