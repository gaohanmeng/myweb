# from django.contrib import admin

import xadmin
# from xadmin.layout import Row, Fieldset

from .models import Link, SideBar
# from GMyBlog.custom_site import custom_site
from GMyBlog.base_admin import BaseOwnerAdmin


@xadmin.sites.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@xadmin.sites.register(SideBar)
# class SideBarAdmin(admin.ModelAdmin):
class SideBarAdmin(BaseOwnerAdmin):
    list_display = (
        'title', 'display_type', 'content', 'created_time'
    )
    fields = (
        'title', 'display_type', 'content'
    )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
