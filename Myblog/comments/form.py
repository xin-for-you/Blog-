#-*-coding:utf-8-*-
from django import forms                   #表单类
from .models import Comment               #自带评论模块
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']