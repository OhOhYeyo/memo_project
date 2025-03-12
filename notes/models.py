from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)  # 글자 수 제한 O
    context = models.TextField()  # 글자 수 제한 X
    create_at = models.DateTimeField(auto_now_add=True)  # 현재 시간

    def __str__(self):
        return self.title
