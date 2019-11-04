from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    headline = serializers.CharField(max_length=100)
    link = serializers.CharField(max_length=100)
    source = serializers.CharField(max_length=100)
