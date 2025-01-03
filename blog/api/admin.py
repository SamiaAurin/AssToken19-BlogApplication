from django.contrib import admin
from api.models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'body', 'owner', 'created')