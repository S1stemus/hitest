from service_objects.services import ServiceWithResult
from django import forms
from models.models import Answer
from service_objects.errors import NotFound

class AnswerShowService(ServiceWithResult):
    answer_id = forms.IntegerField(required=True, min_value=1)
    custom_validations = ["_validate_answer_id"]
    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.answer
        return self

    @property
    def _answer(self):
        return Answer.objects.get(id=self.cleaned_data["answer_id"])
    
    def _validate_answer_id(self):
        if not Answer.objects.filter(id=self.cleaned_data["answer_id"]).exists():
            self.add_error("answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['answer_id']} не найден"))
            