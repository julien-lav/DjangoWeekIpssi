from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    startTime = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:mm'}))
    endTime = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:mm'}))
    class Meta:
        model = Course
        exclude = ["teacher", "students"]

