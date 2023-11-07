from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api.views import NumberViewSet, get_aggregated_data, get_random_number

router = routers.DefaultRouter()
router.register('number', NumberViewSet, basename='number')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema',
        ),
        name='swagger-ui',
    ),
    path('get_aggregated_data/', get_aggregated_data),
    path('get_random_number/', get_random_number),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]
