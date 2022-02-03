from django import forms
from affairs.models import students


class STform(forms.ModelForm):
    class Meta:
        model = students
        fields = ('username', 'password',)


class Intakeform(forms.Form):
    intakeName = forms.CharField(max_length=100)
    startDate = forms.DateField()
    endDate = forms.DateField()

