from django.contrib import admin
from .models import Tech

class TechAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ('title','full_text')
    list_filter = ('is_published',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Tech, TechAdmin)