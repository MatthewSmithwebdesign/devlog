from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import generic
from advert.models import Advert
from .models import BlogPost
from comment.forms import CommentForm
from membership.models import Membership, UserMembership, Subscription
from comment.models import Comment

# Create your views here.



class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


class PostDetail(generic.DetailView):
    http_method_names = ["get", "post"]
    model = BlogPost
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["advert"] = Advert.objects.first()
        comments_connected = Comment.objects.filter(
            post=self.get_object()
        ).order_by("created_on")
        context["comments"] = comments_connected
        
        return context
        

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect("/accounts/login/")
        else:
            return super().dispatch(request, *args, **kwargs)

    
    
    
    
    def post(self, request, *args, **kwargs):
        
        new_comment = Comment(
            body=request.POST.get("body"),
            name=request.POST.get("name"),
            post=self.get_object(),
        )
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
