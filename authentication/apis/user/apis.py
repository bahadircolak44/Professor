import traceback

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response

from api.db_models.professor import Professor
from api.db_models.student import Student
from .forms import StudentForm, ProfessorForm, LoginForm
from .helpers import UserHelpers


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        request.session.flush()
        return render(request, template_name='login.html', context={})

    def post(self, request, *args, **kwargs):
        print("LOGIN GIRIS")
        form = LoginForm(request.POST)
        form.is_valid()
        if form.errors:
            print(form.errors)
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)

        print("USER: ", user)
        if user:
            login(request, user)
            token = UserHelpers.generate_token(user)
            return HttpResponseRedirect('/main/')
        return HttpResponse(status=status.HTTP_200_OK)


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/login/')


class UserRegisterStepView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='step1.html', context={})


class StudentRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = {'forms': StudentForm}
        return render(request, template_name='student_register.html', context=context)

    def post(self, request, *args, **kwargs):
        try:
            form = StudentForm(data=request.POST)
            form.is_valid()
            if not form.errors:
                email = form.cleaned_data.get('email')
                if UserHelpers.split_email(email):
                    form.cleaned_data['user_type'] = 'student'
                    student = Student.objects.create_user(**form.cleaned_data)
                    student.save()
                else:
                    pass
                    # TODO invalid email type. Email should contain edu.tr
            else:
                print(form.errors)
            return render(request, template_name='login.html', context={})
        except:
            print(traceback.format_exc())


class ProfessorRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = {'forms': ProfessorForm}
        return render(request, template_name='professor_register.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ProfessorForm(data=request.POST)
        form.is_valid()
        if not form.errors:
            email = form.cleaned_data.get('email')
            if UserHelpers.split_email(email):
                form.cleaned_data['user_type'] = 'staff'
                form.cleaned_data['title'] = 'Professor'
                professor = Professor.objects.create_user(**form.cleaned_data)
                professor.save()
            else:
                pass
                # TODO invalid email type. Email should contain edu.tr

        return render(request, template_name='login.html', context={})
