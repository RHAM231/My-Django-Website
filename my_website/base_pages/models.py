from django.db import models


# Creates the 'Project' entry in the database. This stores all info about
# each of my coding projects. 'index_key' is used to control display order
# on the home page.
class Project(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    index_key = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    link = models.TextField()

    def __str__(self):
        return self.title


# Creates the database entry for the skills displayed on the home page.
# icon_id sets the unique id value in the html for CSS styling.
class IconSkill(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    icon_id = models.CharField(max_length=100)
    link = models.TextField()

    def __str__(self):
        return self.name
