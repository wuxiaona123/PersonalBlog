# 引入验证，最大值（长度），最小（长度），正则验证
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator, \
    RegexValidator
# 引入继承
from django.db import models
# 引入基础类
from db.base_model import BaseModel
# 引入富文本字段
from ckeditor_uploader.fields import RichTextUploadingField


# 标签表
class TagModels(BaseModel):
    tagname = models.CharField(max_length=15, validators=[MinLengthValidator(2)], verbose_name='标签名')
    parent = models.ForeignKey(to='self', default=0, null=True, blank=True, verbose_name='父id')

    def __str__(self):
        return self.tagname

    class Meta:
        db_table = "tag"  # 表名
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


# 文章表（贴子）
class ArticleModels(BaseModel):
    # 标题
    articletitle = models.CharField(max_length=50, validators=[MinLengthValidator(2)], verbose_name='文章标题')
    # 属于哪个标签
    tagid = models.ForeignKey(to='TagModels', verbose_name='标签')
    # 作者
    author = models.ForeignKey(to='user.UserModels', verbose_name='作者')
    # 富文本
    articlecontent = RichTextUploadingField(verbose_name='文章详情')

    def __str__(self):
        return self.articletitle

    class Meta:
        db_table = "article"  # 表名
        verbose_name = '文章表'
        verbose_name_plural = verbose_name



# 评论模型
class Comment(BaseModel):
    text = models.TextField(verbose_name='评论内容')
    post = models.ForeignKey('ArticleModels', verbose_name='评论文章')
    # 一对多
    users = models.ForeignKey('user.UserModels', verbose_name='评论人')

    def __str__(self):
        return self.text[:20]

    class Meta:
        db_table = "comment"  # 表名
        verbose_name = "评论区管理"
        verbose_name_plural = verbose_name
