from django.utils import timezone
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from feed.models import BlogPost
from .forms import CommentForm
from .models import Comment

# Create your views here.


class PostDetail(DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(
            blogpost_connected=self.get_object()
        ).order_by("date_posted")
        data["comments"] = comments_connected
        data["comment_form"] = CommentForm()
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            body=request.POST.get("body"),
            name=request.POST.get("name"),
            post_connected=self.get_object(),
        )
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
