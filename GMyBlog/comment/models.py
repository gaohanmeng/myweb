from django.db import models


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEM = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    # target = models.ForeignKey(Post, verbose_name='评论目标')
    target = models.CharField(max_length=100, verbose_name='评论目标')
    content = models.CharField(max_length=200, verbose_name='内容')
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEM,
                                         verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=cls.STATUS_NORMAL)

    class Meta:
        verbose_name = verbose_name_plural = '评论'
