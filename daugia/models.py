from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MemberFee(models.Model):
    fee = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.fee


class MemberFeeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nameLog = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=2, null=True)
    money = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class BidderUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)
    membership = models.ForeignKey(
        MemberFee, on_delete=models.CASCADE, null=True)
    allMoney = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.user.username


class AuctionUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)
    membership = models.ForeignKey(
        MemberFee, on_delete=models.CASCADE, null=True)
    allMoney = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.user.username


class Status(models.Model):
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.status


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name+" "+self.category.name


class SessionDate(models.Model):
    date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.date


class Session_Time(models.Model):
    date = models.ForeignKey(SessionDate, on_delete=models.CASCADE, null=True)
    time = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.date.date+" "+self.time


class Status(models.Model):
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.status


class Product(models.Model):
    temp = models.IntegerField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    min_price = models.IntegerField(null=True)
    images = models.FileField(null=True)
    session = models.ForeignKey(
        Session_Time, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
