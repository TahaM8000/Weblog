from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from . import models
from django.core.paginator import Paginator
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class PostListView(ListView):
    model = models.Post
    context_object_name = "Posts"
    template_name = "posts/classBaseViews/home.html"
    queryset = models.Post.objects.published()[::-1]
    paginate_by = 2


class PostDetail(DetailView):
    template_name = "posts/classBaseViews/Post_detail.html"
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(models.Post.objects.published(), slug=slug)


class AuthorDetail(ListView):
    paginate_by = 5
    template_name = "oldview/classview/Author_detail.html"

    def get_queryset(self):
        global Author
        slug = self.kwargs.get('slug')
        Author = User.objects.get(username=slug)
        return Author.posts.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Author'] = Author
        return context
