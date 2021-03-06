from django.shortcuts import render


from django.views.generic import ListView
from membership.models import Membership, UserMembership, Subscription

# Create your views here.


class MembershipView(ListView):
    model = Membership
    template_name = "memberships/list.html"

    def get_user_membership(self, request):
        user_membership_qs = UserMembership.objects.filter(user=self.request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first()
        return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = self.get_user_membership(self.request)
        return context
