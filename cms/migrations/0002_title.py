# Generated by Django 2.1.1 on 2018-10-27 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Заголовок сайта',
            },
        ),
    ]
