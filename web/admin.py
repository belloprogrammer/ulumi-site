from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body','author')
    search_fields = ('title', 'body', 'created', 'author')
    prepopulated_fields = {'slug':['title']}
    raw_id_fields = ('author',)
    date_hierarchy = ('created')
    ordering = ('created',)