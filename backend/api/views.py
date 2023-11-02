import random

from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import NumberSerializer
from number.models import Number


@extend_schema_view(
    list=extend_schema(
        summary='Получить список чисел',
        description=('Возвращает список чисел.'),
    ),
    retrieve=extend_schema(
        summary='Получить данные конкретного числа',
        description=('Возвращает данные конкретного числа.'),
    ),
)
class NumberViewSet(ReadOnlyModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer


@extend_schema(
    summary='Получить случайное число',
    description=('Возвращает случайное число.'),
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response={'example': {'value': 7.185094371302055}},
        ),
    },
)
@api_view(['GET'])
def get_random_number(request):
    serializer = NumberSerializer(data={'value': random.uniform(0, 10)})
    serializer.is_valid(raise_exception=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )
