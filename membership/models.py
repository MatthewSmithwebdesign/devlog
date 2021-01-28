from django.db import models
from django.conf import settings

# Create your models here.

MEMBERSHIP_CHOICES = (("pre", "Premium"), ("free", "Free"))


class Membership(models.Model):
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, default="Free", max_length=7
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.membership_type


# this points to the user then the membership points to the defined model above


class UserMembership(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="users_user", on_delete=models.CASCADE
    )
    membership = models.ForeignKey(
        Membership, related_name="user_membership", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.user.username


# subscrition model the boolean checks to see if the user is subbed


class Subscription(models.Model):
    user_membership = models.ForeignKey(
        UserMembership, related_name="subscription", on_delete=models.CASCADE
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
