from django.db import models


class Articles(models.Model):
    title = models.CharField('название', max_length=60, default='')
    anons = models.CharField('предисловие', max_length=250, default='')
    full_text = models.TextField('полный-текст')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/lessons/{self.id}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
