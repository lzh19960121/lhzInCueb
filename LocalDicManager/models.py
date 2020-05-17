from django.db import models
import tushare as ts


# Create your models here.


class CompanyManagerDicString(models.Model):
    stock_code = models.TextField(max_length=10, blank=True, verbose_name='股票代码')
    manager_string = models.TextField(max_length=5000, blank=True, verbose_name='高管名称列表')


class CompanyNameDicString(models.Model):
    stock_num = models.TextField(max_length=10, blank=True, verbose_name='股票代码')
    stock_num_with_exchange = models.TextField(max_length=10, blank=True, verbose_name='带交易所代码')
    stock_name = models.TextField(max_length=200, blank=True, verbose_name='股票名称')
    old_name_string = models.TextField(max_length=200, blank=True, verbose_name='旧名称列表')


class IndustryDicString(models.Model):
    industry_code = models.CharField(max_length=20, blank=True, verbose_name='行业代码')
    industry_name = models.CharField(max_length=20, blank=True, verbose_name='行业名称')
    industry_level = models.CharField(max_length=20, blank=True, verbose_name='行业等级')


class ConceptStringDicString(models.Model):
    concept_code = models.CharField(max_length=20, blank=True, verbose_name='概念代码')
    concept_name = models.CharField(max_length=20, blank=True, verbose_name='概念名称')


class ProductStringDicString(models.Model):
    name_string = models.TextField(max_length=20, blank=True, verbose_name='产品名称')


def delete_all_company_manager():
    CompanyManagerDicString.objects.filter().delete()


def delete_all_company_name():
    CompanyNameDicString.objects.filter().delete()


def delete_all_industry():
    IndustryDicString.objects.filter().delete()


def delete_all_concept():
    ConceptStringDicString.objects.filter().delete()


def delete_all_product():
    ProductStringDicString.objects.filter().delete()


def save_company_manager(stock_code, name_string):
    CompanyManagerDicString.objects.create(stock_code=stock_code, manager_string=name_string)


def save_company_name(stock_num, stock_num_with_exchange, stock_name, old_name_string):
    CompanyNameDicString.objects.create(stock_num=stock_num, stock_num_with_exchange=stock_num_with_exchange,
                                        stock_name=stock_name, old_name_string=old_name_string)


def save_industry(industry_code, industry_name, industry_level):
    IndustryDicString.objects.create(industry_code=industry_code, industry_name=industry_name,
                                     industry_level=industry_level)


def save_concept(concept_code, concept_name):
    ConceptStringDicString.objects.create(concept_code=concept_code, concept_name=concept_name)


def save_product(name_string):
    ProductStringDicString.objects.create(name_string=name_string)
