from django.urls import path

from . import views
from .views import PostListView, TopicListView

urlpatterns = [
    path("", views.PostListView.as_view(), name='posts'),
    path("<str:pk>/", views.TopicListView.as_view(), name='topic'),
]

