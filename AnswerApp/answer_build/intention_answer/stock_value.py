import numpy as np
from Util import basic_util
import random

from from_neo4j_extract_info.extract.stock_service import stock_industry_service, stock_daily_indicators_service, \
    stock_finance_index_service, stock_trends_service
from named_entity_recognition.get_named_entity import get_stock_code_in_question
from AnswerApp.models import CompanyNamedEntity


# 得到该公司的三级行业
def get_industry(domain):
    """
    :param domain:
    :return: 三级行业名称
    """
    info = stock_industry_service.get_one_company_industry(domain[1])
    for one in info:
        if one['级别'] == 'L3':
            return one['行业名称']


# 得到该公司的每日指标
def get_current_company_index(one_domain):
    """
    :param one_domain:
    :return:
    """
    current_domain_index = stock_daily_indicators_service.get_one_company_daily_index_by_code(one_domain[1])
    return current_domain_index[0]


# 得到某个公司所属行业的所有公司
def get_current_industry_contain(one_domain):
    """
    :param one_domain:
    :return:
    """
    industry = get_industry(one_domain)
    companies = stock_industry_service.get_one_industry_contain(industry)
    companies = basic_util.delete_repeat(companies)
    return companies, industry


# 把市净率排序
def get_sorted_pb(companies):
    industry_index_list = []
    for one_com in companies:
        value_index = stock_daily_indicators_service.get_one_company_daily_index_by_code(one_com['公司代码'])
        if value_index == 'notfound':
            continue
        if len(value_index) != 0:
            if float(value_index[0]['市净率']) >= 0:
                industry_index_list.append(value_index[0])
    industry_index_list_sorted = sorted(industry_index_list, key=lambda e: float(e.__getitem__('市净率')))
    return industry_index_list_sorted


# 把市盈率排序
def get_sorted_pe(companies):
    industry_index_list = []
    for one_com in companies:
        value_index = stock_daily_indicators_service.get_one_company_daily_index_by_code(one_com['公司代码'])
        if value_index == 'notfound':
            continue
        if len(value_index) != 0:
            if float(value_index[0]['市盈率']) >= 0:
                industry_index_list.append(value_index[0])
    industry_index_list_sorted = sorted(industry_index_list, key=lambda e: float(e.__getitem__('市盈率')))
    return industry_index_list_sorted


# 根据分好层次的组别，和当前公司的指标得到市净率的估值评论
def get_value_comment_by_index(after_separated, current_company_index, index_name):
    index = 1
    for one in after_separated:
        # 找到这个组内的最后一名，和这个组的最后一名作比较
        if float(one[-1][index_name]) >= float(current_company_index[index_name]):
            break
        index = index + 1
    if index == 1:
        return "属于前20%,估值低,优势明显"
    if index == 2:
        return "属于20%-40%,估值偏低,有优势"
    if index == 3:
        return "属于40%-60%,估值处于行业平均水平"
    if index == 4:
        return "属于60%-80%,估值偏高,谨慎对待"
    if index == 5:
        return "属于80%-100%,估值过高,警惕风险"


# 组合业务
def get_one_company_value_comment_pb(one_domain):
    current_company_index = get_current_company_index(one_domain)
    # 得到当前公司的每日指标
    companies, industry = get_current_industry_contain(one_domain)
    # 当前共同一个行业的公司
    industry_index_list_sorted_pb = get_sorted_pb(companies)
    # 根据市净率进行排序
    industry_index_list_sorted_pe = get_sorted_pe(companies)
    after_separated_pb = np.array_split(industry_index_list_sorted_pb, 5)
    # 将其分层
    after_separated_pe = np.array_split(industry_index_list_sorted_pe, 5)
    # 将其分层
    value_comment_pb = get_value_comment_by_index(after_separated_pb, current_company_index, '市净率')
    # 根据分层得到评价
    value_comment_pe = get_value_comment_by_index(after_separated_pe, current_company_index, '市盈率')
    return current_company_index, value_comment_pb, industry, value_comment_pe


def get_sorted_increase(companies):
    """
    对增长率进行排序
    :param companies:
    :return:
    """
    industry_index_list = []
    for one_com in companies:
        value_index = get_current_company_finance_index(one_com['公司代码'])
        if value_index == 'notfound':
            continue
        if len(value_index) != 0:
            industry_index_list.append(value_index)
    industry_index_list_sorted = sorted(industry_index_list,
                                        reverse=True, key=lambda e: float(e.__getitem__('利润总额同比增长率百分比')))
    return industry_index_list_sorted


def get_increase_comment_by_index(after_separated, current_company_index):
    """
    :param after_separated: 分层后的所有行业指标
    :param current_company_index: 当前公司的财务指标
    :return:
    """
    index = 1
    for one in after_separated:
        if float(one[-1]['利润总额同比增长率百分比']) <= \
                float(current_company_index['利润总额同比增长率百分比']):
            break
        index = index + 1
    if index == 1:
        return "属于前20%,增长快,优势明显"
    if index == 2:
        return "属于20%-40%,增行较快,有优势"
    if index == 3:
        return "属于40%-60%,增长处于行业平均水平"
    if index == 4:
        return "属于60%-80%,增长偏低,谨慎对待"
    if index == 5:
        return "属于80% -100 %,增长过低,警惕风险"


def get_current_company_finance_index(one_domain_num):
    """
    :param one_domain_num:
    :return:
    """

    current_domain_index = stock_finance_index_service.get_one_company_finance_index(one_domain_num)
    return current_domain_index


def get_one_company_increase_comment(one_domain):
    current_company_finance_index = get_current_company_finance_index(one_domain[1])  # 得到当前公司的每日指标
    companies, industry = get_current_industry_contain(one_domain)  # 当前共同一个行业的公
    industry_index_list_sorted = get_sorted_increase(companies)  # 根据利润排序
    after_separated = np.array_split(industry_index_list_sorted, 5)
    # 将其分层
    increase_comment = get_increase_comment_by_index(after_separated, current_company_finance_index)  # 根据分层得到评价
    return current_company_finance_index, increase_comment


def get_company_trends_node(domain):
    properties = stock_trends_service.get_one_company_trend(domain[1])
    return properties


# def get_templates(properties):
#     """
#     得到模板
#     :param properties:
#     :return:
#     """
#     current_templates = []
#     if properties['阻力位'] != '无' and properties['阻力位'] != '无':
#         current_templates = answer_templates_service.get_template_by_label(answer_type, '估值')
#     elif properties['阻力位'] == '无':
#         current_templates = answer_templates_service.get_template_by_label(answer_type, '估值无压力')
#     elif properties['支撑位'] == '无':
#         current_templates = answer_templates_service.get_template_by_label(answer_type, '估值无支撑')
#     model_nums = len(current_templates)  # 得到模板数量
#     select = random.randint(0, model_nums - 1)
#     return current_templates[select]


def answer(question, intention):
    domains = get_stock_code_in_question(question)
    # 得到问题的所有实体
    if not len(domains):
        return '我没有你要知道的'
    all_answers = '您是想问' + intention + "的方面吧。"
    for one_domain in domains:
        current_company_index, value_comment_pb, industry, value_comment_pe = get_one_company_value_comment_pb(
            one_domain)
        company_trends = get_company_trends_node(one_domain)
        current_company_finance_index, increase_comment = get_one_company_increase_comment(one_domain)
        template = ""
        template = template.replace("data", company_trends['日期'][0]). \
            replace('stocknumber', one_domain[1]). \
            replace('stockname', one_domain[2]). \
            replace('hangye', industry). \
            replace("pe", str(current_company_index['市盈率'])). \
            replace('mouge_1', value_comment_pe). \
            replace("pb", str(current_company_index['市净率'])). \
            replace('mouge_2', value_comment_pe). \
            replace("zengzhanglv", str(current_company_finance_index['利润总额同比增长率百分比'])). \
            replace('mouge_crease', increase_comment). \
            replace("status", company_trends['股价状态'][0]). \
            replace('area', company_trends['超买超卖'][0]). \
            replace("hinder", company_trends['阻力位']). \
            replace('embrace', company_trends['支撑位'])
        all_answers = all_answers + "</br>" + template
    return all_answers, domains


if __name__ == '__main__':
    print(answer("平安银行", ''))
