import random
from AnswerApp.from_neo4j_extract_info.extract.stock_service import stock_region_service
from match_answer_template.get_template import get_template_by_title

from named_entity_recognition.get_named_entity import get_stock_code_in_question

from AnswerTemplatesManager.models import AnswerTemplate
from AnswerApp.models import CompanyNamedEntity

def answer_region(domains):
    # domain 的1 号元素是股票代码
    answers = ''
    for domain in domains:
        info = stock_region_service.get_one_company_region(domain.stock_num)
        if len(info) == 0:
            return "没有您要知道的【地域】信息", domains
        template = get_region_answer_template().content
        answers = answers + "</br>" + template.replace("address", info["省市区"]).replace("M", domain.stock_name)
    return answers, domains


def get_region_answer_template():
    """
    得到地域回答的模板
    :param type_name:
    :return:
    """
    templates = get_template_by_title("地域", "所属")  # type: list[AnswerTemplate]
    model_nums = len(templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return templates[select]


def answer(question, intention):
    domains = get_stock_code_in_question(question)  # type: list[CompanyNamedEntity]

    if len(domains) == 0:
        return '没明白您的意思呢', domains

    return answer_region(domains)
