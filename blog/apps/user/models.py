# 引入验证，最大值（长度），最小（长度），正则验证
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator, \
    RegexValidator
# 引入继承
from django.db import models

# 引入基础类
from db.base_model import BaseModel


class UserModels(BaseModel):
    # 昵称
    nickname = models.CharField(max_length=20, validators=[MinLengthValidator(2)], verbose_name='昵称')
    # 密码
    password = models.CharField(max_length=32, validators=[MinLengthValidator(32)], verbose_name='密码')
    # 邮箱
    email=models.EmailField()
    # 手机号
    phone = models.CharField(max_length=11, verbose_name='手机号',
                             validators=[RegexValidator(regex=r'^1[34578]\d{9}$', message='手机号码格式不正确')], )
    # 性别
    choices = (
        (1, '男'),
        (2, '女'),
        (3, '保密'),
    )
    gender = models.SmallIntegerField(choices=choices, verbose_name='性别', default=3)
    # 头像
    head = models.ImageField(upload_to='user/%y%m/%d', default='user/1902/10/haed.jpg', verbose_name='头像')
    # 学校
    school = models.CharField(max_length=50, verbose_name='学校')
    # 老家
    hometown = models.CharField(max_length=100, verbose_name='老家')
    # 位置
    address = models.CharField(max_length=100, verbose_name='老家')
    # 生日
    birthday = models.DateField(auto_now_add=True, verbose_name='生日')

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = "user"  # 表名
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

