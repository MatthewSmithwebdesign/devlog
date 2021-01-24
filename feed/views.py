from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import generic
from advert.models import Advert
from .models import BlogPost
from comment.forms import CommentForm
from membership.models import Membership, UserMembership, Subscription


# Create your views here.

class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['form'] = CommentForm()
       context['advert'] = Advert.objects.first()
       return context 
    def dispatch(self, request, *args, **kwargs):
          if request.user.is_anonymous:
            return redirect('/accounts/login/')
          else:
            return super().dispatch(request, *args, **kwargs)
                    
      
                    