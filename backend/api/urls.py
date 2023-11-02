from django.urls import include, path
from rest_framework import routers

from api.views import NumberViewSet, get_random_number

router = routers.DefaultRouter()
router.register('number', NumberViewSet, basename='number')

urlpatterns = [
    path('', include(router.urls)),
    path('get_random_number/', get_random_number),
]
