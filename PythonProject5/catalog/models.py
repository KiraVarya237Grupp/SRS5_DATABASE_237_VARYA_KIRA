from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название жанра")

    def __str__(self):
        return self.name


class Title(models.Model):
    KIND_CHOICES = [
        ('movie', 'Фильм'),
        ('series', 'Сериал'),
        ('book', 'Книга'),
        ('game', 'Игра'),
    ]

    title = models.CharField(max_length=200, verbose_name="Название")
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default='movie', verbose_name="Тип")
    genres = models.ManyToManyField(Genre, blank=True, verbose_name="Жанры")

    def __str__(self):
        return self.title


class WatchEntry(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Запланировано'),
        ('watching', 'Смотрю/Читаю'),
        ('completed', 'Завершено'),
    ]

    title = models.ForeignKey(Title, on_delete=models.CASCADE, verbose_name="Произведение")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned', verbose_name="Статус")
    rating = models.PositiveIntegerField(blank=True, null=True, verbose_name="Оценка")
    notes = models.TextField(blank=True, null=True, verbose_name="Заметки")

    def __str__(self):
        return f"{self.title.title} ({self.get_status_display()})"