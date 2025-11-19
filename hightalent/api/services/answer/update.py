from service_objects.services import ServiceWithResult
from django import forms
from models.models import Answer, User
from service_objects.errors import NotFound
from service_objects.fields import ModelField


class UpdateAnswerService(ServiceWithResult):
    answer_id = forms.IntegerField()
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
        answer = Answer.objects.get(id=self.cleaned_data["answer_id"])
        answer.text = self.cleaned_data["text"]
        answer.save()
        return answer


    def _validate_answer_id(self):
        if not Answer.objects.filter(id=self.cleaned_data["answer_id"]).exists():
            self.add_error("answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['answer_id']} не найден"))
    def _validate_user(self):
        if self.cleaned_data["current_user"].id != Answer.objects.get(id=self.cleaned_data["answer_id"]).user.id:
            self.add_error("current_user", NotFound(message="Вы не можете менять ответы других пользователей"))
            