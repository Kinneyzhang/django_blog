from django.contrib import admin

from .models import Category, Tag, Post, Friend, Diary, Video, PlanCategory, Plan
from django.db import models
from mdeditor.widgets import MDEditorWidget

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstract', 'timestamp',
                    'count', 'category', 'status')
    list_filter = ('status', 'category', 'tags')
    date_hierarchy = 'timestamp'
    list_editable = ('abstract', 'status','count')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'description')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'content')

class PlanCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'timevalue')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(PlanCategory, PlanCategoryAdmin)
admin.site.register(Plan, PlanAdmin)
