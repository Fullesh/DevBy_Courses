from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lession

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='E-mail')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='Страна', **NULLABLE)

    is_verified = models.BooleanField(default=False, verbose_name='Подтверждён')
    token = models.CharField(max_length=10, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}: {self.phone}; {self.country}; {self.is_verified}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    payment_methods_variants = (
        ('Наличные', 'cash'),
        ('Перевод на счёт', 'by card')
    )
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    lession = models.ForeignKey(Lession, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=50, default='cash', choices=payment_methods_variants,
                                      verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.User}: {self.lession if self.lession else self.course}; {self.payment_amount};' \
               f' {self.payment_method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
