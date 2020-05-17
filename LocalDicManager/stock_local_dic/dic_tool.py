import datetime
import importlib
import threading
import time
from imp import reload



def update_dic():
    while 1:
        try:
            now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            if now[11:16] == '14:32':
                print('**************************************************开始更新字典*****'
                      '*********************************************')
                module = importlib.import_module('LocalDicManager.make_stock_info_dic.' + 'writer_local_dic')
                module.write_dic()
                print("结束")
                time.sleep(50)
        except Exception as e:
            print(e)


def load_data():
    print("**************************************开启子线程，定时重载字典**************************************************")
    while 1:
        try:
            now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            if now[11:16] == '19:25':
                print('**************************************************开始加载字典*********'
                      '*****************************************')
                module = importlib.import_module('LocalDicManager.stock_local_dic.' + 'stock_dic')
                reload(module)
                print("结束")
            if now[11:16] == '14:25':
                print('**************************************************开始更新字典*****'
                      '*********************************************')
                module = importlib.import_module('LocalDicManager.make_stock_info_dic.' + 'writer_local_dic')
                module.write_dic()
                print("结束")
                time.sleep(50)
            time.sleep(50)
        except Exception as e:
            print(e)


print("**************************************开启子线程，定时重载字典**************************************************")
load_local_data = threading.Thread(target=load_data)
load_local_data.start()


# print("**************************************开启子线程，定时更新字典**************************************************")
# update_dic = threading.Thread(target=update_dic)
# update_dic.start()
