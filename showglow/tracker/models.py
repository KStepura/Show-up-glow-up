from django.db import models

class Notes(models.Model):
    title = models.CharField('Привычка', max_length=50)
    anons = models.CharField('Цель', max_length=250)
    full_text = models.TextField('Прогресс')
    current_value = models.CharField('Нынешнее значение', max_length=250, default='')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tracker/{self.id}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
