
import random

from AnswerApp.from_neo4j_extract_info.extract.stock_service import stock_region_service

exchange_sector_dic ={
                      '688': '上海科创板',
                      '000': '深圳主板',
                      '001': '深圳主板',
                      '003': '深圳主板',
                      '300': '深圳创业板',
                      '002': '深圳中小板'
                      }


def get_industry_answer_template(type_num):
    """
    得到行业的回答模板
    :param type_num:
    :return:
    """

    templates = ""
    tep = []
    for one in templates:
        if one.split('<\.sp.\>')[0] == type_num:
            tep.append(one.split('<\.sp.\>')[1])
    model_nums = len(tep)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return tep[select]

def answer_region(domains):
    # domain 的1 号元素是股票代码
    answers = ''
    for domain in domains:
        info = stock_region_service.get_one_company_region(domain[1])
        if len(info) == 0:
            return "没有您要知道的【地域】信息", domains
        template = get_region_answer_template('stock_region')
        answers = answers + "</br>" + template.replace("address", info["省市区"]).replace("M", domain[2])
    return answers, domains


def get_region_answer_template(type_name):
    """
    得到地域回答的模板
    :param type_name:
    :return:
    """
    templates = intention_answer_templates[type_name]['templates']
    model_nums = len(templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return templates[select]


def get_exchange_answer_template(type_name):
    """
    得到交易所板块的模板
    :param type_name:
    :return:
    """
    templates = intention_answer_templates[type_name]['templates']
    model_nums = len(templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return templates[select]


def answer_industry(domains):
    answers = ''
    for domain in domains:
        info = stock_industry_service.get_one_company_industry(domain[1])
        if len(info) == 0:
            return "没有您要知道的【行业】信息", domains
        template = get_industry_answer_template('1')
        for one in info:
            if one['级别'] == 'L1':
                template = template.replace('N', one['行业名称'])
            if one['级别'] == 'L2':
                template = template.replace('O', one['行业名称'])
            if one['级别'] == 'L3':
                template = template.replace('P', one['行业名称'])
        answers = answers+"</br>"+template.replace('M', domain[2])
    return answers, domains


def answer_exchange(domains):
    answers = ''
    for domain in domains:
        if domain[1].startswith('60'):
            exchange = '上海主板'
        else:
            num = domain[1][0:3]
            exchange = exchange_sector_dic[num]
        template = get_exchange_answer_template('stock_exchange')
        answers = answers + "</br>" + template.replace('exchange', exchange).replace('M', domain[2])
    return answers, domains





def answer_industry_contain(question):
    industry = stock_industry_service.get_industry_from_question(question)
    answers = ''
    if len(industry) == 0:
        answers = '我没有你要知道的【行业】信息' ,""
    for one in industry:
        companies = stock_industry_service.get_one_industry_contain(one)
        one_answer = ''
        template = get_industry_answer_template('2')
        template = template.replace('N', one)
        for one_c in companies:
            one_answer = one_answer + '，' + one_c['公司代码']+one_c['公司简称']
        template = template.replace('M', one_answer)
        answers = answers + '</br>'+template

    return answers, industry


def answer(question, intention):
    domains = stock_company_service.get_stock_code_in_question(question)
    if len(domains) == 0 and intention == '所属行业':
        return answer_industry_contain(question)
    if intention == "所属行业" :
        return answer_industry(domains)
    if intention == "交易所板块":
        return answer_exchange(domains)
    if intention == "所属地域":
        return answer_region(domains)
    return '没明白您的意思呢'


if __name__ == '__main__':
    print(answer("黄金", '所属行业'))

