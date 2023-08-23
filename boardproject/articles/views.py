# articles/views.py

from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)