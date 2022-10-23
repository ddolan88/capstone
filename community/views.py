from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.urls import reverse_lazy
from .models import Post


# Create your views here.
class CommunityPageView(ListView):  #this will be the list view for the community
    template_name = 'pages/community.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields= ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('community_posts')

    def test_func(self):
        obj= self.get_object()
        return obj.author == self.request.user
        

