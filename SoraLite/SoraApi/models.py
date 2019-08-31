from django.db import models

class Baigeng(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    # id = models.AutoField() id是自动生成的
    # An IntegerField that automatically increments according to available IDs.
    # You usually won’t need to use this directly;
    # a primary key field will automatically be added to your model if you don’t specify otherwise
    name = models.CharField(max_length=100)
    content = models.TextField()
    use = models.BooleanField()
    modified_time = models.DateField(auto_now=True)
    created_time = models.DateField(auto_now_add=True)
    creator = models.CharField(max_length=100)
    contact_creator = models.CharField(max_length=100, blank=True)
    related_person = models.CharField(max_length=200)
    type = models.CharField(max_length=10, default=None, blank=True)
    source = models.CharField(max_length=100, default=None, blank=True)
    rank = models.IntegerField()
    rank_num = models.IntegerField()


    def __str__(self):
        return self.name

# Create your models here.
