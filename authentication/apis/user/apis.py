from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response

from .forms import UserForm, LoginForm
from .helpers import UserHelpers


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='login.html', context={})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        form.is_valid()
        if form.errors:
            print(form.errors)
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            token = UserHelpers.generate_token(user)
            return HttpResponseRedirect('/main/')
        return HttpResponse(status=status.HTTP_200_OK)


class UserRegisterStepView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='step1.html', context={})


class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = {'forms': UserForm}
        return render(request, template_name='register_1.html', context=context)

    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST)
        form.is_valid()
        form.save()
        return render(request, template_name='login.html', context={})
