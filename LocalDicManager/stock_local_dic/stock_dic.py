from LocalDicManager import models
# 整个类需要每天加载一遍
from LocalDicManager.stock_local_dic.dic_help import load_all_finance_index_by_date
from stock_local_dic import dic_tool

print("********************************************正在加载字典********************************************")
print("********************************************加载公司名称********************************************")


class CompanyNamedEntity(object):
    def __init__(self, stock_num_with_exchange, stock_num, stock_name, old_name_string):
        self.stock_num_with_exchange = stock_num_with_exchange
        self.stock_num = stock_num
        self.stock_name = stock_name
        self.old_name_string = old_name_string


all_company_name = [CompanyNamedEntity(one.stock_num_with_exchange, one.stock_num, one.stock_name, one.old_name_string)
                    for one in models.CompanyNameDicString.objects.all()]

print("********************************************加载公司高管********************************************")


class CompanyManagerNamedEntity(object):
    def __init__(self, stock_num, manager_string):
        self.stock_num = stock_num
        self.manager_string = manager_string


all_company_manager = [CompanyManagerNamedEntity(one.stock_code, one.manager_string) for one in
                       models.CompanyManagerDicString.objects.all()]
print("********************************************加载产品********************************************")

all_product = [one.name_string for one in models.ProductStringDicString.objects.all()]

print("********************************************加载概念********************************************")
all_concept = [one.concept_name for one in models.ConceptStringDicString.objects.all()]
print("********************************************加载行业********************************************")


class IndustryNamedEntity(object):
    def __init__(self, industry_code, industry_name, industry_level):
        self.industry_code = industry_code
        self.industry_name = industry_name
        self.industry_level = industry_level


all_industry = [IndustryNamedEntity(one.industry_code, one.industry_name, one.industry_level) for one in
                models.IndustryDicString.objects.all()]
print("********************************************加载财务指标********************************************")

all_finance_index = load_all_finance_index_by_date("20190930")

print("**********************本地数据加载结束，即将加载Rnn模块********************************************")

#
# print(all_company_name)
# print(all_concept)
# print(all_product)
# print(all_industry)
# print(all_company_manager)
