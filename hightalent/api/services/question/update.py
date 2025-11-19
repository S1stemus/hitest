from service_objects.services import ServiceWithResult
from django import forms
from models.models import Question, User
from service_objects.errors import NotFound
from service_objects.fields import ModelField

class UpdateQuestionService(ServiceWithResult):
    question_id = forms.IntegerField()
    text = forms.CharField(max_length=511, required=True)
    current_user = ModelField(User, required=True) 

    custom_validations = ["_validate_answer_id", "_validate_user"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update_answer
        return self
        
    @property
    def _update_answer(self):
        question = Question.objects.get(id=self.cleaned_data["question_id"])
        question.text = self.cleaned_data["text"]
        question.save()
        return question


    def _validate_answer_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))
    def _validate_user(self):
        if self.cleaned_data["current_user"].id != Question.objects.get(id=self.cleaned_data["question_id"]).user.id:
            self.add_error("current_user", NotFound(message="Вы не можете менять вопросы других пользователей"))