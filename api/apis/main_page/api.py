from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View

from api.apis.main_page.forms import MainPagePostForm
from api.db_models.professor import Professor
from api.db_models.universities import Universities


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        university_list = Universities.objects.order_by('-rate')[:5]

        professor_list = [
            {'first_name': 'Pınar', 'last_name': 'Yalavaç', 'rate': 100},
            {'first_name': 'Bahadır', 'last_name': 'Çolak', 'rate': 90},
            {'first_name': 'Sina', 'last_name': 'Çolak', 'rate': 80},
            {'first_name': 'Ece', 'last_name': 'Yalavaç', 'rate': 70},
            {'first_name': 'Ahmet', 'last_name': 'Yalavaç', 'rate': 60}
        ]

        university_dict = dict(university=list(university_list), professor=professor_list,
                               university_all=list(Universities.objects.all()))
        print()
        return render(request, template_name='main_3.html', context=university_dict)

    def post(self, request, *args, **kwargs):
        form = MainPagePostForm(data=request.data)
        form.is_valid()
        if form.errors:
            return HttpResponseRedirect('/login/')
        university_id = form.cleaned_data.get('university')
        prof_list = Professor.objects.filter(university_id=university_id)
        return JsonResponse(request, prof_list)
