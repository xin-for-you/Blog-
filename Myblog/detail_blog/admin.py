from django.contrib import admin
# �û��� jgx      ����jgx182
# Register your models here.
from .models import Post, Category, Tag  # ������

#������ʾ������
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modify_time', 'category', 'author']
# ��models�д����������ע��

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
