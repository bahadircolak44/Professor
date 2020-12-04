from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import status

from api.apis.professor.forms import ProfessorGetForm, ProfessorForm
from api.db_models.professor import Professor


class ProfessorViewSet(View):
    def get(self, request, *args, **kwargs):
        form = ProfessorGetForm(request.GET)
        form.is_valid()
        if not form.errors:
            professor_id = form.cleaned_data.get('prof_id')
            professor = Professor.objects.filter(id=professor_id).first()
            professor_form = ProfessorForm(data=professor)
            professor_form.is_valid()
            if not professor_form.errors:
                context = dict(forms=professor_form)
                return render(request, status=status.HTTP_200_OK, template_name='prof_page', context=context)
        return HttpResponseRedirect('/login/')
