from django.forms import model_to_dict
from django.shortcuts import render

from django_filters import rest_framework
from rest_framework import generics, status, response, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *


class PerevalViewset(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    @action(methods=['get'], detail=False)
    def userdetail(self, request):
        obj = Pereval.objects.values().all()
        return Response({'user_posts': [(p['title'],p['beauty_title']) for p in obj]})

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=False)
    #     try:
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     except:
    #         return Response({'status': '400-Bad Request'})
    #     if serializer.is_valid:
    #         pk = Pereval.objects.values().last()['id']
    #         return Response({'status': '200-успех', 'mesage': 'Отправлено успешно', "id": str(pk)})



