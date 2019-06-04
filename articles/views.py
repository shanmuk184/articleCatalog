from django.shortcuts import render
from .serializers import ArticleSerializer
from rest_framework import viewsets
from .models import Article
from django.db.models import Q
from django.contrib.postgres.aggregates import ArrayAgg
# Create your views here.

class ArticleViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(~Q(imagelink = ""))

class AggregationViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.aggregate(ids=ArrayAgg('location'), )