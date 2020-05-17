import io
import csv
import threading
import numpy as np
import os
import re


# ------------------------------------------------文件读写类工具--------------------------------------------------------#

# author:刘华振
# 功能：读取一个csv，返回csv内的内容
def read_one_csv_first_column(csv_path: str):
    """
    :param csv_path:csv的路径
    :return: csv第一列信息
    """
    with io.open(csv_path, "r", encoding='utf-8')as g:
        g_reader = csv.reader(g)
        csv_info = []  # 用来存储csv
        for one_line in enumerate(g_reader):  # 抽取迭代器内行信息
            if len(one_line[1]):  # 抽取非空行信息
                csv_info.append(one_line[1][0])
    return csv_info


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


def save_csv_file(row_info, file_name):  # 写入文件
    """"
    # author:刘华振
    # 写入csv文件
    :param row_info: 行信息
    :param file_name: 文件名称
    :return:
    """
    csv_file = open(file_name + '.csv', "a", newline='', encoding='utf-8')  # 写入文件中
    file_writer = csv.writer(csv_file)
    file_writer.writerow(row_info)


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
        return lines


def is_in_dict(need_match_line, path):
    """
    # 查看文件是否含有相等的字符，一般用来匹配
    :param need_match_line:
    :param path:
    :return:
    """
    all_content = read_one_file(path)  # 在此句话中搜索信息
    for one in all_content:
        if need_match_line == one:
            return True
    return False


# ------------------------------------------------常用操作类--------------------------------------------------------#


# author:刘华振
# 功能：验证是否含有汉字
def is_contain_chinese(word: str):
    """
    :param word: 传入字符串
    :return: 是否是汉字
    """
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# author:刘华振
# 功能：验证是否含有数字
def is_contain_number(word: str):
    return bool(re.search(r'\d', word))


# 列表操作类-------------------------------------------------------------------------
# 去重 此方法很笨重
def delete_repeat(lists: list):
    new_list = []
    for one in lists:
        if one != new_list:
            new_list.append(one)
    return new_list


# author:刘华振
# 功能：运用多线程运行任务
def use_thread_run(function_name, num_of_threading, function_need_param):
    """
    :param num_of_threading: 开多少线程
    :param function_name: 传入函数名称
    :param function_need_param: 线程需要的参数（一般指股票列表）
    :return:
    """
    li = np.array(function_need_param)  # 将列表转成adarry数据
    report_path = np.array_split(li, num_of_threading)
    threads = []
    for one_list in report_path:
        t = threading.Thread(target=function_name, args=(one_list,))
        threads.append(t)
    for t in threads:
        t.start()
    for e in threads:  # 等待所有线程结束
        e.join()
