from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'published_date')
    list_per_page = 30
    search_fields = ['article_title']

admin.site.register(Article, ArticleAdmin)
