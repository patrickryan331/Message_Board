from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
)
from .models import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/details.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
    

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"