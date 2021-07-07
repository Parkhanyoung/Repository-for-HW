from django.contrib import admin
from .models import Todo, Comment, Like, Scrap
# Register your models here.
admin.site.register(Todo)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Scrap)
