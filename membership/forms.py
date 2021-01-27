from datetime import date
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from membership.models import Membership, UserMembership, Subscription
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
      free_membership = Membership.objects.get(membership_type='Free')

class Meta(UserCreationForm.Meta):
         model = user
         def save(self):
            user = super().save(commit=False)
            user.save()

      # Creating a new UserMembership
            user_membership = UserMembership.objects.create(user=user, membership=self.free_membership)
            user_membership.save()

      # Creating a new UserSubscription
            user_subscription = Subscription()
            user_subscription.user_membership = user_membership
            user_subscription.save()
            return user