from django.contrib import admin
from .models import BlogPost
from comment.models import Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


  
admin.site.register(BlogPost, PostAdmin)
