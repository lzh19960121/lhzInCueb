# Generated by Django 2.2.5 on 2020-04-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerTemplatesManager', '0009_auto_20200406_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertemplate',
            name='is_passed',
            field=models.BooleanField(verbose_name='是否审核通过'),
        ),
    ]
