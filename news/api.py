from newsapi import NewsApiClient
from rest_framework.response import Response
from NewsAggregator.settings import NEWS_API_SECRET_KEY
from rest_framework.views import APIView
from rest_framework.schemas import ManualSchema
import coreapi


class NewsList(APIView):
    schema = ManualSchema(fields=[
        coreapi.Field('query', description='search by this value')
    ])
    news_api = NewsApiClient(api_key=NEWS_API_SECRET_KEY)

    # Separate title and url from the entire dictionary and
    def parse_news(self, news):
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

    def get(self, request):
        """
        List all news from NewsApi or search by query
        :param request:
        :return:
        """

        qurey = request.GET.get('query', '')
        top_headlines = self.news_api.get_top_headlines(
            q=qurey)  # if query is None news_api get_top_headlines returns the whole news
        return Response(self.parse_news(top_headlines))
