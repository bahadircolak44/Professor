from django.urls import path
from rest_framework import routers


urlpatterns = [

]
routes = [

]

router = routers.DefaultRouter()


for prefix, vset, viewset in routes:
    if viewset:
        router.register(prefix, vset, viewset)
    else:
        router.register(prefix, vset)