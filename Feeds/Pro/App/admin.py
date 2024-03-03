from django.contrib import admin
from .models import Message,Comment,Like
# Register your models here.

admin.site.register((Message,Comment,Like))