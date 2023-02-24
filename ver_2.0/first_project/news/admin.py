from django.contrib import admin
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id','title','date','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','full_text')
    list_filter = ('is_published',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Articles, ArticlesAdmin)