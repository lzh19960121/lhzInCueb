# Generated by Django 3.0.4 on 2020-03-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerTemplatesManager', '0003_auto_20200307_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertemplate',
            name='content',
            field=models.CharField(blank=True, max_length=199, verbose_name='内容'),
        ),
    ]
