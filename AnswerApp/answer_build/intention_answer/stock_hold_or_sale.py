import random

from from_neo4j_extract_info.extract.stock_service import stock_trends_service
from named_entity_recognition.get_named_entity import get_stock_code_in_question

# 模板对应三种状态，所以要分成三种回答方式，含有震荡的都是震荡，其余为上涨或者下跌 ,此处将要优化
from match_answer_template.get_template import get_template_by_title
from AnswerApp.models import CompanyNamedEntity


def get_templates(properties):
    current_status = stock_trends_service.get_stock_status(properties)
    current_templates = get_template_by_title("持有或卖", current_status)
    model_nums = len(current_templates)  # 得到模板数量
    select = random.randint(0, model_nums - 1)
    return current_templates[select]


def answer(question, intention):
    domains = get_stock_code_in_question(question)  # type: list[CompanyNamedEntity]
    all_answers = '您是想问' + intention + "的方面吧。"  # 输入几个实体，对应几条回答
    if 0 == len(domains):
        return '我没有你要知道的【持有或卖】信息', ""
    for domain in domains:
        properties = stock_trends_service.get_one_company_trend(domain.stock_num)
        template = get_templates(properties).content  # 调用模板选择函数
        answers = template.replace("data", properties['日期'][0]).replace("stocknumber", domain.stock_num).replace(
            "stockname",
            domain.stock_name).replace(
            "status", properties['股价状态'][0]).replace("area", properties['超买超卖'][0]).replace("hinder",
             properties['阻力位']).replace(
            "embrace", properties['支撑位'])
        all_answers = all_answers + "</br>" + answers
    return all_answers, domains


if __name__ == '__main__':
    print(answer("中国银行怎么样", ''))
