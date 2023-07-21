from rest_framework import viewsets
from .serializers import (
    TranslationSerializer,
)
from .models import Translation
import os
import openai


class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def perform_create(self, serializer):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f'Translate the following English text to French: "{self.request.data["query"]}"',
            max_tokens=60,
        )
        res = response.choices[0].text.strip()
        print(f'Translation : {res}')

        return serializer.save(
            query=self.request.data["query"], result=res, user=self.request.user
        )

    def get_queryset(self):
        return Translation.objects.filter(user=self.request.user)
