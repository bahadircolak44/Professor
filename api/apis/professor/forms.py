from django import forms

from api.db_models.professor import Professor
from api.db_models.universities import Universities


class ProfessorGetForm(forms.Form):
    professor_id = forms.IntegerField(required=True)


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['total_rate', 'salary_estimation', 'hot_rate', 'kindness_rate', 'response_rate', 'teach_rate', 'approach_rate',
                  'first_name', 'last_name', 'email', 'title']


class ProfessorRateForm(forms.Form):
    salary_estimation = forms.IntegerField(required=True)
    hot_rate = forms.IntegerField(required=True)
    kindness_rate = forms.IntegerField(required=True)
    response_rate = forms.IntegerField(required=True)
    teach_rate = forms.IntegerField(required=True)
    approach_rate = forms.IntegerField(required=True)
    comment = forms.CharField(required=True)