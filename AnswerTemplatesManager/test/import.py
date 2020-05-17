import datetime

from Util import basic_util

from AnswerTemplatesManager import models
all_path = basic_util.get_all_path(
    r'C:\Users\liuhuazhen\Desktop\AnswerQuestionSystem\AnswerTemplatesManager\test', '.txt')
# Record.objects.order_by('?')[:2]
for one_p in all_path:

    one_type_templates = basic_util.read_one_file(one_p, 'utf-8')
    for one in one_type_templates:
        if one is not '':
            print(one.split('<\.sp.\>')[0])
            print(one_p)
            models.create_new_stock_template(one.split('<\.sp.\>')[0],one.split('<\.sp.\>')[1],one.split('<\.sp.\>')[2],'admin',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),1)


for one in models.AnswerTemplate.objects.all():
    print(one.__dict__)