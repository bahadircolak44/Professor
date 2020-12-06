from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import status

from api.apis.professor.forms import ProfessorGetForm, ProfessorForm
from api.db_models.comment import Comment
from api.db_models.professor import Professor


class ProfessorViewSet(View):
    def get(self, request, *args, **kwargs):
        form = ProfessorGetForm(request.GET)
        form.is_valid()
        if not form.errors:
            professor_id = form.cleaned_data.get('professor_id')
            professor = Professor.objects.filter(id=professor_id).first()
            comments = Comment.objects.filter(professor_id=professor_id)
            professor_form = ProfessorForm(instance=professor)
            professor_form.is_valid()
            if not professor_form.errors:
                context = dict(forms=professor_form, comments=comments)
                return render(request, template_name='prof_page.html', context=context)
        return HttpResponseRedirect('/login/')
