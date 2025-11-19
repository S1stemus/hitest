from models.models import Answer
from rest_framework import serializers

class AnswerCreateSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField()
    class Meta:
        model = Answer
        fields = ["text","question_id"]