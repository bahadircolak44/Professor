from django.forms import ModelForm, models
from django import forms

from api.db_models.professor import Professor
from api.db_models.student import Student
from api.db_models.universities import Universities
from authentication.db_models.users import Users


class StudentForm(ModelForm):
    university = forms.ModelChoiceField(queryset=Universities.objects.all(),  initial=0)

    class Meta:
        model = Student
        exclude = ('is_admin', 'last_login')


class ProfessorForm(ModelForm):
    university = forms.ModelChoiceField(queryset=Universities.objects.all(),  initial=0)

    class Meta:
        model = Professor
        exclude = ('is_admin', 'last_login', 'total_rate', 'salary_estimation', 'hot_rate', 'kindness', 'style',
                   'teach_rate', 'approach_rate')


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
