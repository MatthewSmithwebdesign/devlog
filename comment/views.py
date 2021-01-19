from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from feed.models import BlogPost
from .forms import CommentForm

# Create your views here.


class PostDetail(DetailView):
   

    def post(self, request, *args, **kwargs):
        template_name = "post_detail.html"
        http_method_names = ["get", "post"] 
        comments = post.comments.filter(active=True)
        #post = get_object_or_404(BlogPost, slug=slug)
        #print(kwargs)
         new_COMMENT = None
        # Posted Comment
        if request.method == "POST":
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # unsaved created comment
                new_comment = comment_form.save(commit=False)
                # attaching comment to posts
                new_comment.post = post
                # save to the database
                new_comment.save()

            else:
                comment_form = CommentForm()

                return render(
                    request,
                    template_name,
                    {
                        "post": post,
                        "comments": comments,
                        "new_comment": new_comment,
                        "comment_form": comment_form,
                    },
                )
