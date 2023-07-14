from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Task(models.Model):
    text = models.TextField(
        'Текст поста'
    )
    # pub_date = models.DateTimeField(
    #     'Дата публикации',
    #     auto_now_add=True,
    # )
    # owner = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name