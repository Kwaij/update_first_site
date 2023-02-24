# Generated by Django 4.1.5 on 2023-01-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to='')),
                ('full_text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Техника',
                'verbose_name_plural': 'Техника',
            },
        ),
    ]