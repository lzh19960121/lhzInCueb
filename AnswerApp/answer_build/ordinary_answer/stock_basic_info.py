from AnswerApp.from_neo4j_extract_info.extract.stock_service import stock_company_service
from AnswerApp.models import CompanyNamedEntity
from AnswerApp.named_entity_recognition.get_named_entity import get_stock_code_in_question

# 这个模块需要重写



def answer(question):
    """
    :param question:
    :return: 字符串类型的答案，以及问题中的domains
    """
    domains = get_stock_code_in_question(question)  # type: list[CompanyNamedEntity]
    answers = ''  # type: str
    for one in domains:
        info = stock_company_service.get_company_basic_info(one.stock_num)
        if info == "notfound":
            return "数据库没有该股信息", domains
        for one_i in info:
            answers = answers + one_i + " : " + str(info[one_i]) + "</br>"
    return answers.replace("']","").replace("['",""), domains


if __name__ == '__main__':
    answer("平安银行")
