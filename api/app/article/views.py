from rest_framework import generics, status
from django.core.paginator import Paginator
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            # Handle detail view
            try:
                article = Article.objects.get(pk=kwargs['pk'])
            except Article.DoesNotExist:
                raise Http404

            serializer = self.serializer_class(article)
            return Response(serializer.data)

        else:
            # get limit from request, use 10 as a default if it's not provided
            limit = int(request.GET.get('limit', default=10))
            # get all articles from your database, ordered from new to old
            all_articles = Article.objects.all().order_by('-created_at')

            # paginate them using the limit
            paginator = Paginator(all_articles, limit)

            # get the page
            page = request.GET.get('page', default=1)
            # Use get_page to automatically handle invalid page numbers
            articles = paginator.get_page(page)

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

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        try:
            # Assuming that the ID of the article to be deleted is provided in the URL
            article = Article.objects.get(pk=kwargs['pk'])
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            raise Http404
