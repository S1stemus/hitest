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
    class User(AbstractUser):
        class Meta:
            db_table = "users"
            verbose_name_plural = "Пользователи"
            verbose_name = "Пользователь"
    ```
# API
1. ## Answers
    1. ## GET http://127.0.0.1:8000/api/answer/<int:id>/
        получает ответ по  id. 
    2. ## POST http://127.0.0.1:8000/api/answers/<int:id>/
        Создает ответ на определенный ответ. Требует JWT-токен. Нельзя создать при несуществующем id  вопроса
    3. ## DELETE http://127.0.0.1:8000/api/answers/<int:id>
        Удаляет ответ по id. Требует  JWT-токен. Нельзя удалить ответ которого нет, а так же ответ , который не принадлежит этому пользователю.
    4. ## UPDATE http://127.0.0.1:8000/api/answers/
        Меняет ответ по id. Требует  JWT-токен. Нельзя изменить ответ которого нет, а так же ответ , который не принадлежит этому пользователю.
2. ## Question
    1. ## GET http://127.0.0.1:8000/api/question/<int:id>
        Возвращает вопрос по  id вместе совсеми ответами на него и подробной информацией о данном вопросе
    2. ## GET http://127.0.0.1:8000/api/questions
        Возвращает список вопросов
    3. ## POST http://127.0.0.1:8000/api/questions
        Создает вопрос. Требуется JWT-токен.
    4. ## DELETE http://127.0.0.1:8000/api/questions/<int:id>
        Удаляет вопрос вместе со всеми ответами на данный вопрос. Требуется JWT-токен. Нельзя удалить вопрос которого нет, а так же вопрос , который не принадлежит этому пользователю.
    5. ## UPDATE http://127.0.0.1:8000/api/questions/<int:id>
        Изменяет вопрос вместе со всеми ответами на данный вопрос. Требуется JWT-токен. Нельзя удалить вопрос которого нет, а так же вопрос , который не принадлежит этому пользователю.
3. ## User
    1. ## http://127.0.0.1:8000/api/users/register/
        эндпоинт создает нового пользователя возвращая access и refresh токены
    2. ## http://127.0.0.1:8000/api/users/<int:id>
        Возвращает пользователя по  id 
                
    3. ## http://127.0.0.1:8000/api/token/
        эндпоинт для получения токена возращает access и refresh токены

4. ## Swagger
    весь Api задокументирован в  swagge для более удобного тестирования

    ## http://127.0.0.1:8000/api/docs/#/
# Как запустить
1. ## Скачать репозиторий
    
    ```bash
    git clone https://github.com/S1stemus/hitest
    ```
2. ## Перейти в папку репозитория 
    ```bash
    cd hitest
    ```    
3. ## Выполнить команду
    ```bash
     sudo docker compose up
    ``` 