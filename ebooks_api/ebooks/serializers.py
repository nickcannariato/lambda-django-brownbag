from rest_framework import serializers

from .models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('ebook',)


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = '__all__'
