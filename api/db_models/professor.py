from api.db_models.university_member_base import MemberBase
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from authentication.db_models.users import Users


class Professor(Users, MemberBase):
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)

    class Meta:
        db_table = 'db_professor'
