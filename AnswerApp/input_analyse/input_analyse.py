from AnswerApp.stock_local_dic.stock_dic import all_company_manager, all_company_name
# 分析问题的成分
from TextRnnModel.predict import CnnModel
import string


def is_manager_name(question):
    for one_m in all_company_manager:
        if question in one_m.manager_string.strip(string.digits):
            return 'ordinary', "people"


def is_stock(question):
    for one in all_company_name:
        if question in one.name_string or question == one.short_name:
            return "ordinary", "stock_basic_info"


def is_admin(question):
    if "刘华振" in question:
        return 'ordinary', "people"


def judge_question_type(question):
    """
    :param question:
    :return:
    """
    if is_admin(question) is not None:
        return is_admin(question)
    if is_stock(question) is not None:
        return is_stock(question)
    if is_manager_name(question) is not None:
        return is_manager_name(question)


class QuestionAnalyse:
    def __init__(self):
        self.cnn_model = CnnModel()

    def analyse_question_type(self, question):
        """
        :param question:
        :return:
        """
        if judge_question_type(question) is not None:
            return judge_question_type(question)
        else:
            return "intelligent", self.cnn_model.predict(question)

    def analyse(self, question):
        return self.analyse_question_type(question)
