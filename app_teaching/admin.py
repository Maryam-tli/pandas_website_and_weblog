from django.contrib import admin
from .models import Tag, PandasClass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)



@admin.register(PandasClass)
class PandasClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published', 'views') 
    list_filter = ('status', 'published') 
    search_fields = ('title', 'description', 'content') 
    prepopulated_fields = {'slug': ('title',)} 
    filter_horizontal = ('tags',)  

    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'content', 'example_code', 'tags')
        }),
        ('Publishing Info', {
            'fields': ('status', 'published', 'views'),
            'classes': ('collapse',)  
        }),
    )