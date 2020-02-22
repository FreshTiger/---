from django.db import models

# Create your models here.


class GoodsInfo(models.Model):
    goodsID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to="Home/GoodsP")
    price = models.IntegerField()
    introduce = models.TextField(null=True)
    sale = models.IntegerField(null=True)
    stroe = models.IntegerField(null=True)
    brand = models.ForeignKey(
        "brand", to_field='brandID', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class brand(models.Model):
    brandID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class user(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=32)
    avatar = models.ImageField(upload_to='Home/avatar')
    sex = models.CharField(max_length=32)
    password = models.TextField()
    name = models.CharField(max_length=32)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class message(models.Model):
    messageID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(
        'user', to_field="userID", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class notice(models.Model):
    noticeID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class order(models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.ForeignKey('user',to_field='userID',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    price = models.IntegerField()

class orderList(models.Model):
    ID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey('order',to_field='orderID',on_delete=models.CASCADE)
