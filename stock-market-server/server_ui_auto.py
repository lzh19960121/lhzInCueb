# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import datetime
import sys
import threading
import time
from socket import socket, AF_INET, SOCK_STREAM
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import util
from filter import Filter
from websocket_server import WebsocketServer
import numpy


class FilterConfig(object):
    # 第二层过滤
    raise_fall_zone_fall = 1
    raise_fall_zone_rise = 1
    # 价格差
    price_gap_value = 1
    # 瞬时涨
    instant_rise_value = 1
    # 瞬时跌
    instant_fall_value = -1
    # 分钟涨跌速度
    rise_in_minute_value = -1
    fall_in_minute_value = -1


class Ui_MainWindow(object):
    # Called for every client connecting (after handshake)
    def __init__(self):
        self.new_filter = None

    def new_client(self, client, server):
        self.listWidget_ip.addItem(util.get_time_ymd_hms() + "New client connected and was given id %d" % client['id'])

    # Called for every client disconnecting
    def client_left(self, client, server):
        self.listWidget_ip.addItem(util.get_time_ymd_hms() + "Client(%d) disconnected" % client['id'])

    # Called when a client sends a message
    def message_received(self, client, server, message):
        if len(message) > 200:
            message = message[:200] + '..'
        print("Client(%d) said: %s" % (client['id'], message))
        server.send_message_to_all("sadsadad")

    def set_server(self):
        PORT = 8444
        self.server = WebsocketServer(PORT)
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received)

    def setupUi(self, MainWindow):
        # 启动服务器
        threading.Thread(target=self.set_server).start()
        # 启动时间监听
        threading.Thread(target=self.check_need_running).start()

        MainWindow.setObjectName("过滤器服务端")
        MainWindow.resize(882, 728)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(810, 20, 61, 31))
        self.btn_send_test = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_test.setGeometry(QtCore.QRect(610, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.btn_send_test.setFont(font)
        self.btn_send_test.setObjectName("btn_send_test")
        self.listWidget_ip = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_ip.setGeometry(QtCore.QRect(530, 60, 341, 621))
        self.listWidget_ip.setObjectName("listWidget_ip")

        self.line_gap_price = QtWidgets.QLineEdit(self.centralwidget)
        self.line_gap_price.setGeometry(QtCore.QRect(230, 109, 61, 21))
        self.line_test = QtWidgets.QLineEdit(self.centralwidget)
        self.line_test.setGeometry(QtCore.QRect(230, 20, 61, 21))
        self.line_test2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_test2.setGeometry(QtCore.QRect(130, 20, 61, 21))
        self.line_gap_price.setObjectName("line_gap_price")
        self.line_instant_rise = QtWidgets.QLineEdit(self.centralwidget)
        self.line_instant_rise.setGeometry(QtCore.QRect(230, 150, 61, 20))
        self.line_instant_rise.setObjectName("line_instant_rise")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_instant_fall = QtWidgets.QLineEdit(self.centralwidget)
        self.line_instant_fall.setGeometry(QtCore.QRect(230, 190, 61, 20))
        self.line_instant_fall.setObjectName("line_instant_fall")
        self.line_minute_rise = QtWidgets.QLineEdit(self.centralwidget)
        self.line_minute_rise.setGeometry(QtCore.QRect(230, 230, 61, 20))
        self.line_minute_rise.setObjectName("line_minute_rise")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 181, 20))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_minute_fall = QtWidgets.QLineEdit(self.centralwidget)
        self.line_minute_fall.setGeometry(QtCore.QRect(230, 260, 61, 21))
        self.line_minute_fall.setObjectName("line_minute_fall")
        self.btn_end = QtWidgets.QPushButton(self.centralwidget)
        self.btn_end.setGeometry(QtCore.QRect(530, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.btn_end.setFont(font)
        self.btn_end.setObjectName("btn_end")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "开始"))

        self.line_gap_price.setText(_translate("MainWindow", "1"))
        self.line_instant_rise.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "涨跌过滤（区间）"))
        self.label_2.setText(_translate("MainWindow", "差价（%）"))
        self.label_3.setText(_translate("MainWindow", "瞬时增长（%）"))
        self.label_4.setText(_translate("MainWindow", "顺势下跌（%）"))
        self.label_5.setText(_translate("MainWindow", "分钟增长（%）"))
        self.line_instant_fall.setText(_translate("MainWindow", "-1"))
        self.line_minute_rise.setText(_translate("MainWindow", "0.75"))
        self.label_6.setText(_translate("MainWindow", "分钟下跌（%）"))
        self.line_minute_fall.setText(_translate("MainWindow", "-1"))
        self.btn_end.setText(_translate("MainWindow", "停止"))
        self.btn_send_test.setText(_translate("MainWindow", "测试发送"))
        self.btn_send_test.clicked.connect(self.send_test)
        self.btn_start.clicked.connect(self.start)
        self.btn_end.clicked.connect(self.end)

    def check_today_data(self):
        while True:
            try:
                print(1)
                size_str = util.read_one_file(
                    r"C:\Users\hangqing1\Desktop\bin423\ShareMem.txt",
                    'gbk')[0]
                date_str, size = size_str.split('=')
                if date_str != util.get_today_date():
                    
                    continue
                else:
                    self.listWidget_ip.addItem(util.get_today_time() +
                                               "发现更新数据")
                    self.start_filter(size)
                    break
                
            except Exception as e:
                print(e)

    def start(self):
        size_str = util.read_one_file(
            r"C:\Users\hangqing1\Desktop\bin423\ShareMem.txt",
            'gbk')[0]
        date_str, size = size_str.split('=')
        self.listWidget_ip.addItem(util.get_today_time() +
                                   "等待数据加载")
        print(date_str != util.get_today_date())
        if date_str != util.get_today_date():
            threading.Thread(target=self.check_today_data).start()
        else:
            self.start_filter(size)

    def start_filter(self, size):
        threading.Thread(target=self.server.run_forever).start()
        filter_conf = FilterConfig()
        filter_conf.price_gap_value = float(self.line_gap_price.text().strip())
        filter_conf.instant_rise_value = float(self.line_instant_rise.text().strip())
        filter_conf.instant_fall_value = float(self.line_instant_fall.text().strip())
        filter_conf.rise_in_minute_value = float(self.line_minute_rise.text().strip())
        filter_conf.fall_in_minute_value = float(self.line_minute_fall.text().strip())
        self.listWidget_ip.addItem(str(filter_conf.__dict__))
        self.new_filter = Filter(self.server, filter_conf)
        self.listWidget_ip.addItem("开始")
        filter_thread = threading.Thread(target=self.new_filter.run_filter, args=(int(size),))
        filter_thread.start()
        self.listWidget_ip.addItem("过滤器开始启动")

        # 开启滚动条最下线程

    def check_need_running(self):
        
        while True:
            time.sleep(3)
            d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:22', '%Y-%m-%d%H:%M')
            d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '15:10', '%Y-%m-%d%H:%M')
            n_time = datetime.datetime.now()
            
            # 判断当前时间是否在范围时间内
            if d_time < n_time < d_time1:
                self.label_7.setText("交易时间范围内")
                if self.new_filter is None:
                    threading.Thread(target=self.start).start()
                else:
                    time.sleep(50)
                   
            else:
                self.label_7.setText("不在交易时间范围内")
                if self.new_filter is not None:
                    self.new_filter.filter_flag = False
                    self.listWidget_ip.addItem("不在开盘时间，停止今日监控")
                    self.new_filter = None
                else:
                    time.sleep(50)
                    
            

    def send_test(self):
        self.server.send_message_to_all(
            "test^test^test^test^test^test^0.5^" + self.line_test2.text() + "^" + self.line_test.text())

    def end(self):
        self.new_filter.filter_flag = False
        self.listWidget_ip.addItem("不在开盘时间，停止今日监控")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
