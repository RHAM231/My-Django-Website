from django.db import models


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


class Logo(models.Model):
    objects = None
    image = models.ImageField(upload_to='images')


class ProjectSummary(models.Model):
    objects = None
    index_key = models.IntegerField()
    header = models.CharField(max_length=100)
    paragraph = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project}, {self.header}'


class ProjectSummaryList(models.Model):
    objects = None
    index_key = models.IntegerField()
    name = models.TextField()
    projectsummary = models.ForeignKey(ProjectSummary,
                                related_name='summary_key',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProjectDescription(models.Model):
    objects = None
    index_key = models.IntegerField()
    header = models.CharField(max_length=100)
    paragraph = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project}, {self.header}'


class ProjectDescriptionList(models.Model):
    objects = None
    index_key = models.IntegerField()
    name = models.TextField()
    projectdescription = models.ForeignKey(ProjectDescription,
                                related_name='description_key',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class ProjectListItem(models.Model):
#     objects = None
#     index_key = models.IntegerField()
#     name = models.TextField()
#     project = models.ForeignKey(Project,
#                                 related_name='list_key',
#                                 on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name


# Took this model out and split it into the ProjectSummaries
# and ProjectDescriptions models to avoid writing complicated
# frontend filtering logic

# class TextBody(models.Model):
#     objects = None
#     index_key = models.IntegerField()
#     header = models.CharField(max_length=100)
#     paragraph = models.TextField()
#     project = models.ForeignKey(Project,
#                                 related_name='project_key',
#                                 on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.project}, {self.header}'


class CheckListHeader(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    indexkey = models.IntegerField()

    def __str__(self):
        return self.name


class CheckListEntry(models.Model):
    objects = None
    name = models.TextField()
    checklistheader = models.ForeignKey(CheckListHeader,
                                        related_name='entry_key',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubHeader(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    checklistheader = models.ForeignKey(CheckListHeader,
                                        related_name='subheader_key',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LinkHeader(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RefLink(models.Model):
    objects = None
    linkheader = models.ForeignKey(LinkHeader,
                                   related_name='link_key',
                                   on_delete=models.CASCADE)
    name = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.name


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


class TestObject(models.Model):
    objects = None
    test_attribute = models.CharField(max_length=100)

    def __str__(self):
        return self.test_attribute


class PortfolioSkill(models.Model):
    objects = None
    skill = models.CharField(max_length=100)
    person = models.ForeignKey(PortfolioInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill
