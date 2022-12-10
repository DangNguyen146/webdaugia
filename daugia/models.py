from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MemberFee(models.Model):
    fee = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.fee


class BidderUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)
    membership = models.ForeignKey(
        MemberFee, on_delete=models.CASCADE, null=True)

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

    def __str__(self):
        return self.user.username
