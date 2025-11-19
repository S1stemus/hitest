# hitest
тестовое задание для Хайталент

# Models
1. ## Answer
    ```python
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
    ```
1. ## Question
    ```python
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
    ```
1. ## User
    ```python
    
    ```
# API
1. ## Answers
2. ## Question
3. ## User

# Как запустить
1. ## Скачать репозиторий
    
    ```bash
    git clone https://github.com/S1stemus/hitest
    ```
2. ## Перейти в папку репозитория cd 
    ```bash
    cd hitest
    ```    
3. ## Выполнить команду
    ```bash
     sudo docker compose up
    ``` 