import time


import datetime


def ymd_hms_to_num(time_str):
    """
    年月日时分秒转化为毫秒
    :param time_str: 时间字符串
    :return:
    """
    datetime_obj = time.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    mk_time = int(time.mktime(datetime_obj) * 1000)
    return mk_time


def get_current_y_m_d_h_m_s():
    """
    得到当前时间，年月日时分秒
    :return:
    """
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


