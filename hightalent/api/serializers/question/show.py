from models.models import Question
from rest_framework import serializers
from api.serializers.answer.show import AnswerShowSerializer

class QuestionShowSerializer(serializers.ModelSerializer):
    answers = AnswerShowSerializer(many=True)
    class Meta:
        model = Question
        fields = ['id','text','user', 'created_at', 'updated_at', 'answers']