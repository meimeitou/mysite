from django.db import models
from polls.models import Question


# Create your models here.


class Comments(models.Model):
    content = models.CharField(max_length=200)
    title = models.CharField(blank=True, null=None, max_length=20)
    pub = models.ForeignKey(Question)

    def __str__(self):
        return self.title
