# Generated by Django 3.0.1 on 2020-01-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_desc',
            field=models.CharField(default='', max_length=200),
        ),
    ]
