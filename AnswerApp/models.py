from django.db import models

from django.db import models



class IndustryNamedEntity(object):
    def __init__(self, industry_code, industry_name, industry_level):
        self.industry_code = industry_code
        self.industry_name = industry_name
        self.industry_level = industry_level


class CompanyNamedEntity(object):
    def __init__(self, stock_num_with_exchange, stock_num, stock_name, name_string, short_name):
        self.stock_num_with_exchange = stock_num_with_exchange
        self.stock_num = stock_num
        self.stock_name = stock_name
        self.name_string = name_string
        self.short_name = short_name


class CompanyManagerNamedEntity(object):
    def __init__(self, stock_num, manager_string):
        self.stock_num = stock_num
        self.manager_string = manager_string


# Create your models here.

# --------------------------------------- 以下为上市公司信息的字典
class CompanyManagerDicString(models.Model):
    stock_code = models.TextField(max_length=10, blank=True, verbose_name='股票代码')
    manager_string = models.TextField(max_length=5000, blank=True, verbose_name='高管名称列表')


class CompanyNameDicString(models.Model):
    stock_num = models.TextField(max_length=10, blank=True, verbose_name='股票代码')
    stock_num_with_exchange = models.TextField(max_length=10, blank=True, verbose_name='带交易所代码')
    stock_name = models.TextField(max_length=200, blank=True, verbose_name='股票名称')
    name_string = models.TextField(max_length=200, blank=True, verbose_name='名称列表')
    short_name = models.TextField(max_length=200, blank=True, verbose_name='股票简称')


class IndustryDicString(models.Model):
    industry_code = models.CharField(max_length=20, blank=True, verbose_name='行业代码')
    industry_name = models.CharField(max_length=20, blank=True, verbose_name='行业名称')
    industry_level = models.CharField(max_length=20, blank=True, verbose_name='行业等级')


class ConceptStringDicString(models.Model):
    concept_code = models.CharField(max_length=20, blank=True, verbose_name='概念代码')
    concept_name = models.CharField(max_length=20, blank=True, verbose_name='概念名称')


class ProductStringDicString(models.Model):
    name_string = models.TextField(max_length=20, blank=True, verbose_name='产品名称')


# ---------------------------------------以下为全国地区名的字典


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


def save_company_name(stock_num, stock_num_with_exchange, stock_name, old_name_string, short_name):
    CompanyNameDicString.objects.create(stock_num=stock_num, stock_num_with_exchange=stock_num_with_exchange,
                                        stock_name=stock_name, name_string=old_name_string, short_name=short_name)


def save_industry(industry_code, industry_name, industry_level):
    IndustryDicString.objects.create(industry_code=industry_code, industry_name=industry_name,
                                     industry_level=industry_level)


def save_concept(concept_code, concept_name):
    ConceptStringDicString.objects.create(concept_code=concept_code, concept_name=concept_name)


def save_product(name_string):
    ProductStringDicString.objects.create(name_string=name_string)
