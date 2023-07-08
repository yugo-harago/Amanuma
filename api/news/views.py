from rest_framework import generics, status
from django.core.paginator import Paginator
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        # get limit from request, use 10 as a default if it's not provided
        limit = request.GET.get('limit', default=10)
        all_articles = Article.objects.all()  # get all articles from your database
        # paginate them using the limit
        paginator = Paginator(all_articles, limit)

        # get the page
        page = request.GET.get('page', default=1)
        articles = paginator.page(page)

        # serialize the articles
        serializer = ArticleSerializer(articles, many=True)

        # return serialized data
        return Response(serializer.data)

    # TODO: Make secure
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
