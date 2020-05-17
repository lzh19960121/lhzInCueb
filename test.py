from Util import basic_util
import random

all_question = basic_util.read_one_file('file', 'utf-8')

after_delete = basic_util.delete_repeat(all_question)
question_list = []
for one in after_delete:
    label = one.split('<\.sp.\>')[0]
    sentence = one.split('<\.sp.\>')[1]
    if label == '所属地域':
        question_list.append('stock_region<\.sp.\>'+ sentence)
    if label == '所属行业':
        question_list.append('stock_industry<\.sp.\>' + sentence)
    if label == '趋势':
        question_list.append('stock_trend<\.sp.\>' + sentence)
    if label == '持有或卖':
        question_list.append('stock_hold_or_sale<\.sp.\>' + sentence)
    if label == '买卖':
        question_list.append('stock_buy_or_sale<\.sp.\>' + sentence)
    if label == '买':
        question_list.append('stock_buy<\.sp.\>' + sentence)
    if label == '概念':
        question_list.append('stock_concept<\.sp.\>' + sentence)
    if label == '交易所板块':
        question_list.append('stock_exchange_board<\.sp.\>' + sentence)
    if label == '估值':
        question_list.append('stock_value<\.sp.\>' + sentence)
    if label == '产品':
        question_list.append('stock_product<\.sp.\>' + sentence)
    if label == '大盘':
        question_list.append('stock_market<\.sp.\>' + sentence)

random.shuffle(question_list)
random.shuffle(question_list)
random.shuffle(question_list)
random.shuffle(question_list)
random.shuffle(question_list)
random.shuffle(question_list)
random.shuffle(question_list)
random.shuffle(question_list)
random.shuffle(question_list)
for one in question_list:
    basic_util.write_text_apend('file_name',one)