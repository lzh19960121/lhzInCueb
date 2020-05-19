import os
import datetime
from functools import reduce


def get_today_date():
    return datetime.datetime.now().strftime('%Y%m%d')


def get_today_time():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def get_time_ymd_hms():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def StrToFloat(s):
    l = s.split('.')
    return reduce(lambda x, y: int(x) + int(y) / 10 ** len(y), l)


def write_text_apend(file_name, content):
    """
    # author:刘华振
    # 写入一行文件，追加的方式写入
    :param file_name: 文件名
    :param content: 内容
    :return: 空
    """
    with open(file_name, "a", encoding='utf-8') as f:
        f.writelines(content)
        f.writelines("\n")
        f.close()


def get_all_path(dirname: str, file_filter: str):
    """
    # author:刘华振
    # 功能得到文件夹下的全部文件路径
    :param dirname: 文件路径
    :param file_filter: 文件名后缀
    :return: 返回文路径列表
    """
    result = []  # 所有的文件路径
    for main_dir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            a_path = os.path.join(main_dir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(a_path)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext == file_filter:
                result.append(a_path)
    return result


def read_one_file(path: str, code: str):
    """
    # 读取一个txt类型的文件，得到字符串列表
    :param path: 路径
    :param code: 编码
    :return:
    """
    # author:刘华振
    # 读取一个txt类型的文件
    with open(path, 'r+', encoding=code) as f:
        lines = [line.strip() for line in f.readlines()]
        f.close()
        return lines  # type:list[str]
