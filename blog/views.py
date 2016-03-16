from django.shortcuts import render
from django.views import generic
from .models import Article
from django.http import HttpResponse


class IndexView(generic.ListView):
    queryset = Article.objects.order_by('-published_date')
    paginate_by = 5
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

class PostDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/post.html'
