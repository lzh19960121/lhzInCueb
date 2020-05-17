from AnswerApp.stock_local_dic.stock_dic import all_concept, \
    all_company_manager, all_industry, all_company_name, all_product
from Util import basic_util

from AnswerApp.models import CompanyNamedEntity
# ------------------------------------------------------股票实体识别----------------------------------------------------



def get_stock_code_by_full_name(question):
    """
    根据股票的全程，获得股票的信息
    :param question:
    :return:
    """
    domains = []
    for one_company in all_company_name:
        # 检查股票代码或者当前股票名称是否包含其中
        if one_company.stock_num in question or one_company.stock_name in question:
            domains.append(one_company)
            continue

        # 检查用户是否输入的是旧名字
        now_old_short_name = one_company.name_string.split(',')[1:]
        for one_name in now_old_short_name:
            if one_name in question:
                domains.append(one_company)
    return basic_util.delete_repeat(domains)  # type:list[CompanyNamedEntity]


def get_stock_code_by_short_name(question):
    """
    通过股票简称获得股票的代码
    :param question:
    :return:
    """
    domains = []
    for one_company in all_company_name:
        # 检查股票代码或者当前股票名称是否包含其中
        if one_company.short_name == '':
            continue
        if one_company.short_name in question or one_company.short_name == question:
            domains.append(one_company)
    return basic_util.delete_repeat(domains)  # type:list[CompanyNamedEntity]


def get_stock_code_in_question(question):
    """
    此方法效率很低，可以改进，从问题中找到实体
    :param question:
    :return:
    """
    re = get_stock_code_by_full_name(question)
    if len(re) != 0:
        return re
    else:
        return get_stock_code_by_short_name(question)


# --------------------------------------------------股票概念识别-------------------------------------------------------------

def get_concept_from_question(question):
    """
    从问题中获取概念
    :param question:
    :return:
    """
    concept_list = []
    for one in all_concept:
        if one in question:
            concept_list.append(one)
    return basic_util.delete_repeat(concept_list)  # type:list[str]


# -------------------------------------------------行业识别-------------------------------------------------------------------


def get_industry_from_question(question):
    """
    从问题中获取行业
    :param question:
    :return:
    """
    industry = []
    for one in all_industry:
        if one.industry_name in question:
            industry.append(one)
    return basic_util.delete_repeat(industry)  # type:list[IndustryNamedEntity]


# ----------------------------------------------产品识别-----------------------------------------------------------------------
def get_product_from_question(question):
    """
    :param question: 从问题中获取产品
    :return:
    """
    product = []
    for one_p in all_product:
        # 将和产品近似的产品全部抛出
        if one_p in question:
            product.append(one_p)
        elif one_p[0:3] in question:
            product.append(one_p)
    return product  # type:list[str]


# ---------------------------------------------------------------公司高管识别---------------------------------------------------
def get_name_from_manager(question):
    """
    从问题匹配管理层
    :param question:
    :return:管理层人员的名字
    """
    companies = []
    for one in all_company_manager:
        if question in one.manager_string:
            companies.append(one.stock_num)
    return companies  # type:list[str]
