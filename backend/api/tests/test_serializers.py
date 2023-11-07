import random

from django.conf import settings
from django.test import TestCase
from rest_framework.serializers import ModelSerializer

from api.serializers import NumberMoreNineSerializer, NumberSerializer
from number.models import Number, NumberMoreNine


def create_objects(
    serializers: ModelSerializer, field: str, value: float
) -> NumberSerializer | NumberMoreNineSerializer:
    '''Создать объект в модели.'''

    serializer = serializers(data={f'{field}': value})
    if serializer.is_valid():
        serializer.save()
    return serializer


class SerializersTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.value_over_ten = random.uniform(0, 10) + 10
        cls.value_from_zero_to_ten = random.uniform(0, 10)
        cls.value_less_nine = random.uniform(0, 9)
        cls.value_from_nine_to_ten = random.uniform(9, 10)

    def test_created_number_value_over_ten(self) -> None:
        '''Нельзя записать в модель `Числа` значение больше десяти.'''

        self.assertEqual(
            Number.objects.count(),
            settings.CHECK_ZERO_OBJECTS_FOR_TEST,
        )
        self.number = create_objects(
            NumberSerializer, 'value', self.value_over_ten
        )
        self.assertEqual(
            Number.objects.count(),
            settings.CHECK_ZERO_OBJECTS_FOR_TEST,
        )
        self.number = create_objects(
            NumberSerializer, 'value', self.value_from_zero_to_ten
        )
        self.assertEqual(
            Number.objects.count(),
            settings.CHECK_ONE_OBJECTS_FOR_TEST,
        )

    def test_created_number_more_nine_value_less_nine(self) -> None:
        '''Нельзя записать в модель `Числа более 9` значение меньше девяти.'''

        self.assertEqual(
            NumberMoreNine.objects.count(),
            settings.CHECK_ZERO_OBJECTS_FOR_TEST,
        )
        self.number_more_nine = create_objects(
            NumberMoreNineSerializer, 'value_more_nine', self.value_less_nine
        )
        self.assertEqual(
            NumberMoreNine.objects.count(),
            settings.CHECK_ZERO_OBJECTS_FOR_TEST,
        )
        self.number_more_nine = create_objects(
            NumberMoreNineSerializer,
            'value_more_nine',
            self.value_from_nine_to_ten,
        )
        self.assertEqual(
            NumberMoreNine.objects.count(),
            settings.CHECK_ONE_OBJECTS_FOR_TEST,
        )
