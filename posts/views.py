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
    paginate_by = 4
