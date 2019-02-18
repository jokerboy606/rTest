from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rfolder.models import Question
from rfolder.models import Choice

from apis.serializers import QuestionSerializer

class  QuestionList(generics.ListCreateAPIView):
    queryset= Question.objects.all()
    serializer_class = QuestionSerializer

