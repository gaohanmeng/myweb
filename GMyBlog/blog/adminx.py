import xadmin
from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import RelatedFieldListFilter
from xadmin.filters import manager

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
# from GMyBlog.custom_site import custom_site
from GMyBlog.base_admin import BaseOwnerAdmin


class PostInline(admin.TabularInline):
    # fields = ('title', 'desc')
    form_layout = (
        Container(
            Row('title', 'desc'),
        )
    )
    extra = 5
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


# class CategoryOwnerFilter(admin.SimpleListFilter):
class CategoryOwnerFilter(RelatedFieldListFilter):

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')
    # """自定义过滤器只展示当前用户分类"""
    # title = '分类过滤器'
    # parameter_name = 'owner_category'
    #
    # def lookups(self, request, model_admin):
    #     return Category.objects.filter(owner=request.user).values_list('id', 'name')
    #
    # def queryset(self, request, queryset):
    #     category_id = self.value()
    #     if category_id:
    #         return queryset.filter(category_id=self.value())
    #     return queryset


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status', 'created_time', 'owner', 'operator'
    ]
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']

    actions_on_top = True

    save_on_top = False

    # fields = ('title', 'category', 'tag')

    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'tag',
        ),

        Fieldset(
            '文章展示状态',
            Row("status")
        ),

        Fieldset(
            '内容信息', 'desc', 'is_md', 'content_ck', 'content_md', 'content',
        )
    )

    # filter_vertical = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
            # self.model_admin_url('change', obj.id)
        )
    operator.short_description = '操作'
