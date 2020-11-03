from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save


class UserData(AbstractUser):
    USER_TYPE = ((1, "Vendor"), (2, "Bidder"))
    user_type = models.IntegerField(choices=USER_TYPE, default=1)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


