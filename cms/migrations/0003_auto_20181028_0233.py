# Generated by Django 2.1.1 on 2018-10-27 23:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='text',
            options={'verbose_name': 'Контент', 'verbose_name_plural': 'Контент'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'Заголовок сайта', 'verbose_name_plural': 'Заголовок сайта'},
        ),
        migrations.AlterField(
            model_name='text',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
