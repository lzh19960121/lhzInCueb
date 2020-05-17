import random

from from_neo4j_extract_info.extract.stock_service.stock_product_service import get_one_company_products, \
    get_one_product_contain
from match_answer_template.get_template import get_template_by_title
from named_entity_recognition.get_named_entity import get_product_from_question, get_stock_code_in_question

from AnswerApp.models import CompanyNamedEntity
answer_type = 'stock_product'


def get_answer_concept_templates(child_title):
    current_templates = get_template_by_title("概念", child_title)
    model_nums = len(current_templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return current_templates[select]


def answer_company_contain_product(domains):
    all_answers = ''
    for domain in domains:
        info = get_one_company_products(domain.stock_num)
        print(info)
        if info == 'notfound':
            all_answers = all_answers + "</br>" + domain.stock_name + '产品信息不详'
            continue
        template = get_answer_concept_templates("包含").content
        all_product = ''
        for one_product in info:
            all_product = all_product + '[' + one_product['产品'] + ']'
        answers = template.replace('M', domain.stock_name).replace("N", all_product)
        all_answers = all_answers + "</br>" + answers
    return all_answers, domains


def answer_product_contain_company(question):
    answers = '以下是产品相关的信息'
    products = get_product_from_question(question)

    if not len(products):
        answers = '不要逗我，我没有你要知道的【产品】信息', ""
    for one in products:
        companies = get_one_product_contain(one)
        one_answer = ''
        template = get_answer_concept_templates("所属").content
        template = template.replace('N', one)
        if len(companies) == 0:
            continue
        for one_c in companies:
            one_answer = one_answer + '，' + one_c['公司简称']
        template = template.replace('M', one_answer)
        answers = answers + '</br>' + template
    return answers, products


def answer(question, intention):
    domains = get_stock_code_in_question(question)  # type: list[CompanyNamedEntity]
    if len(domains) == 0:
        return answer_product_contain_company(question)
    elif intention == "产品":
        return answer_company_contain_product(domains)
    return '没办法回答你的问题'
