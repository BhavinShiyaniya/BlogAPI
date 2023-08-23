from django.contrib import admin
from .models import Post, Like

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'owner')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('like_id', 'post', 'user')

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)