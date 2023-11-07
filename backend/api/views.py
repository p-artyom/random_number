import random

from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import AggregatedNumberSerializer, NumberSerializer
from number.models import AggregatedNumber, Number


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
    '''Представление модели `Числа`.'''

    queryset = Number.objects.all()
    serializer_class = NumberSerializer


@extend_schema(
    summary='Получить случайное число',
    description='Возвращает случайное число.',
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response={'example': {'value': 7.185094371302055}},
        ),
    },
)
@api_view(['GET'])
def get_random_number(request: Request) -> Response:
    '''Получить рандомное число.

    Returns:
        HttpResponse, который содержит случайное число в диапазоне от 0 до 10.
    '''

    serializer = NumberSerializer(data={'value': random.uniform(0, 10)})
    serializer.is_valid(raise_exception=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@extend_schema(
    summary='Получить поминутно агрегированные данные модели `Числа`',
    description=('Возвращает поминутно агрегированные данные модели `Числа`.'),
    responses=AggregatedNumberSerializer,
)
@api_view(['GET'])
def get_aggregated_data(request: Request) -> Response:
    '''Получить данные представления `Поминутно агрегированные числа`.

    Returns:
        HttpResponse, который содержит данные представления `Поминутно
        агрегированные числа`, представляющее собой поминутно агрегированные
        данные модели `Числа`.
    '''

    return Response(
        AggregatedNumberSerializer(
            AggregatedNumber.objects.all(), many=True
        ).data,
        status=status.HTTP_200_OK,
    )
