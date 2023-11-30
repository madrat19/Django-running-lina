from django.db import models

class Requests(models.Model):
    request = models.CharField('Запрос', max_length=256)
    date = models.DateTimeField('Дата зароса')
    
    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
