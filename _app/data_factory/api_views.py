from .view_scripts import getReadableLang
from rest_framework import viewsets
from .serializers import (
    TranslationSerializer,
)
from .models import Translation
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def perform_create(self, serializer):
        data = self.request.data
        query = data['query']
        dest = data['to']
        dest_str = getReadableLang(dest)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f'Translate the following text to {dest_str}: "{query}"',
            max_tokens=300,
        )
        res = response.choices[0].text.strip()
        print(dest, dest_str, res)

        return serializer.save(
            query=self.request.data["query"], result=res, user=self.request.user
        )

    def get_queryset(self):
        return Translation.objects.filter(user=self.request.user)
