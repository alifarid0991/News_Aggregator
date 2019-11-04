from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from .serializer import NewsSerializer
from .reddit import get_api_reddit
from .newsapi import get_api_news
import coreapi


class NewsList(ListAPIView):
    schema = ManualSchema(fields=[
        coreapi.Field('query', description='search by this value')
    ])

    def handle_exception(self, exc):
        return Response({
            "status_code": 500,
            "detail": str(exc),
        })

    def get_queryset(self):
        # return news from api_news and reddit
        query = self.request.query_params.get("query", "")
        return get_api_news(query) + \
               get_api_reddit(query)

    serializer_class = NewsSerializer
