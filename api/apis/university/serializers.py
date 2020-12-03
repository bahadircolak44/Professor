from rest_framework import serializers

from api.db_models.professor import Professor
from api.db_models.universities import Universities


class UniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = ('name', 'phone', 'website', 'address')


class ProfessorSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(required=True)

    class Meta:
        model = Professor
        fields = ('id', 'rate', 'user_id', 'user_first_name')
