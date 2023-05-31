# Generated by Django 4.2.1 on 2023-05-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField(blank=True, verbose_name='Текст отзыва')),
            ],
        ),
    ]