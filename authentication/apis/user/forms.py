from django.forms import ModelForm, models
from django import forms

from api.db_models.student import Student
from api.db_models.universities import Universities
from authentication.db_models.users import Users


class UserForm(ModelForm):
    university = forms.ModelChoiceField(queryset=Universities.objects.all(),  initial=0)

    def save(self, commit=True):
        student = Student.objects.create_user(**self.cleaned_data)
        student.save()

    class Meta:
        model = Student
        exclude = ('is_admin', 'last_login')


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
