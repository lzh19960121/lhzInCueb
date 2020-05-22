# 代码，股票名称，买一价格，买一数量，卖一价格，卖一量，成交价格，成交量，高低位转换，类别
import datetime
# 代码，股票名称，买一价格，买一数量，卖一价格，卖一量，成交价格，成交量
# one_infos[0], one_infos[1], one_infos[3],
# one_infos[4], one_infos[5], one_infos[6],
# one_infos[7], one_infos[8]
# 用涨跌（幅度）过滤，比如幅度大于某个阈值就不处理。
from data_resource import read_memory
import time
import util
from data_save.db import MysqlHelper
from minute_rise_fall_filter.minute_rise_fall_filter import MinuteRiseFallFilter
mysql = MysqlHelper('127.0.0.1:3306', 'root', '000000', 'filter_result', 'utf-8')
minutes_events = []



def make_difference(list1, list2):
    """
    :param list1: 列表1
    :param list2:
    :return:
    """
    # 求两个字符串列表的差集
    return set(list1).difference(set(list2))


class FilterEventTypeConfig(object):
    """
    过滤器的事件类型
    """
    gap_price_type = "1"
    instant_rise = '2'
    instant_fall = '3'
    minute_rise = '4'
    minute_fall = '5'


class Filter(object):
    def __init__(self, server, filter_border_value):
        self.filter_event_config = FilterEventTypeConfig()
        # 上个时刻价格差的字符串
        self.pre_time_gap_price_need_data = []
        # 上个时刻的涨跌的字符串
        self.pre_time_instant_need_data = []
        # 上个时刻全部信息的字符串
        self.full_real_time_info = []
        self.pre_full_real_time_info = []
        # 当前时刻和上个时买入和卖出价格差差异
        self.gap_price_difference = []
        # 当前时刻和上个时刻瞬时涨跌价格差异
        self.instant_difference = []
        # 进行过滤器初始化
        self.gap_price_need_data = []
        # 当前时刻的成交价格所需的数据
        self.instant_need_data = []
        # 初始化数据
        self.server = server
        # 过滤器运行的标志
        self.filter_flag = True
        # 加载过滤器的配置
        self.filter_border_value = filter_border_value
        self.filter = []

    def init_filter(self, initial_data):
        """
        :param initial_data: 初始化的数据
        :return:
        """
        self.filter.append(MinuteRiseFallFilter(self.server, initial_data, 10, self.filter_event_config, self.filter_border_value))

    def delete_unchanged(self):
        """
        :return:
        """
        self.gap_price_difference = make_difference(self.gap_price_need_data, self.pre_time_gap_price_need_data)
        self.instant_difference = make_difference(self.instant_need_data, self.pre_time_instant_need_data)

    def load_info(self, size):
        """
        :param size:
        :return:
        """
        self.gap_price_need_data = []
        self.instant_need_data = []
        self.full_real_time_info = read_memory.get_info_from_memory(size)
        # 先用set去重,把当前的和上次的对比，直接字符串去差集效率较高
        change_one_file_info = make_difference(self.full_real_time_info, self.pre_full_real_time_info)
        # 代码，股票名称，买一价格，买一数量，卖一价格，卖一量，成交价格，成交量，高低位转换，类别
        print("更新了" + str(len(change_one_file_info)))
        for one_line in change_one_file_info:
            stock_num, stock_name, time_str, buy_price, buy_volume, sale_price, sale_volume, price, volume, fall_rise, stock_type = one_line.split(
                ',')
            price = int(price) / 1000
            fall_rise = int(fall_rise) / 100
            if volume == '0':
                continue
            if "ST" in stock_name:
                continue
            if price == 0 or fall_rise == 0:
                continue
            # 如果涨跌不在区间内，将不显示
            info_str = util.get_today_time() + "^" + time_str + "^" + stock_name + '^' + stock_num + "^" + str(
                price) + "^" + volume + "^" + str(fall_rise) + "^"
            self.gap_price_need_data.append(info_str + "," + stock_num + "," + sale_price + "," + buy_price)
            self.instant_need_data.append(info_str + "," + stock_num + "," + str(price * 1000))

    def run_filter(self, size):
        """
        :return:
        """
        init_data = read_memory.get_info_from_memory(size)
        self.init_filter(init_data)
        while self.filter_flag:

            # try:
                time.sleep(2)
                oldtime = datetime.datetime.now()
                # 加载数据
                self.load_info(size)
                # 此处使用哈希求差集
                self.delete_unchanged()
                # 运行过滤器
                for one in self.filter:
                    one.filter(self.instant_difference,self.full_real_time_info)
                # 更新上个时刻的数据
                self.pre_time_gap_price_need_data = self.gap_price_need_data
                self.pre_time_instant_need_data = self.instant_need_data
                self.pre_full_real_time_info = self.full_real_time_info
                newtime = datetime.datetime.now()
                print(u'处理一次数据：%s微秒' % (newtime - oldtime).microseconds)

            # except Exception as e:
            #     print(e)


