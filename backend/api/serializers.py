from rest_framework import serializers

from number.models import Number


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ('id', 'time', 'value')
