from rest_framework import serializers
from .models import Good


class GoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Good
        fields = ('url', 'id', 'name', 'description')
