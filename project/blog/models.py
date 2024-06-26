from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Название статьи')
    content = models.TextField(verbose_name='Содержание статьи')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновление')
    publish = models.BooleanField(default=True, verbose_name='Статус публикации')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    video = models.CharField(max_length=500, verbose_name='Ссылка видео', blank=True, null=True)

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'data:image/png;base64,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'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
