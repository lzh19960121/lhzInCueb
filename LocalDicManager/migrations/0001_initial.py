# Generated by Django 2.2.5 on 2020-04-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyManagerDicString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.TextField(blank=True, max_length=10, verbose_name='股票代码')),
                ('manager_string', models.TextField(blank=True, max_length=5000, verbose_name='高管名称列表')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyNameDicString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_num', models.TextField(blank=True, max_length=10, verbose_name='股票代码')),
                ('stock_num_with_exchange', models.TextField(blank=True, max_length=10, verbose_name='带交易所代码')),
                ('stock_name', models.TextField(blank=True, max_length=200, verbose_name='股票名称')),
                ('old_name_string', models.TextField(blank=True, max_length=200, verbose_name='旧名称列表')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptStringDicString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept_code', models.CharField(blank=True, max_length=20, verbose_name='概念代码')),
                ('concept_name', models.CharField(blank=True, max_length=20, verbose_name='概念代码')),
            ],
        ),
        migrations.CreateModel(
            name='IndustryDicString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_code', models.CharField(blank=True, max_length=20, verbose_name='行业代码')),
                ('industry_name', models.CharField(blank=True, max_length=20, verbose_name='行业名称')),
                ('industry_level', models.CharField(blank=True, max_length=20, verbose_name='行业等级')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStringDicString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_string', models.TextField(blank=True, max_length=20, verbose_name='产品名称')),
            ],
        ),
    ]
