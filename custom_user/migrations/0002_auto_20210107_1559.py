# Generated by Django 3.1.5 on 2021-01-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cellphone',
            field=models.CharField(max_length=13, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(auto_now=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=60, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Статус акаунта (подтвержден/неподтвержден администатором)'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=60, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=121, verbose_name='Никнейм (создается автоматически)'),
        ),
    ]
