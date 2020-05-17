from Neo4j import base_dao


def find_all_finance_index_by_date(report_data):
    """
    :param report_data:
    :return:
    """

    index = base_dao.match_where("财务指标名称", "报告期", report_data)
    finance_index_tuples = {}
    for one in index:
        stock_code = one['TS代码'].replace(".SH", "").replace(".SZ", "")
        tmp = {
            stock_code: one
        }
        finance_index_tuples.update(tmp)
    return finance_index_tuples


def load_all_finance_index_by_date(report_date):
    """
    :param report_date:
    :return:
    """
    return find_all_finance_index_by_date(report_date)
