from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']

admin.site.register(Comment, CommentAdmin)
# Register your models here.
