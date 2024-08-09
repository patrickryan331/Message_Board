from django.urls import path
from posts import views
# from views import HomePageView


urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    # path("", HomePageView.as_view(), name="home"),
]