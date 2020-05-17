from LocalDicManager import models
import tushare as ts


# Register your models here.


def write_concept_dic_to_sql():
    models.delete_all_concept()
    pro = ts.pro_api('65d978be5ed23ecc8e71f573fea23125ba1319fe6838ce50e9243242')
    data_gainian = pro.concept()
    data_gainian = [tuple(xi) for xi in data_gainian.values]
    # 打印概念列表
    for one in data_gainian:
        models.save_concept(one[0], one[1])
