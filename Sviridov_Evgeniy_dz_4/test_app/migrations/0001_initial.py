# Generated by Django 3.2 on 2021-04-22 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipted_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Дата поступления')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('measure', models.CharField(max_length=20, verbose_name='Единица измерения')),
                ('vendor', models.CharField(max_length=255, verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Карточка товара',
                'verbose_name_plural': 'Карточки товаров',
            },
        ),
    ]
