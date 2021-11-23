from django import forms
from django.forms import fields
from . import models


class MonthlyReportForm(forms.ModelForm):
    class Meta:
        model = models.MonthlyReport 
        fields ='__all__'




class DialyNotesForm(forms.ModelForm):
    class Meta:
        model = models.DailyNotes
        fields = '__all__'



class MonthTasksForm(forms.ModelForm):
    class Meta:
        model = models.MonthMenets
        fields = '__all__'