from rest_framework import serializers

from api.db_models.professor import Professor
from api.db_models.universities import Universities
from api.db_models.university_member_base import get_universities
from authentication.db_models.users import Users


class ProfessorSerializer(serializers.ModelSerializer):
    name = serializers.ChoiceField(choices=get_universities())

    class Meta:
        model = Universities
        fields = ('name', 'phone', 'address')


class RetrieveUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name')


class RetrieveProfessorsSerializer(serializers.Serializer):
    university_id = serializers.IntegerField(required=True)

