from django.db import models
from jsonfield import JSONField


# Create your models here.

class MockData(models.Model):
    name = models.CharField(max_length=10, default='')
    json = JSONField(default=None)

    def __str__(self):
        return self.name

