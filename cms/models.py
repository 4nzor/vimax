from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Text(models.Model):
    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'

    title = models.CharField(max_length=200)
    content = RichTextField()
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Title(models.Model):
    class Meta:
        verbose_name = 'Заголовок сайта'
        verbose_name_plural = 'Заголовок сайта'

    title = models.CharField(max_length=400, verbose_name='Тема')

    def __str__(self):
        return self.title
