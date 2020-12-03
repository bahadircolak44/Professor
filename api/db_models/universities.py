from django.db import models


class Universities(models.Model):
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, null=True)
    website = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    rate = models.FloatField(default=0)
    class Meta:
        db_table = 'db_universities'

    def __str__(self):
        return self.name
