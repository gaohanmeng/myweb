from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post, Category
from .serializers import PostSerializer, PostDetailSerializer, \
    CategorySerializer, CategoryDetailSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        # queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
        # permission_classes = [IsAdminUser]  # 写入时的权限校验
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(catefory_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)
