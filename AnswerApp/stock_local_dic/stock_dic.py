from AnswerApp import models
# 整个类需要每天加载一遍
from AnswerApp.stock_local_dic.dic_help import load_all_finance_index_by_date
from AnswerApp.stock_local_dic import dic_tool

print("********************************************正在加载字典********************************************")
print("********************************************加载公司名称********************************************")

all_company_name = [
    models.CompanyNamedEntity(one.stock_num_with_exchange, one.stock_num, one.stock_name, one.name_string,
                              one.short_name)
    for one in models.CompanyNameDicString.objects.all()]

print("********************************************加载公司高管********************************************")

all_company_manager = [models.CompanyManagerNamedEntity(one.stock_code, one.manager_string) for one in
                       models.CompanyManagerDicString.objects.all()]

print("********************************************加载产品********************************************")

all_product = [one.name_string for one in models.ProductStringDicString.objects.all()]

print("********************************************加载概念********************************************")
all_concept = [one.concept_name for one in models.ConceptStringDicString.objects.all()]
print("********************************************加载行业********************************************")

all_industry = [models.IndustryNamedEntity(one.industry_code, one.industry_name, one.industry_level) for one in
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
