
import random

from from_neo4j_extract_info.extract.stock_service import stock_concept_service, stock_company_service
from match_answer_template.get_template import get_template_by_title
from named_entity_recognition.get_named_entity import get_concept_from_question, get_stock_code_in_question
from AnswerApp.models import CompanyNamedEntity

answer_type = 'stock_gainian'


def get_answer_concept_templates(child_title):
    current_templates = get_template_by_title("概念", child_title)
    model_nums = len(current_templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return current_templates[select]


def answer_concept(domains):
    all_answers = ''
    for domain in domains:
        concept_info = stock_concept_service.get_one_company_concept(domain.stock_num)
        if concept_info == 'notfound':
            return "我没有你知道的概念信息", domains
        template = get_answer_concept_templates("所属").content
        all_concept = ''
        for one_concept in concept_info:
            all_concept = all_concept + '[' + one_concept['概念名称'] + ']'
        answers = template.replace('M', domain.stock_name).replace("N", all_concept)
        all_answers = all_answers + "</br>" + answers
    return all_answers, domains


def answer_concept_contain(question):
    answers = ''
    concepts = get_concept_from_question(question)
    if not len(concepts):
        answers = '我没有你要知道的【概念】信息', ""
    for one in concepts:
        companies = stock_concept_service.get_concept_contains_company(one)
        one_answer = ''
        template = get_answer_concept_templates("包含").content
        template = template.replace('N', one)
        for one_c in companies:
            one_answer = one_answer + '，' + one_c['公司代码'] + one_c['公司简称']
        template = template.replace('M', one_answer)
        answers = answers + '</br>' + template
    return answers, concepts


def answer(question, intention):
    domains = get_stock_code_in_question(question) # type: list[CompanyNamedEntity]
    if len(domains) == 0:
        return answer_concept_contain(question)
    if intention == "概念":
        return answer_concept(domains)
    return '没办法回答你的问题', domains


if __name__ == '__main__':
    print(answer('煤炭', '概念'))
