from django.db import models


class Answer(models.Model):
    text = models.TextField(
        max_length=511,
        verbose_name='Текст ответа',
        null=False,
        blank=False,       
    )
    user = models.ForeignKey(
        'User',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    question = models.ForeignKey(
        'Question',
        verbose_name='Вопрос',
        related_name='answers',
        related_query_name='answer',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        db_table = 'answers'
