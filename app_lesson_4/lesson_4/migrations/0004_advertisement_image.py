# Generated by Django 4.2.3 on 2023-08-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_4', '0003_advertisement_user_alter_advertisement_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
