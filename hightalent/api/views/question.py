import re
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome
from api.services.question.list import ListQuestionService
from api.services.question.create import CreateQuestionService
from api.services.question.show import ShowQuestionService
from api.services.question.update import UpdateQuestionService
from api.services.question.delete import DeleteQuestionService
from api.serializers.question.list import QuestionListSerializer
from api.serializers.question.show import QuestionShowSerializer
from api.serializers.question.create import QuestionCreateSerializer
from api.serializers.question.update import QuestionUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class QuestionListAndPostView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Вопросы"],
        summary="Создает вопрос",
        description="Создает вопрос",
        responses={200: QuestionListSerializer},
        request=QuestionCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CreateQuestionService(), request.data | {"current_user": request.user})
        return Response(QuestionListSerializer(outcome.result).data, status=status.HTTP_201_CREATED)


    permission_classes = [AllowAny]
    @extend_schema(
        tags=["Вопросы"],
        summary="Возвращает список вопросов",
        description="Возвращает список вопросов",
        responses={200: QuestionListSerializer},
    )
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(ListQuestionService(),request.data)
        return Response(QuestionListSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK)
    
class QuestionShowView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        tags=["Вопросы"],
        summary="Возвращает вопрос по id c ответами на данный вопрос",
        description="Возвращает вопрос по id c ответами на данный вопрос",
        responses={200: QuestionShowSerializer},
    )
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(ShowQuestionService(), {"question_id": kwargs["id"]})
        return Response(QuestionShowSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK )

class QuestionUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Вопросы"],
        summary="Обновляет вопрос по id",
        description="Обновляет вопрос по id",
        responses={200: QuestionShowSerializer},
        request = QuestionUpdateSerializer,
    )
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            UpdateQuestionService,
            request.data|{"question_id": kwargs["id"], "current_user": request.user}
        )
        return Response(QuestionShowSerializer(outcome.result).data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=["Вопросы"],
        summary="Удаляет вопрос по id",
        description="Удаляет вопрос по id",
    )
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            DeleteQuestionService,
            {"question_id": kwargs["id"], "current_user": request.user}
        )
        return Response( status=status.HTTP_204_NO_CONTENT)
    

    

    