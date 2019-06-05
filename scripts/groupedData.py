from django.db import connection

sql = """
 SELECT json_agg(grouped) as groupedArticles
 	FROM (SELECT json_agg(articles) as articles, 
				 COUNT(location) as articleCount,
				 location
				 FROM articles
				 GROUP BY location,
				 imagelink
				 HAVING
				 imagelink <> ''
				 AND
				 location <> '') as grouped;
"""

def run():
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
        print(type(data))
