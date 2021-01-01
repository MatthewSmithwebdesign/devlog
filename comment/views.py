from .models import BlogPost
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

class post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(BlogPost, slog=slug)
    comments = post.comments.filter(active=True)
    new_COMMENT = None
    #Posted Comment
    if request.method == 'POST':
        comment_form = CommentForm(data=requested.POST)
        if comment_form.is_valid():
            # unsaved created comment
            new_comment = comment_form.save(commit=False)
            #attaching comment to posts
            new_comment.post = post
            # save to the database
            new_comment.save()
        else:
           comment_form = CommentForm()

          return render(request, template_name, {'post': post,
                                               'comments': comments,
                                               'new_comment': new_comment,
                                               'comment_form': comment_form })
