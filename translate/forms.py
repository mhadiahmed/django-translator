from django import forms 
from .models import TestTranslate

class TestTranslateForm(forms.ModelForm):
    class Meta:
        model = TestTranslate
        fields = ('text','language')

    