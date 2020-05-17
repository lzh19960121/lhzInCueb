import importlib


#  查询当前所有正常上市交易的股票列表
#  答案形成类，动态加载类进行回答

def answer(question, answer_type, intention):
    if answer_type == 'intelligent':
        analyse_module = importlib.import_module('AnswerApp.answer_build.intention_answer.' + intention)
        answers, domains = analyse_module.answer(question, intention)
        return answers,  domains

    if answer_type == 'ordinary':
        ordinary_class_name = intention
        analyse_module = importlib.import_module('AnswerApp.answer_build.ordinary_answer.' + ordinary_class_name)
        answers, domains = analyse_module.answer(question)
        return answers,  domains
