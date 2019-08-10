#-*-coding:utf-8-*- 
from django import template
from ..models import Post , Category ,Tag

register = template.Library()  # ע��Ϊģ��
#��������Ŀ¼
@register.simple_tag     #���װ������ע��Ϊģ�����˼
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]
#�鵵����Ŀ¼
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')
#��������Ŀ¼
@register.simple_tag
def get_categories():
    # �������ڶ������� Category ��
    return Category.objects.all()
@register.simple_tag
def tags():
    return Tag.objects.all()