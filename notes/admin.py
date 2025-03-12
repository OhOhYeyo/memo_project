from django.contrib import admin
from .models import Note  # 현재 폴더위치에 있는 models.py

# Register your models here.

admin.site.register(Note)
