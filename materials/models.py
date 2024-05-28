from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='materials/courses/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f''

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lession(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='materials/lessions/', verbose_name='Превью', **NULLABLE)
    URL = models.URLField(verbose_name='URL')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)

    def __str__(self):
        return f''

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
