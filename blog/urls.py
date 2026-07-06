from django.urls import path
from blog.views import PostCreateAPIView, PostRetrieveUpdateDestroyAPIView, PostListView, AuthorRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(route="post/", view=PostCreateAPIView.as_view(), name="create-post-view"),
    path(route="post/<int:pk>", view=PostRetrieveUpdateDestroyAPIView.as_view(), name="detail-post-view"),
    path(route="posts/<int:pk>", view=PostListView.as_view(), name="list-post-view"),
    path(route="author/<int:pk>", view=AuthorRetrieveUpdateDestroyAPIView.as_view(), name="detail-author-view")
]