from django.shortcuts import render
# from .serializers import ArticleSerializer
from rest_framework import viewsets
from django.views import View
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db.models.aggregates import Count
from django.contrib.postgres.search import SearchVector
from .handlers import Handlers
import json
from django.shortcuts import HttpResponse




# Create your views here
class ArticleView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        query = request.GET['query']
        # body = json.loads(query)

        if query:
            return HttpResponse(json.dumps(Handlers.createFilteredResponse(query)))

        groupedData = Handlers.groupedarticleHandler()
        return HttpResponse(json.dumps(groupedData[0][0]))

