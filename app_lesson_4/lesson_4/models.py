from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def created_at(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span type="color:green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d:%m:%Y')

#class Meta:
#        db_table = 'advertisements'
 #   def __str__(self):
  #      return f'Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'



"""
название
описание
цена
время создания
время обновления
торг
"""
