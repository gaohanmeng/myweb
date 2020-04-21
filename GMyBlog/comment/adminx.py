import xadmin

# from django.contrib import admin

from .models import Comment
# from GMyBlog.custom_site import custom_site
# from GMyBlog.base_admin import BaseOwnerAdmin


@xadmin.sites.register(Comment)
class CommentAdmin:
    list_display = ('target', 'nickname', 'content', 'created_time')
