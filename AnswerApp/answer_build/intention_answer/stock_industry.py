from from_neo4j_extract_info.extract.stock_service import stock_industry_service
from match_answer_template.get_template import get_template_by_title
from named_entity_recognition.get_named_entity import get_industry_from_question, get_stock_code_in_question
from AnswerApp.models import CompanyNamedEntity


def answer_industry(domains):
    answers = ''
    for domain in domains:
        info = stock_industry_service.get_one_company_industry(domain.stock_num)
        if len(info) == 0:
            return "没有您要知道的【行业】信息", domains
        template = get_template_by_title("行业", "所属")[0].content
        for one in info:
            if one['级别'] == 'L1':
                template = template.replace('N', one['行业名称'])
            if one['级别'] == 'L2':
                template = template.replace('O', one['行业名称'])
            if one['级别'] == 'L3':
                template = template.replace('P', one['行业名称'])
        answers = answers + "</br>" + template.replace('M', domain.stock_name)
    return answers, domains


def answer_industry_contain(question):
    industry = get_industry_from_question(question)
    answers = ''
    if len(industry) == 0:
        answers = '我没有你要知道的【行业】信息', ""
    for one in industry:
        companies = stock_industry_service.get_one_industry_contain(one)
        one_answer = ''
        template = get_template_by_title("行业", "包含")[0].content
        template = template.replace('N', one)
        for one_c in companies:
            one_answer = one_answer + '，' + one_c['公司代码'] + one_c['公司简称']
        template = template.replace('M', one_answer)
        answers = answers + '</br>' + template

    return answers, industry


def answer(question, intention):
    domains = get_stock_code_in_question(question) # type: list[CompanyNamedEntity]
    if len(domains) == 0 and intention == '所属行业':
        return answer_industry_contain(question)
    if intention == "所属行业":
        return answer_industry(domains)
    return '没明白您的意思呢'
