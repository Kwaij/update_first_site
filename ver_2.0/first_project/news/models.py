from django.db import models
from django.urls import reverse

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,verbose_name='URL')
    full_text = models.TextField(verbose_name='Статья')
    date = models.DateField(verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True,verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_el', kwargs={'post_slug': self.slug})    

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date','title']