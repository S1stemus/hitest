from django.urls import path
from api.views.answer import AnswerShowView, AnswerCreateView, AnswerUpdateDeleteView
from api.views.question import QuestionShowView, QuestionListAndPostView, QuestionUpdateDeleteView
from api.views.user import RegisterUserView, UserShowView


urlpatterns = [
    path("users/register/", RegisterUserView.as_view(), name="register"),
    path("users/<int:id>/", UserShowView.as_view(), name="users"),
    path("questions/", QuestionListAndPostView.as_view(), name="questions"),
    path("question/<int:id>/", QuestionShowView.as_view(), name="question"),
    path("questions/<int:id>/", QuestionUpdateDeleteView.as_view(), name="question"),
    path("answers/", AnswerCreateView.as_view(), name="answers"),
    path("answer/<int:id>/", AnswerShowView.as_view(), name="answer"),
    path("answers/<int:id>/", AnswerUpdateDeleteView.as_view(), name="answer"),
    
]