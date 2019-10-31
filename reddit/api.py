from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
import coreapi
import praw


class NewsList(APIView):
    schema = ManualSchema(fields=[
        coreapi.Field('query', description='search by this value')
    ])

    # Separate title and url from the entire dictionary and
    def parse_news(self, news):
        response_list = []
        for article in news.children:
            response_list.append(
                {
                    "headline": article.title,
                    "link": article.url,
                    "source": 'reddit'
                }
            )
        return response_list

    def get(self, request):
        """
           List all news from reddit or search by query
           :param request:
           :return:
       """
        reddit = praw.Reddit(
            'user',  # user defined in praw.ini
            user_agent='hadi user agent'
        )

        query = request.GET.get("query")
        if query:

            params = {
                'q': query
            }
            response = reddit.get('/search', params)
        else:
            response = reddit.get('/new')
        return Response(self.parse_news(response))
