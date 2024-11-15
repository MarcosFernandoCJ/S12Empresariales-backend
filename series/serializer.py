from rest_framework import serializers

from .models import Serie, Category

class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Serie
        fields = ('id', 'name', 'realese_date', 'rating', 'cotegory')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'description')