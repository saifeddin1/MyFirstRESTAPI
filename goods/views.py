from django.shortcuts import render
from .models import Good
from .serializers import GoodSerializer
from rest_framework import viewsets

# Create your views here.


class GoodView(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

