from django.contrib import admin
from .models import Article, Comments


class CommentsInline(admin.TabularInline):
    model=Comments

class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        CommentsInline,
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)