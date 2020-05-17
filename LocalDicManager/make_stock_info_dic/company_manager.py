import time

from LocalDicManager import models
import tushare as ts
# Register your models here.
from Neo4j import base_dao
from Util import basic_util


# 代码不具有维护性
from dic_util import list_to_string


def write_manager_name_to_sql():
    #
    models.delete_all_company_manager()
    pro = ts.pro_api('65d978be5ed23ecc8e71f573fea23125ba1319fe6838ce50e9243242')
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name')
    company_info = [tuple(xi) for xi in data.values]
    for ones in company_info:
        try:
            names = base_dao.get_one_company_to_relation_node(ones[1], '是管理层')
            if len(names) == 0:
                continue
            one_line_list = []
            for one_n in names:
                one_line_list.append(one_n['姓名'])
            one_line_list = basic_util.delete_repeat(one_line_list)
            name_string = list_to_string(one_line_list)
            print(name_string)
            models.save_company_manager(ones[1], name_string)
            # time.sleep(0.8)
        except Exception as e:
            print(e)
            pass
