import util


class MinuteRiseFallTimes(object):
    # 这种方法写起来虽然很笨，但是理解较为直观
    """
    计数器
    """
    # 股票列表
    stock_num_list = []  # type:list[str]
    # 分钟涨的次数
    minute_rise_times = {}  # type:dict
    # 分钟跌的次数
    minute_fall_times = {}  # type:dict
    # 今日分钟涨的分钟数
    today_minute_rise_occur_times = {}  # type:dict
    # 今日分钟跌的分钟数
    today_minute_fall_occur_times = {}  # type:dict

    def __init__(self, stock_num_list, how_many_minutes):
        self.stock_num_list = stock_num_list
        self.minutes_events = []
        # 装载每分钟的数据
        for one_stock_num in self.stock_num_list:
            for i in range(1, how_many_minutes + 1):
                self.minute_rise_times[str(i)][one_stock_num] = 0
                self.minute_fall_times[str(i)][one_stock_num] = 0
                self.today_minute_rise_occur_times[str(i)][one_stock_num] = 0
                self.today_minute_fall_occur_times[str(i)][one_stock_num] = 0

    def save_event(self, stock_num: str, event_times: int, minutes_num: int):
        """
        这个方法将在分钟结束的时候调用
        保存事件的次数
        :param stock_num: 股票代码
        :param event_times: 事件次数
        :param minutes_num: 分钟数
        :return:
        """
        if event_times == 0:
            return
        time_str_end = util.get_time_ymd_hms()
        time_str_start = str(util.datetime_pre_minutes(time_str_end, minutes_num))
        record = time_str_start + "," + time_str_end + "," + stock_num + "," + str(event_times) + "," + str(minutes_num)
        self.minutes_events.append(record)

    def minute_times_init(self, minute_nums):
        """
        #要两个步骤，先记录，后清零
        :param minute_nums: 分钟数
        :return:
        """
        for stock_num in self.stock_num_list:
            # 如果本分钟内发生了分钟涨，那么就记录后清零
            if self.minute_rise_times[str(minute_nums)][stock_num] != 0:
                self.save_event(stock_num, self.minute_rise_times[str(minute_nums)][stock_num], 1)
                self.today_minute_rise_occur_times[str(minute_nums)][stock_num] = \
                    self.today_minute_rise_occur_times[str(minute_nums)][
                        stock_num] + 1
            else:
                self.minute_rise_times[str(minute_nums)][stock_num] = 0

            # 如果本分钟内发生了分钟跌，那么就记录后清零
            if self.minute_fall_times[str(minute_nums)][stock_num] != 0:
                self.save_event(stock_num, self.minute_fall_times[str(minute_nums)][stock_num], 1)
                self.today_minute_fall_occur_times[str(minute_nums)][stock_num] = \
                    self.today_minute_fall_occur_times[str(minute_nums)][
                        stock_num] + 1
            else:
                self.minute_fall_times[str(minute_nums)][stock_num] = 0
