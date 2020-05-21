from django.contrib import admin
from .models import (Skill)

# Registers all necessary database entries on the django admin page
# to provide a GUI for database editing.

admin.site.register(Skill)
