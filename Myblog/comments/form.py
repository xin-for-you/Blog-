#-*-coding:utf-8-*-
from django import forms                   #����
from .models import Comment               #�Դ�����ģ��
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']