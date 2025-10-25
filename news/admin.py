from django.contrib import admin
from news.models import Newspaper, Topics, Redactor


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ['title','topic', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'topic', 'publisher__username']


@admin.register(Topics)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['username']
    search_fields = ['username', 'first_name', 'last_name']
