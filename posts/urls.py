from django.urls import path
from posts import views
# from .views import HomePageView, AboutPageView


urlpatterns = [
    path("list", views.PostListView.as_view(), name="list"),
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreateView.as_view(), name="new"),
]

