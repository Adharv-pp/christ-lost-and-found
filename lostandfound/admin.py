# lostandfound/admin.py
from django.contrib import admin
from .models import Category, LostItem

# A simple registration is enough to get started
admin.site.register(Category)
admin.site.register(LostItem)