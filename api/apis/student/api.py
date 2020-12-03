from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.apis.student.serializers import StudentSerializer
from api.db_models.student import Student
from common.permissions.globals import PermissionSetGroup
from common.viewset import BaseViewSet


class StudentViewSet(BaseViewSet, ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_set_group = PermissionSetGroup.Student

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        student = Student.objects.create(university=data.get('university'), user_id=request.user.id)
        student.save()
        return Response(status=status.HTTP_201_CREATED)
