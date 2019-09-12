from django import forms
from .models import Course, DAY_OF_THE_WEEK_CHOICES

class CourseForm(forms.ModelForm):
    dayOfTheWeek = forms.ChoiceField(choices = DAY_OF_THE_WEEK_CHOICES)
    startTime = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:mm', 'type': 'time'}))
    endTime = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:mm', 'type': 'time'}))

    class Meta:
        model = Course
        exclude = ["teacher", "students"]

