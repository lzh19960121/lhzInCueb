# Generated by Django 2.2.5 on 2020-03-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerTemplatesManager', '0006_auto_20200313_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertemplate',
            name='content',
            field=models.TextField(blank=True, max_length=999, verbose_name='内容'),
        ),
    ]
