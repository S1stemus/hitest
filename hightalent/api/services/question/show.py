from service_objects.services import ServiceWithResult
from django import forms
from models.models import Question
from service_objects.errors import NotFound


class ShowQuestionService(ServiceWithResult):
    question_id = forms.IntegerField()
    custom_validations = ["_validate_question_id"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._question
        return self

    @property
    def _question(self):
        return Question.objects.filter(id=self.cleaned_data["question_id"]).prefetch_related("answers")

    def _validate_question_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))