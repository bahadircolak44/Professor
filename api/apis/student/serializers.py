from rest_framework import serializers

from api.db_models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('university', 'user_id')