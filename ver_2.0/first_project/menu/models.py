from django.db import models

class Menu(models.Model):
    title = models.CharField('Название', max_length=15)
    url_name = models.CharField('url_name', max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
