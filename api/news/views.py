from rest_framework import generics, status
from django.core.paginator import Paginator
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        # get limit from request, use 10 as a default if it's not provided
        limit = int(request.GET.get('limit', default=10))
        # get all articles from your database, ordered from new to old
        all_articles = News.objects.all().order_by('-created_at')

        # paginate them using the limit
        paginator = Paginator(all_articles, limit)

        # get the page
        page = request.GET.get('page', default=1)
        # Use get_page to automatically handle invalid page numbers
        news_list = paginator.get_page(page)

        # serialize the articles
        serializer = NewsSerializer(news_list, many=True)

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
            news = News.objects.get(pk=kwargs['pk'])
            news.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except News.DoesNotExist:
            raise Http404
