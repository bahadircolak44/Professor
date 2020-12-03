
from rest_framework import serializers

from api.db_models.university_member_base import get_universities
from authentication.db_models.users import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'last_login', 'email', 'first_name', 'last_name')


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'password', 'user_type')


class MemberRegistrationSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    user = UserRegistrationSerializer()
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)
    universities = serializers.ChoiceField(choices=get_universities(), required=True)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = Users
        fields = ('email', 'password')
