# Generated by Django 2.2.5 on 2020-03-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerTemplatesManager', '0004_auto_20200307_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertemplate',
            name='type',
            field=models.IntegerField(choices=[(1, '外盘'), (2, '保险'), (3, '税务'), (4, '股票')], default=4, verbose_name='主类别'),
        ),
    ]
