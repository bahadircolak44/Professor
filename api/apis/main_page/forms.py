from django.forms import ModelForm
from django import forms

from api.db_models.universities import Universities


class UniversityForm(ModelForm):
    class Meta:
        model = Universities
        exclude = ('', )


class MainPageForm(forms.Form):
    university = UniversityForm()
    prof = forms.CharField()