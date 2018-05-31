# code = utf-8

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect, pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QMessageBox,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             QPushButton, QLabel, QLineEdit)
import socket
import re

class Ui_MainWindow(QMainWindow):

    def __init__(self):

        # 调用父类 __init__()
        super().__init__()

        # 状态栏信息
        self.status_bar_message = ''

        # 初始化UI
        self.initUI()


    def initUI(self):
        '''
        connWidget：dst_ip + dst_port
        statusBar: 最底下的状态栏
        '''

        # mainWidget
        self.mainWidget = QWidget(self)
        self.mainWidget.setObjectName('mainWidget')

        # add connWidget
        self.connWidget()

        self.setCentralWidget(self.mainWidget)


        # 状态栏，位于最下方
        self.statusBar().showMessage(self.status_bar_message)

        # 左 上 宽 高
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle('HttpTestClient')
        self.show()

    def connWidget(self):
        '''
        hostPortLabel: Host:Port
        hostPortEdit: 编辑 dst_ip:dst_port
        connButton: 点击
            检查 ip:port 格式是否正确
            创建 TCP connection 发送 HTTP 请求
        '''

        # connWiget
        self.connWidget = QWidget(self.mainWidget)
        self.connWidget.setObjectName('connWidget')
        self.connWidget.setGeometry(QRect(0, 0, 350, 45))

        # connLayeout
        self.connLayout = QGridLayout(self.connWidget)
        self.connLayout.setObjectName('connLayout')

        # Host:Port Connect_button with connection_message

        ## hostPortLabel
        self.hostPortLabel = QLabel('Host:Port', self.connWidget)
        self.hostPortLabel.setFont(self.labelFont())

        ## hostPortEdit
        self.hostPortEdit = QLineEdit(self.connWidget)
        self.hostPortEdit.setObjectName('hostPortEdit')
        self.hostPortEdit.setText('1.1.1.1:80')
        #self.hostPortEdit.editingFinished.connect(self.hostPortCheck())

        ## connButton
        self.connButton = QPushButton('发送请求', self.connWidget)
        self.connButton.setObjectName('connButton')
        self.connButton.clicked.connect(self.connButtonClick)

        self.connLayout.addWidget(self.hostPortLabel, 0, 0, 1, 1)
        self.connLayout.addWidget(self.hostPortEdit, 0, 1, 1, 1)
        self.connLayout.addWidget(self.connButton, 0, 2, 1, 1)

        self.setLayout(self.connLayout)

    def connButtonClick(self):

        ip_port, ok = self.hostPortCheck(self.hostPortEdit.text())

        if ok:
            self.status_bar_message = 'IP:Port格式正确, ' + ip_port

        else:
            self.status_bar_message = 'IP:Port格式错误, ' + ip_port

        self.statusBar().showMessage(self.status_bar_message)




    def labelFont(self):
        '''
        Label 字体样式
        :return: font
        '''
        font = QFont()
        font.setBold(True)
        return font

    def hostPortCheck(self, text):
        '''
        检查 ip:port 格式
        :param text: hostPortEdit 输入的内容
        :return: True/False
        '''

        # check IP and port format

        hostPortString = text
        hostPortList = hostPortString.split(":")
        result = True

        if len(hostPortList) != 2:
            result = False
        else:
            address = hostPortList[0].strip()
            port = hostPortList[1].strip()
            number = re.match(r"(\d+$)", port)
            if number == None:
                # illegal port
                result = False
            else:
                # legal port

                try:
                    # legal IP address
                    socket.inet_aton(address)
                except socket.error:
                    # illegal IP address
                    result = False
        return (hostPortString.strip(), result)



