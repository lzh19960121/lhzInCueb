import datetime
from AnswerApp.stock_local_dic.make_stock_info_dic import company_manager, concept, product, industry, company_name
import time


# 代码不具有维护性

def write_dic():
    s = time.process_time()
    # 日更新
    print("concept")
    concept.write_concept_dic_to_sql()
    print("industry")
    industry.write_industry_to_sql()
    print("company_name")
    company_name.write_company_name_to_sql()
    print("product")
    product.write_product_dic_to_sql()

    now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

    print("company_manager")
    company_manager.write_manager_name_to_sql()
    e = time.process_time()
    print(s - e)

