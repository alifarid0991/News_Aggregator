from newsapi import NewsApiClient
from NewsAggregator.settings import NEWS_API_SECRET_KEY

news_api = NewsApiClient(api_key=NEWS_API_SECRET_KEY)

def get_api_news(query):
    news = news_api.get_top_headlines(
        q=query)  # if query is None news is all the latest news, but if there was a query, would search and collect all the news tagged as that query
    response_list = []
    for article in news['articles']:
        response_list.append(
            {
                "headline": article['title'],
                "link": article['url'],
                "source": 'newsapi'
            }
        )
    return response_list
