from django.views.generic import (
    TemplateView,
    DetailView,
    # ListView
)
from django.views.generic.edit import (
    CreateView,
    DeleteView
    # UpdateView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class CommunityPageView(TemplateView):
    template_name = 'pages/community.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin ,CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields= ['title', 'body']


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('community')


