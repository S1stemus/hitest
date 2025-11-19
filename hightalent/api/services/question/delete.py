from service_objects.services import ServiceWithResult
from django import forms
from models.models import Question, User
from service_objects.fields import ModelField
from service_objects.errors import NotFound

class DeleteQuestionService(ServiceWithResult):
    question_id = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User)

    custom_validations = ["_validate_question_id", "_validate_user"]
    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._delete
        return self
        
    @property
    def _delete(self):
        question = Question.objects.filter(id=self.cleaned_data["question_id"])
        question.delete()
        return self
    def _validate_question_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))
    def _validate_user(self):
        if self.cleaned_data["current_user"].id != Question.objects.get(id=self.cleaned_data["question_id"]).user.id:
            self.add_error("current_user", NotFound(message="Вы не можете удалять вопросы других пользователей"))