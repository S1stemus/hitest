from models.models import Question
from rest_framework import serializers


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text','id']