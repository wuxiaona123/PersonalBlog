from django.db import models


class BaseModel(models.Model):
    # 添加时间
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    # 修改时间
    up_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        # 说明是一个抽象模型类，不会被迁移
        abstract = True
