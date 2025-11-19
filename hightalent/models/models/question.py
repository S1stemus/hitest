
from django.db import models


class Question(models.Model):
    text = models.TextField(
        max_length=255,
        verbose_name='Текст вопроса',
        null = False,
        blank = False        
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        verbose_name='Создатель вопроса',
        null = False,
        blank = False
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        db_table = 'questions'