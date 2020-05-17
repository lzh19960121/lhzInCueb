
from LocalDicManager.stock_local_dic.stock_dic import all_finance_index
from dic_help import find_all_finance_index_by_date


def get_one_company_finance_index(one_domain_num):
    """
    得到公司的财务指标
    :param one_domain_num:
    :return:
    """
    try :
        one_domain_num = one_domain_num.replace(".SH", "").replace(".SZ", "")
        index = all_finance_index[one_domain_num]
        return index
    except Exception as e:
        return 'notfound'


def load_all_finance_index_by_date(report_date):
    """

    :param report_date:
    :return:
    """
    return find_all_finance_index_by_date(report_date)


all_finance_index = load_all_finance_index_by_date("20190930")


