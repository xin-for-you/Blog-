#-*-coding:utf-8-*- 
from django import template
from ..models import Post , Category ,Tag

register = template.Library()  # 注册为模板
#最新文章目录
@register.simple_tag     #这个装饰器是注册为模板的意思
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]
#归档文章目录
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')
#分类文章目录
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()
@register.simple_tag
def tags():
    return Tag.objects.all()