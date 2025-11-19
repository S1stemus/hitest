
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult
from django import forms
from models.models import Question,User
from service_objects.errors import NotFound


class CreateQuestionService(ServiceWithResult):
    text = forms.CharField(max_length=255, required=True)
    current_user = ModelField(User, required=True)

    def process(self):
        question = Question.objects.create(text=self.cleaned_data["text"], user=self.cleaned_data["current_user"])
        self.result = question
        return self