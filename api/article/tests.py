from django.urls import resolve
from .views import ArticleListCreateView
from django.test import TestCase
from django.urls import reverse
from .models import Article
from rest_framework import status
from rest_framework.test import APIClient


class ArticleModelTest(TestCase):

    def setUp(self):
        Article.objects.create(
            title='Test Article',
            content='This is a test article content',
            author='Test Author',
            date='2023-11-12',
            image=None,
            links=None
        )

    def test_article_creation(self):
        article = Article.objects.get(title='Test Article')
        self.assertTrue(isinstance(article, Article))
        self.assertEqual(article.__str__(), article.title)


class ArticleViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.article = Article.objects.create(
            title='Another Test Article',
            content='Content for another article',
            author='Another Author',
            date='2023-11-12'
        )
        self.list_url = reverse('articles')
        self.detail_url = reverse(
            'article-detail', kwargs={'pk': self.article.pk})

    def test_get_all_articles(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_article(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_article(self):
        response = self.client.get(
            reverse('article-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Add tests for POST, DELETE as needed


class URLTest(TestCase):

    def test_article_list_url_resolves(self):
        url = reverse('articles')
        self.assertEqual(resolve(url).func.view_class, ArticleListCreateView)

    def test_article_detail_url_resolves(self):
        url = reverse('article-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ArticleListCreateView)
