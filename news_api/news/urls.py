from django.urls import path

from .views import (ArticleDetailApiView,
                    ArticleListCreateApiView,
                    JournalistListCreateAPIView)


urlpatterns = [
    path('articles/',
         ArticleListCreateApiView.as_view(),
         name="article-list"),

    path('articles/<int:pk>',
         ArticleDetailApiView.as_view(),
         name="article-detail"),

    path('journalists/',
         JournalistListCreateAPIView.as_view(),
         name="journalist_list"),
]
