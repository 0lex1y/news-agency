from django.contrib import admin
from news.models import Newspaper, Topics, Redactor


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ['title','topic', 'publisher', 'published_date']
    filter = ['published_date']
    search_fields = ['title', 'topic', 'publisher']


@admin.register(Topics)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter = ['name']


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    filter = ['username']
    search_fields = ['username', 'first_name', 'last_name']
