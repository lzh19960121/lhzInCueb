# 股票趋势的分析类
import random

from from_neo4j_extract_info.extract.stock_service import stock_trends_service
from named_entity_recognition.get_named_entity import get_stock_code_in_question
# 得到所有实体
from match_answer_template.get_template import get_template_by_title
from AnswerTemplatesManager.models import AnswerTemplate
from AnswerApp.models import CompanyNamedEntity

def get_templates(properties):
    """
    得到模板
    :param properties:
    :return:
    """
    current_templates = [] # type: list[AnswerTemplate]
    if properties['阻力位'] != '无' and properties['阻力位'] != '无':
        current_templates = get_template_by_title("趋势", '趋势')
    elif properties['阻力位'] == '无' :
        current_templates = get_template_by_title("趋势", '趋势无压力')
    elif properties['支撑位'] == '无':
        current_templates = get_template_by_title("趋势", '趋势无支撑')
    model_nums = len(current_templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return current_templates[select]


# 每个类必须有answer方法



def answer(question, intention):
    """
    # 回答的主要方法
    :param intention:
    :param question: 传入问题
    :return:
    """
    domains = get_stock_code_in_question(question) # type: list[CompanyNamedEntity]
    print(domains)
    if not len(domains):
        return '我没有你要知道的【趋势】信息' ,""
    all_answers = '您是想问'+intention+"的方面吧。"

    for domain in domains:
        properties = stock_trends_service.get_one_company_trend(domain.stock_num)
        template = get_templates(properties).content
        answers = template.replace("data", properties['日期'][0]). \
            replace("stocknumber", domain.stock_num).\
            replace("stockname", domain.stock_name).\
            replace("status", properties['股价状态'][0]).\
            replace("area", properties['超买超卖'][0]).\
            replace("hinder", properties['阻力位']).\
            replace("embrace", properties['支撑位'])
        all_answers = all_answers+"</br>"+answers
    return all_answers, domains


if __name__ == '__main__':
    print(answer("麒盛科技", '趋势'))