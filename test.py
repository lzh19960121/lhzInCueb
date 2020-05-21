from Util import basic_util
import random
#
# all_question = basic_util.read_one_file('file', 'utf-8')
#
# after_delete = basic_util.delete_repeat(all_question)
# question_list = []
# for one in after_delete:
#     label = one.split('<\.sp.\>')[0]
#     sentence = one.split('<\.sp.\>')[1]
#     if label == '所属地域':
#         question_list.append('stock_region<\.sp.\>'+ sentence)
#     if label == '所属行业':
#         question_list.append('stock_industry<\.sp.\>' + sentence)
#     if label == '趋势':
#         question_list.append('stock_trend<\.sp.\>' + sentence)
#     if label == '持有或卖':
#         question_list.append('stock_hold_or_sale<\.sp.\>' + sentence)
#     if label == '买卖':
#         question_list.append('stock_buy_or_sale<\.sp.\>' + sentence)
#     if label == '买':
#         question_list.append('stock_buy<\.sp.\>' + sentence)
#     if label == '概念':
#         question_list.append('stock_concept<\.sp.\>' + sentence)
#     if label == '交易所板块':
#         question_list.append('stock_exchange_board<\.sp.\>' + sentence)
#     if label == '估值':
#         question_list.append('stock_value<\.sp.\>' + sentence)
#     if label == '产品':
#         question_list.append('stock_product<\.sp.\>' + sentence)
#     if label == '大盘':
#         question_list.append('stock_market<\.sp.\>' + sentence)
#
# random.shuffle(question_list)
# random.shuffle(question_list)
# random.shuffle(question_list)
# random.shuffle(question_list)
# random.shuffle(question_list)
# random.shuffle(question_list)
# random.shuffle(question_list)
# random.shuffle(question_list)
# random.shuffle(question_list)
# for one in question_list:
#     basic_util.write_text_apend('file_name',one)
# 加一分钟或5分钟
from datetime import datetime, timedelta


#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

# 加一分钟或5分钟
def datetime_add(dt_string,minutes):
    delta = timedelta(minutes=minutes)
    n_days = string_toDatetime(dt_string) + delta
    return n_days
