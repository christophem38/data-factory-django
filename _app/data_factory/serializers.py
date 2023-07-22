from rest_framework import serializers
from .models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['user', 'query', 'result', 'to']
        read_only_fields = ['result']
