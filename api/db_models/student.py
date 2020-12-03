from api.db_models.university_member_base import MemberBase
from authentication.db_models.users import Users
from django.db import models


class Student(Users, MemberBase):
    grade = models.FloatField(default=0, null=True)

    class Meta:
        db_table = 'db_student'
