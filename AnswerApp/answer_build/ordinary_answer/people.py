from from_neo4j_extract_info.extract.stock_service import stock_managers_service, stock_company_service
from named_entity_recognition.get_named_entity import get_name_from_manager, get_stock_code_in_question


# 这个模块需要重写

def answer(question):
    if "刘华振" in question:
        return "你是问管理员吗？管理员是我爸爸,不要说我爸爸的坏话"

    info = get_name_from_manager(question)
    answers = ''

    name = stock_managers_service.get_manager_info_by_name(question)
    for one in info:
        current = []
        for n in name:
            if n['离任日期'] == '':
                current.append(n)
        a = get_stock_code_in_question(one.split(',')[0])
        if len(current) == 0:
            return "没有您要知道的信息", question
        answers = '为您找到这些这些消息' + ',' + current[0]['姓名'] + ',' + ('女' if (current[0]['性别'] == 'F') else '男') + ',' + \
                  current[0]['出生年月'] + '月出生,' + '在' + a[0].stock_name + '担任以下职位---'
        manager = '高管：'
        stock_holder = '董事会：'
        other = '其他：'
        for c in current:
            if c['岗位类别'] == '其他':
                other = other + "[" + c['岗位'] + ']'
            if c['岗位类别'] == '董事会成员':
                stock_holder = stock_holder + "[" + c['岗位'] + ']'
            if c['岗位类别'] == '高管':
                manager = manager + "[" + c['岗位'] + ']'
        if other == '其他：':
            other = ''
        answers = answers + "</br>" + manager + "</br>" + stock_holder + "</br>" + other

    return answers, name
