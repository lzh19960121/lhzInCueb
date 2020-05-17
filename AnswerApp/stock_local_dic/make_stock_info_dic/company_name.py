import time
from AnswerApp import models
import tushare as ts
# Register your models here.
from Util import basic_util

# 这个程序逻辑较为别扭，是为了提高更新效率，代码不具有维护性
# 刘华振


all_province = basic_util.read_one_file(
    r'C:\inetpub\wwwroot\AnswerQuestionSystem\AnswerApp\stock_local_dic\make_stock_info_dic\region\province.text', 'utf-8')
all_city = basic_util.read_one_file(
    r'C:\inetpub\wwwroot\AnswerQuestionSystem\AnswerApp\stock_local_dic\make_stock_info_dic\region\city.text', 'utf-8')
all_district = basic_util.read_one_file(
    r'C:\inetpub\wwwroot\AnswerQuestionSystem\AnswerApp\stock_local_dic\make_stock_info_dic\region\district.text', 'utf-8')


def filter_name(simple_name):
    """
    检查该名字开头是不是以省市区
    :param simple_name:
    :return:
    """
    for one in all_province:
        # 不添加
        if one.replace("市", '').replace("省", '') == simple_name:
            return
    for one in all_city:
        if one.replace("市", '') == simple_name:
            return
    for one in all_district:
        if one.replace("区", '').replace("县", '') == simple_name:
            return
    return 1


def check_is_change(stock_num, stock_name):
    """
    :return:
    """
    # 检查是否已经存在了当前信息，如果没发生改变返回0
    try:
        dic_obj = models.CompanyNameDicString.objects.get(stock_name=stock_name)
        return False
    except Exception:
        models.CompanyNameDicString.objects.filter(stock_num=stock_num).delete()
        print("发现有更新的" + stock_num + stock_name)
        # 如果没有,则返回，说明新增了，需要删除
        return True

    # for one in current_dic:
    #     if stock_name == one.stock_name:
    #         return 0, current_dic
    # # 若没有匹配到，说明发生了改变，此时又两种情况。
    # # 1. 名字已经更新，此时要把原来的一行删掉
    # # 2. 该股票不存在,此时返回1
    # for one in current_dic:
    #     if one.stock_name == stock_name:
    #         current_dic.remove(one)
    # return 1, current_dic


def write_company_name_to_sql():
    pro = ts.pro_api('65d978be5ed23ecc8e71f573fea23125ba1319fe6838ce50e9243242')
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name')
    company_info = [tuple(xi) for xi in data.values]
    for one_company_info in company_info:
        # 拼接字符串
        stock_exchange_num = one_company_info[0]
        stock_num = one_company_info[1]
        stock_name = one_company_info[2]
        # 检查名字是否变动
        check_result = check_is_change(stock_num, stock_name)
        if check_result is False:
            continue
        # 通过接口调用曾用名
        ever_name = pro.namechange(ts_code=one_company_info[0], fields='ts_code,name')
        # 拼接曾用名字符串
        name_list = ''
        for one_name in ever_name['name'].values:
            name_list = name_list + "," + one_name

        start_two_word = one_company_info[2][0:2]
        # 检查名字开头是否以地名开头，如果不是，添加名字开头两个子为简称
        if filter_name(start_two_word) == 1:
            short_name = start_two_word
        else:
            short_name = ''

        models.save_company_name(stock_num, stock_exchange_num, stock_name, name_list, short_name)
        # company_name_info.
        # current_dic.append(str_entity)
        time.sleep(0.5)
    # 清空所有的公司名称字符串


if __name__ == '__main__':
    write_company_name_to_sql()
