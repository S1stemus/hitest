from service_objects.services import ServiceWithResult
from django import forms
from models.models import Question
from service_objects.errors import NotFound

class ListQuestionService(ServiceWithResult):
    
    def process(self):
        if self.is_valid():
            self.result = self._questions
        return self
    @property
    def _questions(self):
        try:
            return Question.objects.all()
        except Question.DoesNotExist:
            return None