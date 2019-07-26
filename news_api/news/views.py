from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Article, Journalist
from .serializers import ArticleSerializer, JournalistSerializer


class ArticleListCreateApiView(APIView):
    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailApiView(APIView):
    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)

        return article

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)

        return Response(serializer.data)

    def patch(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistListCreateAPIView(APIView):
    def get(self, request):
        journalist = Journalist.objects.all()
        serializer = JournalistSerializer(journalist,
                                          many=True, 
                                          context={"request": request})

        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)