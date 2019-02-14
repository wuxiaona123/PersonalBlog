from django.contrib import admin

# Register your models here.
from article.models import TagModels, ArticleModels


# 标签
@admin.register(TagModels)
class ActivityModelAdmin(admin.ModelAdmin):
    list_per_page = 4  #: 每页显示条数

    actions_on_top: True  # 操作是否在上面显示, 默认  True  ,反正两个相反
    actions_on_bottom: True  # 操作是否在下面显示, 默认   False

    # 自定义显示列，在models类中对字段有方法的就填方法名
    list_display = ['id', 'tagname', 'parent']

    # 设置在列表页字段上添加一个 a标签, 从而进入到编辑页面,在models类中对字段有方法的就填方法名
    list_display_links = ['id', 'tagname', 'parent']

    # 列表右侧栏过滤器,只能写一个
    list_filter = ['tagname']

    # 搜索框,搜索字段 也只能写一个
    search_fields = ['tagname']





# 文章
@admin.register(ArticleModels)
class ActivityModelAdmin(admin.ModelAdmin):
    list_per_page = 4  #: 每页显示条数

    actions_on_top: True  # 操作是否在上面显示, 默认  True  ,反正两个相反
    actions_on_bottom: True  # 操作是否在下面显示, 默认   False

    # 自定义显示列，在models类中对字段有方法的就填方法名
    list_display = ['id', 'articletitle', 'tagid', 'author','articlecontent']

    # 设置在列表页字段上添加一个 a标签, 从而进入到编辑页面,在models类中对字段有方法的就填方法名
    list_display_links = ['id', 'articletitle', 'tagid', 'author','articlecontent']

    # 列表右侧栏过滤器,只能写一个
    list_filter = ['articletitle']

    # 搜索框,搜索字段 也只能写一个
    search_fields = ['articletitle']
