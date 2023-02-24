from django.db import models
from django.urls import reverse

class Tech(models.Model):
    title = models.CharField(max_length=50,verbose_name='Загаловок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,verbose_name='URL')
    image = models.ImageField(upload_to='images/',verbose_name='Фото')
    full_text = models.TextField(blank=True,verbose_name='Текст записи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
    is_published = models.BooleanField(default=True,verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tech_el', kwargs={'post_slug': self.slug})      

    class Meta:
        verbose_name = 'Технику'
        verbose_name_plural = 'Техника'
        ordering = ['title']