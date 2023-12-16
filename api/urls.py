from django.urls import path
from .views import PostListView, PostDetailAPIView

urlpatterns = [
    path('posts', PostListView.as_view()),
    path('categories/<int:pk>', PostDetailAPIView.as_view())
]
