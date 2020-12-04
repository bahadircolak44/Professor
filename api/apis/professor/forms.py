from django import forms

from api.db_models.professor import Professor
from api.db_models.universities import Universities


class ProfessorGetForm(forms.Form):
    prof_id = forms.IntegerField(required=True)


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['total_rate', 'salary_estimation', 'hot_rate', 'kindness', 'style', 'teach_rate', 'approach_rate',
                  'first_name', 'last_name', 'email']
