from LocalDicManager import models
import tushare as ts


def write_industry_to_sql():
    models.delete_all_industry()
    pro = ts.pro_api('65d978be5ed23ecc8e71f573fea23125ba1319fe6838ce50e9243242')

    # 得到所有实体
    tuples = []
    df = pro.index_classify(level='L1', src='SW')
    info = [tuple(xi) for xi in df.values]

    # 获取申万二级行业列表
    for one in info:
        tuples.append(one)

    df = pro.index_classify(level='L2', src='SW')
    info = [tuple(xi) for xi in df.values]
    for one in info:
        tuples.append(one)

    # 获取申万三级级行业列表
    df = pro.index_classify(level='L3', src='SW')
    info = [tuple(xi) for xi in df.values]
    for one in info:
        tuples.append(one)

    for one in tuples:
        models.save_industry(one[0], one[1], one[2])
