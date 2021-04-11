from django.urls import path

from .views import PostListView, AboutView

urlpatterns = [
    path("posts/", PostListView.as_view()),
    path("about/", AboutView.as_view())
]