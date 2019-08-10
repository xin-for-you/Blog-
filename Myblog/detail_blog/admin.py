from django.contrib import admin
# 用户名 jgx      密码jgx182
# Register your models here.
from .models import Post, Category, Tag  # 导入类

#定制显示的内容
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modify_time', 'category', 'author']
# 将models中创建的类进行注册

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
