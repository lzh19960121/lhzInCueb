from filter.minute_rise_fall_filter.rise_fall_times import MinuteRiseFallTimes
import threading
import time


class MinuteRiseFallFilter(object):
    def __init__(self, server, init_data, how_many_minutes, filter_event_config, filter_border_value):
        # 临界值
        self.filter_border_value = filter_border_value
        # 代表着过滤事件属于哪种类型
        self.filter_event_config = filter_event_config
        # 监听多少分钟的变化
        self.how_many_minutes = how_many_minutes
        self.server = server
        self.stock_num_list = []
        # 为了过滤高效
        self.current_need_data = []
        self.full_real_time_info = []
        self.filter_result = []
        self.run_flag = True
        # 分钟开始价格
        self.minute_begin_price = {}
        self.init_minute_begin_price(init_data)
        # 记录涨跌次数的类
        self.rise_fall_times = MinuteRiseFallTimes(self.stock_num_list, how_many_minutes)



    def init_minute_begin_price(self, init_data):
        """
        :param init_data:
        :return:
        """
        for one_stock_info in init_data:
            one_infos = one_stock_info.split(',')
            stock_num = one_infos[0]
            price = float(one_infos[7]) / 1000
            self.stock_num_list.append(stock_num)
            for i in range(1, self.how_many_minutes + 1):
                self.minute_begin_price[str(i)][stock_num] = price

    def start_minute_begin_price_update(self):
        """
        开始分钟初始价格的记录，以及每分钟情况的记录
        :return:
        """
        for i in range(1, self.how_many_minutes + 1):
            threading.Thread(target=self.update_minute_begin_info, args=(i,)).start()

    def add_minute_rise_times(self, minute_name, stock_num):
        self.rise_fall_times.minute_rise_times[minute_name][stock_num] = \
        self.rise_fall_times.minute_rise_times[minute_name][stock_num] - 1
        return self.rise_fall_times[minute_name][stock_num]

    def add_minute_fall_times(self, minute_name: str, stock_num):
        self.rise_fall_times.minute_fall_times[minute_name][stock_num] = \
        self.rise_fall_times.minute_fall_times[minute_name][stock_num] - 1
        return self.rise_fall_times[minute_name][stock_num]

    def minute_fall_or_raise(self, minute_name, begin_price_dic):
        for one_instant in self.current_need_data:
            time_str, stock_num, current_price = one_instant.split(',')
            begin_price = begin_price_dic[stock_num]
            minute_raise_or_fall_result, dif = self.minute_raise_or_fall_cal(begin_price, current_price)
            if minute_raise_or_fall_result is not False:
                if dif > 0:
                    times = self.add_minute_rise_times(minute_name, stock_num)
                    today_occur_times = self.rise_fall_times.today_minute_rise_occur_times[minute_name][stock_num]
                    minute_result = time_str + self.filter_event_config.minute_rise + minute_name + "^" + str(
                        format(dif, '.2f')) + "^" + str(times)+str(today_occur_times)
                else:
                    times = self.add_minute_fall_times(minute_name, stock_num)
                    minute_result = time_str + self.filter_event_config.minute_fall + minute_name + "^" + str(
                        format(dif, '.2f')) + "^" + str(times)

                self.server.send_message_to_all(minute_result)
                self.filter_result.append(minute_result)

    def minute_raise_or_fall_cal(self, begin_price: float, current_price: float):
        if begin_price == 0:
            return False, 0
        if begin_price - float(current_price) == 0:
            return False, 0
        dif = ((float(current_price) - begin_price) / begin_price) * 100
        if dif > 0:
            return dif >= self.filter_border_value.rise_in_minute_value, dif
        else:
            return dif <= self.filter_border_value.fall_in_minute_value, dif

    def record_minute_begin(self):
        minute_begin_price = {}
        for one_stock_info in self.full_real_time_info:
            one_infos = one_stock_info.split(',')
            stock_num = one_infos[0]
            price = float(one_infos[7])
            minute_begin_price[stock_num] = price
        return minute_begin_price

    def update_minute_begin_info(self, how_many_minutes):
        # 用最low的方式
        while self.run_flag:
            try:
                time.sleep(60 * how_many_minutes)
                self.minute_begin_price[str(how_many_minutes)] = self.record_minute_begin()
                self.rise_fall_times.minute_times_init(how_many_minutes)
            except Exception as e:
                print(e)

    def filter(self, current_need_data, full_real_time_info):
        self.current_need_data = current_need_data
        self.full_real_time_info = full_real_time_info
        for i in range(1, self.how_many_minutes + 1):
            self.minute_fall_or_raise(str(i), self.minute_begin_price[str(i)])

