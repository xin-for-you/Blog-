#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
from django.db import models
from django.utils.six import python_2_unicode_compatible
# ����Ӧ�� �����ݿ���������

python_2_unicode_compatible # װ�������ڼ��� Python2
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('detail_blog.Post',on_delete=models.CASCADE)
    def __str__(self):
        return self.text[:20]