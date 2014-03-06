from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    fields = (('title', 'slug'), 'content', 'pub_date', )


admin.site.register(Article, ArticleAdmin)
