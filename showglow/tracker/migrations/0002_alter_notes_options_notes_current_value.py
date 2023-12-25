# Generated by Django 5.0 on 2023-12-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
        migrations.AddField(
            model_name='notes',
            name='current_value',
            field=models.CharField(default='Значение по умолчанию', max_length=250, verbose_name='Нынешнее значение'),
        ),
    ]
