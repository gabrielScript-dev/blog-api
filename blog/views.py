from blog.models import Post, Author
from blog.serializers import PostSerializer, AuthorSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author
    serializer_class = AuthorSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post
    serializer_class = PostSerializer


class PostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):

        author_id = self.kwargs['pk']
        return Post.objects.filter(author=author_id)