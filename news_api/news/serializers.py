from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer()

    class Meta:
        model = Article
        exclude = ("id",)

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)

        return time_delta

    def validate(self, data):
        """
        Check that description and title are different.
        """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must " \
                                              "be different from one another")

        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("Title must be at least 60 " \
                                              "characters long")

        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name="article-detail")
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"