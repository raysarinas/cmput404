from django.contrib import admin

# Register your models here.
from .models import Choice, Question # manage my choices and questions

admin.site.register(Choice)
admin.site.register(Question)