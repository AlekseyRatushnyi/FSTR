from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from core.views import PerevalViewset #PerevalAPIList, PerevalAPIUpdate,PerevalAPIDetailView

router = routers.DefaultRouter()
router.register(r'submitData', PerevalViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]