from django.shortcuts import render
from django.views import View

from api.apis.main_page.forms import UniversityForm, MainPageForm
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

        university_dict = dict(university=list(university_list), professor=professor_list)

        return render(request, template_name='main_3.html', context=university_dict)

    def post(self, request, *args, **kwargs):
        pass
