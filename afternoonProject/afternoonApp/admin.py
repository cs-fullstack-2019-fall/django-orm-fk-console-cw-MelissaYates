from django.contrib import admin

# Register your models here.
from .models import Author, Post

# Register your models here.
admin.site.register(Author) #creates option to make different authors
admin.site.register(Post) #creates option to make different posts and allows tying to different authors based on choice
