groupedArticles = """
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
				 location <> '' 
				 ORDER BY articleCount DESC
				 ) as grouped;
"""
