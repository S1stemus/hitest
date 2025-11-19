from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome
from api.services.answer.show import AnswerShowService
from api.services.answer.create import CreateAnswerService
from api.services.answer.update import UpdateAnswerService
from api.services.answer.delete import DeleteAnswerService
from api.serializers.answer.show import AnswerShowSerializer
from api.serializers.answer.update import AnswerUpdateSerializer
from api.serializers.answer.create import AnswerCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class AnswerUpdateDeleteView(APIView):
    [IsAuthenticated]
    @extend_schema(
        tags=["Ответы"],
        summary="Обновляет ответ по id",
        description="Обновляет ответ по id",
        responses={200: AnswerShowSerializer},
        request=AnswerUpdateSerializer
    )
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UpdateAnswerService, request.data|{"answer_id": kwargs["id"], "current_user": request.user})
        return Response(AnswerShowSerializer(outcome.result).data, status=status.HTTP_200_OK)
    @extend_schema(
        tags=["Ответы"],
        summary="Удаляет ответ по id",
        description="Удаляет ответ по id",
        responses={204: AnswerShowSerializer},
    )
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(DeleteAnswerService, {"answer_id": kwargs["id"], "current_user": request.user})
        return Response(status=status.HTTP_204_NO_CONTENT)
class AnswerCreateView(APIView):
    [IsAuthenticated]
    @extend_schema(
        tags=["Ответы"],
        summary="Создает ответ",
        description="Создает ответ",
        responses={201: AnswerShowSerializer},
        request=AnswerCreateSerializer
    )
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CreateAnswerService, request.data|{"current_user": request.user})
        return Response(AnswerShowSerializer(outcome.result).data, status=status.HTTP_201_CREATED)
class AnswerShowView(APIView):
    [AllowAny]
    @extend_schema(
        tags=["Ответы"],
        summary="Возвращает ответ по id",
        description="Возвращает ответ по id",
        responses={200: AnswerShowSerializer},
    )
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(AnswerShowService, {"answer_id": kwargs["id"]})
        return Response(AnswerShowSerializer(outcome.result).data, status=status.HTTP_200_OK)
