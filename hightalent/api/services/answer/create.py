
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult
from django import forms
from models.models import Answer,Question,User
from service_objects.errors import NotFound



class CreateAnswerService(ServiceWithResult):

    text = forms.CharField(max_length=511)
    question_id = forms.IntegerField(required=True)
    current_user = ModelField(User)


    custom_validations = ["_validate_question_id"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self.create_answer
        return self
    @property
    def create_answer(self):
        answer = Answer.objects.create(text = self.cleaned_data["text"], question = Question.objects.get(id = self.cleaned_data["question_id"]), user = self.cleaned_data["current_user"])
        return answer
    
    def _validate_question_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))