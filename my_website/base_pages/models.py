from django.db import models


# Creates the database entry for the skills displayed on the home page.
# icon_id sets the unique id value in the html for CSS styling.
class Skill(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    icon_id = models.CharField(max_length=100)
    link = models.TextField()

    def __str__(self):
        return self.name
