from rest_framework import serializers
from .models import Article
from django.db import connection
from .queries.queries import groupedArticles


def getCursor():
    with connection.cursor() as cursor:
        cursor.execute(groupedArticles)
        data = cursor.fetchall()
        return data

# class ArticleSerializer(serializers.ModelSerializer):
#
#
#     def getGroupedResponse(self):
#         with connection.cursor() as cursor:
#             cursor.execute(groupedArticles)
#             data = cursor.fetchall()
#             return data
#
#     groupedArticles = getGroupedResponse()
#
#     class Meta:
#         model=Article
#         fields = (groupedArticles)