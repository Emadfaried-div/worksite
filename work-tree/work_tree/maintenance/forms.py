from django import forms
from .models import CheckList,UtilityCheckList



class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields ="__all__"


class UtilityCheckListForm(forms.ModelForm):
    class Meta:
        model = UtilityCheckList
        fields ="__all__"