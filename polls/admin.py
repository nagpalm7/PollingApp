from django.contrib import admin
from .models import Question, Choice

# Register your models here.
models = [Question, Choice]
admin.site.register(models)