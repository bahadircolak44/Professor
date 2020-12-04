from api.db_models.university_member_base import MemberBase
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from authentication.db_models.users import Users


class Professor(Users, MemberBase):
    total_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    salary_estimation = models.FloatField(validators=[MinValueValidator(0)], default=0)
    hot_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    kindness = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    style = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    teach_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    approach_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)

    class Meta:
        db_table = 'db_professor'

