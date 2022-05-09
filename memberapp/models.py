from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Test(models.Model):
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Test"

    def __str__(self):
        return self.verbose_name

SE = (('男', '男'), ('女', '女'))
GRADE = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))

class List(models.Model):
    class Meta:
        verbose_name = "リスト"
        verbose_name_plural = "リスト"

    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    listpk = models.CharField(verbose_name = 'listpk', max_length = 100)
    name = models.CharField(verbose_name = '氏名', max_length = 100)
    number = models.CharField(verbose_name = '学籍番号', max_length = 10)
    grade = models.CharField(verbose_name = '学年',max_length = 50, choices = GRADE)
    group = models.CharField(verbose_name = '所属', max_length = 100)
    se = models.CharField(verbose_name = '性別',max_length = 50, choices = SE)
    adre = models.CharField(verbose_name = '連絡先(gmail)', max_length = 100)
    content = models.TextField(verbose_name = '備考')

    def __str__(self):
        return self.name

class BList(models.Model):
    class Meta:
        verbose_name = "Bリスト"
        verbose_name_plural = "Bリスト"

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(verbose_name = 'タイトル', max_length = 100)
    content = models.CharField(verbose_name = '概要', max_length = 100)


