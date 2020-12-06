from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View

from api.apis.main_page.forms import MainPagePostForm
from api.db_models.professor import Professor
from api.db_models.universities import Universities


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        university_list = Universities.objects.order_by('-rate')[:5]
        professor_list = Professor.objects.order_by('-total_rate')[:5]
        university_dict = dict(university=list(university_list), professor=list(professor_list),
                               university_all=list(Universities.objects.all()))
        return render(request, template_name='main_3.html', context=university_dict)

    def post(self, request, *args, **kwargs):
        form = MainPagePostForm(data=request.data)
        form.is_valid()
        if form.errors:
            return HttpResponseRedirect('/login/')
        university_id = form.cleaned_data.get('university')
        prof_list = Professor.objects.filter(university_id=university_id)
        return JsonResponse(request, prof_list)
