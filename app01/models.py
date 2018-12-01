from django.db import models

# Create your models here.


# 用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增ID列作为主键
    num = models.CharField(max_length=24)  # varchar(32)
    pwd = models.CharField(max_length=16)  # varchar(32)

    def __str__(self):
        return self.num


# 出版社表
class Press(models.Model):
    id = models.AutoField(primary_key=True) # id主键
    name = models.CharField(max_length=32)  # 出版社名称

    def __str__(self):
        return '<这是一个出版社对象，它的名字是:{}>'.format(self.name)
        # return self.name


# 书籍数据表
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增id
    title = models.CharField(max_length=30)  # 书名
    # price = models.IntegerField()  # 价格
    # django 1.11 默认就是级联删除，Django2.0 必须加(on_delete=models.CASCADE)
    # to 表示关联的表名
    press = models.ForeignKey(to='Press',on_delete=models.CASCADE)


# 作者数据表
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)  # 作者名字
    # 方法二  ORM创建第三张表
    books = models.ManyToManyField(to='Book')  # 只是ORM层面建立的多多关系，不是作者表的字段

    def __str__(self):
        return self.name

# 方法一  自己创建第三张表
# 创建作者和书籍的关系表
# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     # 外键关系
#     author = models.ForeignKey(to='Author',on_delete=models.CASCADE)
#     book = models.ForeignKey(to='Book',on_delete=models.CASCADE)




















