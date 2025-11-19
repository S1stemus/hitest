from service_objects.services import ServiceWithResult
from django import forms
from models.models import Answer, User
from service_objects.fields import ModelField
from service_objects.errors import NotFound

class DeleteAnswerService(ServiceWithResult):
    answer_id = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User)
    custom_validations = ["_validate_answer_id", "_validate_user"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._delete
        return self
    @property
    def _delete(self):
        answer = Answer.objects.filter(id=self.cleaned_data["answer_id"])
        answer.delete()
        return self
    def _validate_answer_id(self):
        if not Answer.objects.filter(id=self.cleaned_data["answer_id"]).exists():
            self.add_error("answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['answer_id']} не найден"))
    def _validate_user(self):
        if self.cleaned_data["current_user"].id != Answer.objects.get(id=self.cleaned_data["answer_id"]).user.id:
            self.add_error("current_user", NotFound(message="Вы не можете удалять ответы других пользователей"))
