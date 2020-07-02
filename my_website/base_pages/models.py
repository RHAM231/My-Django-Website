from django.db import models


class Skill(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    icon_id = models.CharField(max_length=100)
    link = models.TextField()

    def __str__(self):
        return self.name
