# articles/urls.py

from django.urls import path
from .views import ArticleDetailView, ArticleListCreateView

urlpatterns = [
    path('', ArticleListCreateView.as_view(), name='article-list'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
