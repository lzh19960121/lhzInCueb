# Generated by Django 2.2.5 on 2020-04-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerTemplatesManager', '0016_auto_20200407_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertemplate',
            name='type',
            field=models.CharField(default='股票', max_length=32, verbose_name='主类别'),
        ),
    ]
