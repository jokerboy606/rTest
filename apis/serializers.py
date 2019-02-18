from rest_framework import serializers
from rfolder.models import Question,Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields= '__all__'

# 