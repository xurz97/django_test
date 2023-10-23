from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']
 
class TestModel(models.Model):
    SELVALUE = (
        ('标题', 'first'), #前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('内容', 'second'),
        ('作者', 'third'),
    )
    select_value = models.CharField(max_length=10, choices=SELVALUE)


