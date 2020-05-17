from AnswerApp import models
import tushare as ts

from Neo4j import base_dao


# 代码不具有维护性
def write_product_dic_to_sql():
    models.delete_all_product()
    pro = ts.pro_api('65d978be5ed23ecc8e71f573fea23125ba1319fe6838ce50e9243242')
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name')
    company_info = [tuple(xi) for xi in data.values]
    for ones in company_info:
        try:
            product = base_dao.get_one_company_to_relation_node(ones[1], '提供')
            if product is not None:
                for one in product:
                    print(one['产品'])
                    models.save_product(one['产品'])
        except Exception as e:
            print(e)
            pass
