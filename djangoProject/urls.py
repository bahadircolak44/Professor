"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api.apis.main_page.api import MainPageView
from authentication.apis.user.apis import UserLoginView, UserRegisterStepView, UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('v1/', include(auth_router_2.urls)),
    # path('v1/', include(auth_router.urls)),
    path('', UserLoginView.as_view(), name='main'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('step/', UserRegisterStepView.as_view(), name='step'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('main/', MainPageView.as_view(), name='main')
]
