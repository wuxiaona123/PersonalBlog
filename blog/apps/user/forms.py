# 引入继承
import re

from django import forms

# 引入模型
from db.app_common import set_password
from user.models import UserModels


# 验证登录
class LoginForms(forms.ModelForm):
    # 密码
    password = forms.CharField(max_length=10,
                               min_length=6,
                               error_messages={
                                   'required': '请填写密码',
                                   'max_length': '密码最大长度为10位',
                                   'min_length': '密码最小长度为6位',
                               })

    # 验证昵称
    class Meta:
        model = UserModels
        fields = ['nickname']
        error_messages = {
            'nickname': {
                'required': '请填写昵称',
                'max_length': '昵称长度为2个字符-20个字符之间',
                'min_length': '昵称长度为2个字符-20个字符之间',
            }
        }

    # 验证手机号码是否已经注册，密码是否正确
    def clean(self):
        data = self.cleaned_data
        nickname = data.get('nickname')
        try:
            user = UserModels.objects.get(nickname=nickname)
        except:
            raise forms.ValidationError({'nickname': '此昵称未注册，请注册'})

        password = set_password(data.get('password'))

        if user.password != password:
            raise forms.ValidationError({'password': '密码不正确'})

        data['user'] = user
        return data




# 验证注册
class RegisterForms(forms.ModelForm):
    # 密码
    password = forms.CharField(max_length=10,
                               min_length=6,
                               error_messages={
                                   'required': '请填写密码',
                                   'max_length': '密码最大长度为10位',
                                   'min_length': '密码最小长度为6位',
                               })
    # 确认密码
    repassword = forms.CharField(max_length=10,
                                 min_length=6,
                                 error_messages={
                                     'required': '请填写确认密码',
                                     'max_length': '确认密码最大长度为10位',
                                     'min_length': '确认密码最小长度为6位',
                                 })
    # 邮箱
    email = forms.EmailField(error_messages={
        'required': '请填写邮箱',
    })

    # 验证码
    yzm = forms.CharField(
        error_messages={
            'required': '请填写验证码',
        })

    # 是否同意用户协议
    checkbox = forms.BooleanField(error_messages={
        'required': '请阅读用户协议后同意',
    })

    # 验证昵称
    class Meta:
        model = UserModels
        fields = ['nickname']
        error_messages = {
            'nickname': {
                'required': '请填写昵称',
                'max_length': '昵称长度为2个字符-20个字符之间',
                'min_length': '昵称长度为2个字符-20个字符之间',
            }
        }

    # 再次验证昵称，是否已经注册
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        ifexi = UserModels.objects.filter(nickname=nickname).exists()
        if ifexi:  # 数据库已经存在这个昵称，不能让他注册
            raise forms.ValidationError('昵称已经注册')
        else:  # 数据库不存在，可以让他继续注册
            return nickname

    # 综合验证，验证两次密码是否一致
    def clean(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if password and repassword and password != repassword:
            raise forms.ValidationError({'repassword': '两次密码不一致'})
        return self.cleaned_data

    # # 验证  验证码
    def clean_yzm(self):
        yzm = self.cleaned_data['yzm']  # 用户传过来的验证码
        verification = self.data.get('verification')  # 服务器保存的验证码
        if yzm == verification:
            return yzm
        else:
            raise forms.ValidationError('验证码错误')

# # 验证修改密码
# class SetPasswordForm(forms.Form):
#     password = forms.CharField(max_length=10, min_length=6,
#                                error_messages={
#                                    "required": "旧密码必填",
#                                    "max_length": "密码长度不能大于10个字符",
#                                    "min_length": "标题长度不能小于6个字符",
#                                })
#
#     newpassword = forms.CharField(max_length=10, min_length=6,
#                                   error_messages={
#                                       "required": "新密码必填",
#                                       "max_length": "密码长度不能大于10个字符",
#                                       "min_length": "标题长度不能小于6个字符",
#                                   })
#
#     renewpassword = forms.CharField(max_length=10, min_length=6,
#                                     error_messages={
#                                         "required": "确认密码必填",
#                                         "max_length": "密码长度不能大于10个字符",
#                                         "min_length": "标题长度不能小于6个字符",
#                                     })
#
#
#
#     # 判断旧密码是否正确
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         mipassword = set_password(password)
#         userid = self.data.get('userid')
#         try:
#             user = UserModels.objects.get(id=userid)
#         except:
#             raise forms.ValidationError('登录标识错误，请重新登录后再修改密码')
#         if mipassword == user.password:
#             return password
#         else:
#             raise forms.ValidationError('密码错误')
#
#     def clean(self):
#         newpassword = self.cleaned_data.get('newpassword')
#         renewpassword = self.cleaned_data.get('renewpassword')
#         if newpassword and renewpassword and newpassword != renewpassword:
#             raise forms.ValidationError({"renewpassword": "两次密码不一致"})
#         else:
#             return self.cleaned_data
#
#
#
# class AddressAddForm(forms.ModelForm):
#     """用户添加收货地址的表单"""
#     class Meta:
#         model = UserAddress
#         exclude = ['create_time', 'update_time', 'is_delete','user']
#         error_messages = {
#             'username': {
#                 'required': "请填写用户名！",
#             },
#             'phone': {
#                 'required': "请填写手机号码！",
#             },
#             'brief': {
#                 'required': "请填写详细地址！",
#             },
#             'harea': {
#                 'required': "请填写完整地址！",
#             },
#         }
#
#     def clean(self):
#         # 验证如果数据库里地址已经超过6六表报错
#         cleaned_data = self.cleaned_data
#         count = UserAddress.objects.filter(user_id=self.data.get("user_id")).count()
#         if count >= 6:
#             raise forms.ValidationError({"harea":"收货地址最多只能保存6条"})
#
#         # 操作默认值
#         # 如果当前是默认地址,其他 就设置为False
#         if cleaned_data.get('isDefault'):
#             UserAddress.objects.filter(user_id=self.data.get("user_id")).update(isDefault=False)
#
#         return cleaned_data
