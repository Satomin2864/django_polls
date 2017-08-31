from django.contrib import admin

# Register your models here.

from .models import import Question

admin.site.register(Question)
