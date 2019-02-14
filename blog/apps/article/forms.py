from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from article.models import ArticleModels


class SummernoteForm(forms.ModelForm):
    tagid = forms.IntegerField()
    editordata = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = ArticleModels
        fields = ['articletitle']
        widgets = {
            'editordata': SummernoteInplaceWidget(),
        }
