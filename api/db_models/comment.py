from django.db import models

from api.db_models.professor import Professor
from api.db_models.student import Student


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_count = models.BigIntegerField(default=0)
    comment = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

