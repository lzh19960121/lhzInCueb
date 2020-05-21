# 代码，股票名称，买一价格，买一数量，卖一价格，卖一量，成交价格，成交量，高低位转换，类别
import datetime
# 代码，股票名称，买一价格，买一数量，卖一价格，卖一量，成交价格，成交量
# one_infos[0], one_infos[1], one_infos[3],
# one_infos[4], one_infos[5], one_infos[6],
# one_infos[7], one_infos[8]
# 用涨跌（幅度）过滤，比如幅度大于某个阈值就不处理。
import read
import threading
import time
import util
from db import MysqlHelper

# 代码，股票名称，买一价格，买一数量，卖一价格，卖一量，成交价格，成交量
# one_infos[0], one_infos[1], one_infos[3],
# one_infos[4], one_infos[5], one_infos[6],
# one_infos[7], one_infos[8]
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


class RiseFallTimes(object):
    """
    计数器
    """
    # 没精力优化了，copy paste
    stock_num = ''
    instant_rise_times = 0
    instant_fall_times = 0

    one_minute_rise_times = 0
    two_minute_rise_times = 0
    three_minute_rise_times = 0
    four_minute_rise_times = 0
    five_minute_rise_times = 0

    one_minute_fall_times = 0
    two_minute_fall_times = 0
    three_minute_fall_times = 0
    four_minute_fall_times = 0
    five_minute_fall_times = 0

    def save_event(self, event_times, minutes_num):
        time_str = util.get_time_ymd_hms()
        time_str = time_str + "-" + util.datetime_pre_minutes(time_str, minutes_num)
        record = time_str + "," + self.stock_num + "," + str(event_times) + "," + str(minutes_num)
        minutes_events.append(record)

    def one_minute_times_be_zero(self):
        """
        分钟结束的时候，把次数记录
        :return:
        """
        if self.one_minute_rise_times != 0:
            self.save_event(self.one_minute_rise_times, 1)
        if self.one_minute_fall_times != 0:
            self.save_event(self.one_minute_fall_times, 1)
        self.one_minute_rise_times = 0
        self.one_minute_fall_times = 0

    def two_minute_times_be_zero(self):
        if self.two_minute_rise_times != 0:
            self.save_event(self.two_minute_rise_times, 2)
        if self.two_minute_fall_times != 0:
            self.save_event(self.two_minute_fall_times, 2)

        self.two_minute_rise_times = 0
        self.two_minute_fall_times = 0

    def three_minute_times_be_zero(self):
        if self.one_minute_rise_times != 0:
            self.save_event(self.two_minute_rise_times, 3)
        if self.one_minute_fall_times != 0:
            self.save_event(self.two_minute_fall_times, 3)
        self.three_minute_rise_times = 0
        self.three_minute_fall_times = 0

    def four_minute_times_be_zero(self):
        if self.four_minute_rise_times != 0:
            self.save_event(self.four_minute_rise_times, 4)
        if self.four_minute_fall_times != 0:
            self.save_event(self.four_minute_fall_times, 4)
        self.four_minute_rise_times = 0
        self.four_minute_fall_times = 0

    def five_minute_times_be_zero(self):
        if self.five_minute_rise_times != 0:
            self.save_event(self.five_minute_rise_times, 5)
        if self.five_minute_fall_times != 0:
            self.save_event(self.five_minute_fall_times, 5)
        self.five_minute_rise_times = 0
        self.five_minute_fall_times = 0


class Filter(object):

    def __init__(self, server, FilterConfig):
        self.filter_event_config = FilterEventTypeConfig()
        # 上个时刻价格
        self.pre_time_price = {}
        # 上个时刻的价格差
        self.pre_gap_price = {}
        # 1分钟开始价格
        self.minute_begin_price = {}
        # 2分钟开始价格
        self.two_minute_begin_price = {}
        # 3分钟开始价格
        self.three_minute_begin_price = {}
        # 4分钟开始价格
        self.four_minute_begin_price = {}
        # 5分钟开始价格
        self.five_minute_begin_price = {}
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
        self.FilterConfig = FilterConfig
        self.filter_result = []
        self.rise_fall_times = []  # type:list[RiseFallTimes]

    def minute_fall_or_raise_filter(self):
        self.minute_fall_or_raise("1", self.minute_begin_price)

    def two_minute_fall_or_raise_filter(self):
        self.minute_fall_or_raise("2", self.two_minute_begin_price)

    def three_minute_fall_or_raise_filter(self):
        self.minute_fall_or_raise("3", self.three_minute_begin_price)

    def four_minute_fall_or_raise_filter(self):
        self.minute_fall_or_raise("4", self.four_minute_begin_price)

    def five_minute_fall_or_raise_filter(self):
        self.minute_fall_or_raise("5", self.five_minute_begin_price)

    def update_minute_rise_times(self, minute_name, stock_num):
        for one in self.rise_fall_times:
            if one.stock_num == stock_num:
                if minute_name == '1':
                    one.one_minute_rise_times = one.one_minute_rise_times + 1
                    return one.one_minute_rise_times
                if minute_name == '2':
                    one.two_minute_rise_times = one.two_minute_rise_times + 1
                    return one.two_minute_rise_times
                if minute_name == '3':
                    one.three_minute_rise_times = one.three_minute_rise_times + 1
                    return one.three_minute_rise_times
                if minute_name == '4':
                    one.four_minute_rise_times = one.four_minute_rise_times + 1
                    return one.four_minute_rise_times
                if minute_name == '5':
                    one.five_minute_rise_times = one.five_minute_rise_times + 1
                    return one.five_minute_rise_times

    def update_minute_fall_times(self, minute_name, stock_num):
        for one in self.rise_fall_times:
            if one.stock_num == stock_num:
                if minute_name == '1':
                    one.one_minute_fall_times = one.one_minute_fall_times - 1
                    return one.one_minute_fall_times
                if minute_name == '2':
                    one.two_minute_fall_times = one.two_minute_fall_times - 1
                    return one.two_minute_fall_times
                if minute_name == '3':
                    one.three_minute_fall_times = one.three_minute_fall_times - 1
                    return one.three_minute_fall_times
                if minute_name == '4':
                    one.four_minute_fall_times = one.four_minute_fall_times - 1
                    return one.four_minute_fall_times
                if minute_name == '5':
                    one.five_minute_fall_times = one.five_minute_fall_times - 1
                    return one.five_minute_fall_times

    def update_instant_rise_times(self, stock_num):
        for one in self.rise_fall_times:
            if one.stock_num == stock_num:
                one.instant_rise_times = one.instant_rise_times + 1
                return one.instant_rise_times

    def update_instant_fall_times(self, stock_num):
        for one in self.rise_fall_times:
            if one.stock_num == stock_num:
                one.instant_fall_times = one.instant_fall_times - 1
                return one.instant_fall_times

    def init_filter(self, initial_data):
        """
        :param initial_data: 初始化的数据
        :return:
        """
        for one_stock_info in initial_data:
            one_infos = one_stock_info.split(',')
            stock_num = one_infos[0]
            price = float(one_infos[7])
            self.pre_time_price[stock_num] = price
            self.pre_gap_price[stock_num] = 0
            self.minute_begin_price[stock_num] = price
            self.two_minute_begin_price[stock_num] = price
            self.three_minute_begin_price[stock_num] = price
            self.four_minute_begin_price[stock_num] = price
            self.five_minute_begin_price[stock_num] = price
            rise_fall_times = RiseFallTimes()
            rise_fall_times.stock_num = stock_num
            self.rise_fall_times.append(rise_fall_times)

    def gap_price_cal(self, sale_price: float, buy_price: float):
        """
        :param buy_price:
        :param sale_price:
        :return: 返回True ，表示过滤掉，否则返回差价
        """
        if buy_price == 0 or sale_price == 0:
            return False
        price_gap = (sale_price / 1000 - buy_price / 1000) / (buy_price / 1000) * 100
        if price_gap <= self.FilterConfig.price_gap_value:
            return False
        else:
            return price_gap

    def instant_raise_or_fall_cal(self, price: float, pre_price: float):
        """
        :param price:
        :param pre_price:
        :return: 返回True ，表示过滤掉，否则返回顺时增长
        """
        if price == 0 or pre_price == 0:
            return False
        if price - pre_price == 0:
            return False
        instant = (price / 1000 - pre_price / 1000) / (pre_price / 1000) * 100
        # 比较临界值
        if instant > 0:
            if instant >= self.FilterConfig.instant_rise_value:
                return instant
            else:
                return False
        else:
            if instant <= self.FilterConfig.instant_fall_value:
                return instant
            else:
                return False

    def minute_raise_or_fall_cal(self, begin_price: float, current_price: float):
        if begin_price == 0:
            return False, 0
        if begin_price - float(current_price) == 0:
            return False, 0
        dif = ((float(current_price) - begin_price) / begin_price) * 100
        if dif > 0:
            return dif >= self.FilterConfig.rise_in_minute_value, dif
        else:
            return dif <= self.FilterConfig.fall_in_minute_value, dif

    def gap_price_filter(self):
        """
        过滤掉差价
        :return:
        """
        for one_gap_dif in self.gap_price_difference:
            time_str, stock_num, sale_price, buy_price = one_gap_dif.split(',')
            gap_price_result = self.gap_price_cal(float(sale_price), float(buy_price))
            if gap_price_result is not False:
                gap_result = time_str + self.filter_event_config.gap_price_type + "^" + str(
                    format(gap_price_result, '.2f')) + "^" + str(1)
                self.server.send_message_to_all(gap_result)
                self.filter_result.append(gap_result)

    def instant_price_filter(self):
        for one_instant_dif in self.instant_difference:
            time_str, stock_num, current_price = one_instant_dif.split(',')
            pre_price = self.pre_time_price[stock_num]
            instant_rise_or_fall_result = self.instant_raise_or_fall_cal(float(current_price), pre_price)
            self.pre_time_price[stock_num] = float(current_price)
            if instant_rise_or_fall_result is not False:
                if instant_rise_or_fall_result > 0:
                    times = self.update_instant_rise_times(stock_num)
                    instant_result = time_str + self.filter_event_config.instant_rise + "^" + str(
                        format(instant_rise_or_fall_result, '.2f')) + "^" + str(times)
                else:
                    times = self.update_instant_fall_times(stock_num)
                    instant_result = time_str + self.filter_event_config.instant_fall + "^" + str(
                        format(instant_rise_or_fall_result, '.2f')) + "^" + str(times)
                self.server.send_message_to_all(instant_result)
                self.filter_result.append(instant_result)

    def minute_fall_or_raise(self, minute_name, begin_price_dic):
        for one_instant in self.instant_difference:
            time_str, stock_num, current_price = one_instant.split(',')
            begin_price = begin_price_dic[stock_num]
            minute_raise_or_fall_result, dif = self.minute_raise_or_fall_cal(begin_price, current_price)
            if minute_raise_or_fall_result is not False:
                if dif > 0:
                    times = self.update_minute_rise_times(minute_name, stock_num)
                    minute_result = time_str + self.filter_event_config.minute_rise + minute_name + "^" + str(
                        format(dif, '.2f')) + "^" + str(times)
                else:
                    times = self.update_minute_fall_times(minute_name, stock_num)
                    minute_result = time_str + self.filter_event_config.minute_fall + minute_name + "^" + str(
                        format(dif, '.2f')) + "^" + str(times)

                self.server.send_message_to_all(minute_result)
                self.filter_result.append(minute_result)

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
        self.full_real_time_info = read.get_info_from_memory(size)
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

    def cal_times(self):
        print(len(self.rise_fall_times))
        for one in self.rise_fall_times:
            util.write_text_apend(r"C:\Users\hangqing1\Desktop" + r"\\" + util.get_today_date()+"321",
                                  util.get_today_date() + "," +
                                  one.stock_num + "," + str(one.instant_fall_times) + "," + str(one.instant_rise_times))
        print(len(minutes_events))
        for one_e in minutes_events:
            util.write_text_apend(r"C:\Users\hangqing1\Desktop" + r"\\" + util.get_today_date()+"321",
                                  one_e)

    def record_minute_begin(self):
        minute_begin_price = {}
        for one_stock_info in self.full_real_time_info:
            one_infos = one_stock_info.split(',')
            stock_num = one_infos[0]
            price = float(one_infos[7])
            minute_begin_price[stock_num] = price
        return minute_begin_price

    def update_1minute_begin_info(self):
        # 用最low的方式
        while self.filter_flag:
            try:
                time.sleep(60)
                self.minute_begin_price = self.record_minute_begin()
                for one in self.rise_fall_times:
                    one.one_minute_times_be_zero()
            except Exception as e:
                print(e)

    def update_2minute_begin_info(self):
        # 用最low的方式
        while self.filter_flag:
            try:
                time.sleep(120)
                self.two_minute_begin_price = self.record_minute_begin()
                for one in self.rise_fall_times:
                    one.two_minute_times_be_zero()
            except Exception as e:
                print(e)

    def update_3minute_begin_info(self):
        while self.filter_flag:
            try:
                time.sleep(180)
                self.three_minute_begin_price = self.record_minute_begin()
                for one in self.rise_fall_times:
                    one.three_minute_times_be_zero()
            except Exception as e:
                print(e)

    def update_4minute_begin_info(self):
        while self.filter_flag:
            try:
                time.sleep(240)
                self.four_minute_begin_price = self.record_minute_begin()
                for one in self.rise_fall_times:
                    one.four_minute_times_be_zero()
            except Exception as e:
                print(e)

    def update_5minute_begin_info(self):
        while self.filter_flag:
            try:
                time.sleep(300)
                self.five_minute_begin_price = self.record_minute_begin()
                for one in self.rise_fall_times:
                    one.five_minute_times_be_zero()
            except Exception as e:
                print(e)

    def run_filter(self, size):
        """
        :return:
        """
        init_data = read.get_info_from_memory(size)
        self.init_filter(init_data)
        # threading.Thread(target=self.update_minute_begin_info).start()
        threading.Thread(target=self.update_1minute_begin_info).start()
        threading.Thread(target=self.update_2minute_begin_info).start()
        threading.Thread(target=self.update_3minute_begin_info).start()
        threading.Thread(target=self.update_4minute_begin_info).start()
        threading.Thread(target=self.update_5minute_begin_info).start()
        while self.filter_flag:
            try:
                oldtime = datetime.datetime.now()
                # 加载数据
                self.load_info(size)
                # 此处使用哈希求差集
                self.delete_unchanged()
                # 运行过滤器
                self.gap_price_filter()
                self.instant_price_filter()
                self.minute_fall_or_raise_filter()
                self.two_minute_fall_or_raise_filter()
                self.three_minute_fall_or_raise_filter()
                self.four_minute_fall_or_raise_filter()
                self.five_minute_fall_or_raise_filter()
                # 更新上个时刻的数据
                self.pre_time_gap_price_need_data = self.gap_price_need_data
                self.pre_time_instant_need_data = self.instant_need_data
                self.pre_full_real_time_info = self.full_real_time_info
                newtime = datetime.datetime.now()
                print(u'处理一次数据：%s微秒' % (newtime - oldtime).microseconds)
                time.sleep(2)
            except Exception as e:
                print(e)
        self.cal_times()
