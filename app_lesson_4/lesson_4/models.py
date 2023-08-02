from django.db import models

# Create your models here.

class Advertisement(models.Model):

    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'advertisements'

'''DecimalField - поле для чисел;
    CharField - поле для маленьких строк;      
    TextField - поле для больших строк;
    BooleanField - да или нет;
'''


"""
название
описание
цена
время создания
время обновления
торг
"""