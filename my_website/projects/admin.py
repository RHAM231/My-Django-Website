from django.contrib import admin
from .models import (CheckListHeader,
                     CheckListEntry,
                     SubHeader,
                     RefLink,
                     LinkHeader,
                     Project,
                     ProjectDescription,
                     ProjectDescriptionList,
                     ProjectSummary,
                     ProjectSummaryList,
                     PortfolioInfo,
                     IconSkill
                     )

# Registers all necessary database entries on the django admin page
# to provide a GUI for database editing.

admin.site.register(CheckListHeader)
admin.site.register(CheckListEntry)
admin.site.register(SubHeader)
admin.site.register(RefLink)
admin.site.register(LinkHeader)
admin.site.register(Project)
admin.site.register(ProjectDescription)
admin.site.register(ProjectSummary)
admin.site.register(ProjectDescriptionList)
admin.site.register(ProjectSummaryList)
admin.site.register(PortfolioInfo)
admin.site.register(IconSkill)
