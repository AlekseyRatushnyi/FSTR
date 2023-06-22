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

    def list(self, request, *args, **kwargs):
        user = request.GET.get('user__email')
        if user is None:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = Pereval.objects.filter(user__email=user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        if instance.status == 'new':
            self.perform_update(serializer)
            return Response({'state': 1, 'message': 'Запись успешно изменена'})
        else:
            return Response({'state': 0, 'message': 'Update is not allowed - status is not new'})







    @action(methods=['get'], detail=False)
    def userdetail(self, request):
        obj = Pereval.objects.values().all()
        return Response({'user_posts': [(p['title'],p['beauty_title']) for p in obj]})





