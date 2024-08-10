from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
)
from .models import Post
# from django.urls import reverse


class PostListView(ListView):                           #scan
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):                       #read single
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):                       # create new records
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
    # success_url = reverse("list")

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"