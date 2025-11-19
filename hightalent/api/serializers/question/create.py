from models.models import Question
from rest_framework import serializers

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["text"]