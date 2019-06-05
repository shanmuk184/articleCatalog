from django.db import connection
from .queries.queries import groupedArticles
from django.contrib.postgres.search import SearchVector
from .models import Article

class Handlers():
    @staticmethod
    def groupedarticleHandler():
        with connection.cursor() as cursor:
            cursor.execute(groupedArticles)
            data = cursor.fetchall()
            return data

    @staticmethod
    def createFilteredResponse(body):
        articleResult = Article.objects.annotate(
            search=SearchVector('job_title',
                                'location', 'houseof'), ).filter(search=body.get('query'))
        result = {}
        result['articles'] = list(articleResult.values())
        result['count'] = articleResult.count()
        return result
