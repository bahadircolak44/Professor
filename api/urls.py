from rest_framework import routers

from api.apis.professor.api import ProfessorViewSet
from api.apis.student.api import StudentViewSet
from api.apis.university.api import UniversitiesViewSet

router = routers.DefaultRouter()
router_v2 = routers.DefaultRouter()
urlpatterns = []
routes = [
    (r'student', StudentViewSet, None),
    (r'professor', ProfessorViewSet, None),
    (r'universities', UniversitiesViewSet, None)
]


for prefix, vset, viewset in routes:
    if viewset:
        router.register(prefix, vset, viewset)
    else:
        router.register(prefix, vset)
