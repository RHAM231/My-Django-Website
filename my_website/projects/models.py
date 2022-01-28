from django.db import models
from django.apps import apps


'''
'models.py' creates all the database entries. Database entries get
passed to 'views.py'. 'views.py' then renders the entries through 
template tags into the html django templates.
'''


# Creates the 'Project' entry in the database. This stores all info
# about each of my coding projects. 'index_key' is used to control
# display order on the home page.
class Project(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    index_key = models.IntegerField()
    description = models.TextField()
    #image = models.ImageField(upload_to='images')
    link = models.TextField()

    def __str__(self):
        return self.title


# Stores summary paragraphs for projects
class ProjectSummary(models.Model):
    objects = None
    index_key = models.IntegerField()
    header = models.CharField(max_length=100)
    paragraph = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project}, {self.header}'


# Stores summary list items for projects, such as skills,
# to do's, issues encountered, etc.
class ProjectSummaryList(models.Model):
    objects = None
    index_key = models.IntegerField()
    name = models.TextField()
    projectsummary = models.ForeignKey(ProjectSummary,
                                       related_name='summary_key',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Stores large bodies of text describing the projects
class ProjectDescription(models.Model):
    objects = None
    index_key = models.IntegerField()
    header = models.CharField(max_length=100)
    paragraph = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project}, {self.header}'


# Stores project list items, such as skills,
# to do's, issues encountered, etc.
class ProjectDescriptionList(models.Model):
    objects = None
    index_key = models.IntegerField()
    name = models.TextField()
    projectdescription = models.ForeignKey(ProjectDescription,
                                           related_name='description_key',
                                           on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Stores all the checklist headers for the web development checklist
# page
class CheckListHeader(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    indexkey = models.IntegerField()

    def __str__(self):
        return self.name


# Stores all the checklist entries for the web development checklist
# page
class CheckListEntry(models.Model):
    objects = None
    name = models.TextField()
    checklistheader = models.ForeignKey(CheckListHeader,
                                        related_name='entry_key',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Model for storing sub headers, not currently used
class SubHeader(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    checklistheader = models.ForeignKey(CheckListHeader,
                                        related_name='subheader_key',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Reference link headers used on the checklist page. See
# project_checklist.html
class LinkHeader(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Reference links used on the checklist page. See
# project_checklist.html
class RefLink(models.Model):
    objects = None
    name = models.TextField()
    link = models.TextField()
    linkheader = models.ForeignKey(LinkHeader,
                                   related_name='link_key',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Enters me in the database. Currently unused in the frontend but left
# in for future scaling if needed
class PortfolioInfo(models.Model):
    objects = None
    name_first = models.CharField(max_length=100)
    name_last = models.CharField(max_length=100)
    my_title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    background = models.TextField()

    def __str__(self):
        return self.name_first


# Stores my skills
class PortfolioSkill(models.Model):
    objects = None
    skill = models.CharField(max_length=100)
    person = models.ForeignKey(PortfolioInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill
