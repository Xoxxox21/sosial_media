from django.contrib import admin
from .models import Profile, Post, Like_post, Follower_count

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like_post)
admin.site.register(Follower_count)