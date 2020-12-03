from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.apis.professor.serializers import ProfessorSerializer, RetrieveProfessorsSerializer
from api.db_models.professor import Professor
from common.permissions.globals import PermissionSetGroup
from common.viewset import BaseViewSet


class ProfessorViewSet(BaseViewSet, ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_set_group = PermissionSetGroup.Student

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.validated_data
    #     professor = Professor.objects.create(university=data.get('university'), user_id=request.user.id)
    #     professor.save()
    #     return Response(status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset(), many=True).data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        professors = list(Professor.objects.filter(university_id=pk))
        return Response(RetrieveProfessorsSerializer(professors, many=True).data)


