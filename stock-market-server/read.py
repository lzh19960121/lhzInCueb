import mmap
import struct


def get_info_from_memory(size):
    """
    每天读入size，每条记录的大小为52
    :param size:
    :return:
    """
    current_info = []
    mp = mmap.mmap(-1, size, access=mmap.ACCESS_READ, tagname='ShareMem')
    point = 0
    for one in range(int(size / 52)):
        mp.seek(point)
        stock_num = mp.read(6).decode('gbk')
        point = point + 6
        mp.seek(point)
        stock_name = mp.read(8).decode('gbk')
        point = point + 8
        mp.seek(point)
        time_str = mp.read(6).decode('gbk')
        point = point + 6
        mp.seek(point)
        one_info = stock_num + ',' + stock_name + ',' + time_str
        result = struct.unpack('>iiiiiiii', mp.read(32))
        point = point + 32
        for one_int in result:
            one_info = one_info + ',' + str(one_int)
        current_info.append(one_info)
    return current_info




 