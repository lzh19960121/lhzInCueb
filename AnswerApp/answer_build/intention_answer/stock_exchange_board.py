import random

from match_answer_template.get_template import get_template_by_title
from AnswerApp.models import CompanyNamedEntity
from named_entity_recognition.get_named_entity import get_stock_code_in_question
from AnswerApp.models import CompanyNamedEntity

exchange_sector_dic = {
    '688': '上海科创板',
    '000': '深圳主板',
    '001': '深圳主板',
    '003': '深圳主板',
    '300': '深圳创业板',
    '002': '深圳中小板'
}


def get_exchange_answer_template():
    """
    得到交易所板块的模板
    :param type_name:
    :return:
    """
    templates = get_template_by_title("交易所板块", '属于')
    model_nums = len(templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return templates[select]


def answer_exchange(domains):
    answers = ''
    for domain in domains:
        if domain[1].startswith('60'):
            exchange = '上海主板'
        else:
            num = domain.stock_num[0:3]
            exchange = exchange_sector_dic[num]
        template = get_exchange_answer_template().content
        answers = answers + "</br>" + template.replace('exchange', exchange).replace('M', domain.stock_name)
    return answers, domains


def answer(question, intention):
    domains = get_stock_code_in_question(question) # type: list[CompanyNamedEntity]

    return answer_exchange(domains)
