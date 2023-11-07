from rest_framework import serializers

from number.models import AggregatedNumber, Number, NumberMoreNine


class NumberSerializer(serializers.ModelSerializer):
    '''Сериализатор модели `Числа`.'''

    class Meta:
        model = Number
        fields = ('id', 'time', 'value')


class NumberMoreNineSerializer(serializers.ModelSerializer):
    '''Сериализатор модели `Числа более 9`.'''

    class Meta:
        model = NumberMoreNine
        fields = ('id', 'time', 'value_more_nine')


class AggregatedNumberSerializer(serializers.ModelSerializer):
    '''Сериализатор представления данных `Поминутно агрегированные числа`.'''

    class Meta:
        model = AggregatedNumber
        fields = ('time_minute', 'avg_value')
