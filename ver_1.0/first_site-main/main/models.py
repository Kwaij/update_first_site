from django.db import models

class Tech(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField(upload_to='images/')
    full_text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Технику'
        verbose_name_plural = 'Техника'