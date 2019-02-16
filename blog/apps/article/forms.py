from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from article.models import ArticleModels, Comment


# 发布帖子
class SummernoteForm(forms.ModelForm):
    tagid = forms.IntegerField()
    editordata = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = ArticleModels
        fields = ['articletitle']
        widgets = {
            'editordata': SummernoteInplaceWidget(),
        }


# 评论
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']