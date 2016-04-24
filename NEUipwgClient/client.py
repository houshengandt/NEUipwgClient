import sys
from PyQt5.QtWidgets import *
import urllib.error

from ui import *
from wg import *


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.createActions()
        self.createTrayIcon()
        self.trayIcon.setIcon(self.icon)
        self.trayIcon.show()

        self.trayIcon.activated.connect(self.trayClick)

        self.label_info.setText("<center><b>欢迎使用校园网客户端</b></center>")

        self.get_u_info_from_file()
        self.zdlj()

        self.pushButton_ljwl.clicked.connect(self.login_wg)
        self.pushButton_ljwl.clicked.connect(self.save_u_info)
        self.pushButton_dklj.clicked.connect(self.logout_wg)
        self.pushButton_dklj.clicked.connect(self.save_u_info)


#   界面操作，最小化、隐藏到托盘等

    def trayClick(self, reason):
        if reason == self.trayIcon.Critical:
            self.showNormal()

    def createActions(self):
        self.restoreAction = QAction("&显示", self, triggered=self.showNormal)
        self.quitAction = QAction("&退出", self, triggered=self.quit_entire)

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.showMessage("最小化", "已隐藏到系统托盘，从这里退出", 0, 1)
            # QMessageBox.information(self, "最小化", "已隐藏到系统托盘，从这里退出")
            self.hide()
            event.ignore()

    def createTrayIcon(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)


    def quit_entire(self):
        self.trayIcon.setVisible(False)
        QApplication.instance().quit()



    def zdlj(self):
        if self.checkBox_zdlj.isChecked():
            self.login_wg()


#   网络操作，连接、断开、存储密码、开启Wi-Fi等

    def login_wg(self):
        u_name = self.lineEdit_xywzh.text()
        u_password = self.lineEdit_xywmm.text()
        try:
            IpWg().login(u_name, u_password)
        except urllib.error.HTTPError as e:
            self.label_info.setText("<b><center>连接失败</center><br><center>服务器未响应</center><br><br>&nbsp;&nbsp;"
                                    "试试从网页登陆IP网<br>&nbsp;&nbsp;关或其他校内服务，<br>&nbsp;&nbsp;并关注网络中心黑板"
                                    "报<br>&nbsp;&nbsp;最新通知</b>")
        except urllib.error.URLError as e:
            self.label_info.setText("<b><center>连接失败</center><br><center>无法连接到服务器</center><br><br>&nbsp;&nbsp;"
                                    "可能不在校园网环境，<br>&nbsp;&nbsp;试试从网页登陆IP网<br>&nbsp;&nbsp;关或其他校内服务，"
                                    "<br>&nbsp;&nbsp;检查网线是否插好</b>")
        else:
            u_info = IpWg().get_user_info()
            ll, sc, ye, *z, ip = re.split(r'[,\s]\s*', str(u_info, "utf-8"))
            ll = format(int(ll)/1000000, '0.2f')
            sc = format(int(sc)/3600, '0.2f')
            self.label_info.setText("<b><center>连接成功</center><br>&nbsp;&nbsp;已用流量：" + str(ll) + "M<br>&nbsp;"
                                    "&nbsp;已用时长：" + str(sc) + "小时<br>&nbsp;&nbsp;余额：" + ye + "元<br>&nbsp;"
                                    "&nbsp;IP:" + ip + "</b>")

    def logout_wg(self):
        u_name = self.lineEdit_xywzh.text()
        u_password = self.lineEdit_xywmm.text()
        try:
            IpWg().logout(u_name, u_password)
        except urllib.error.HTTPError as e:
            self.label_info.setText("<b><center>断开连接失败</center><br><center>服务器未响应</center><br><br>&nbsp;&nbsp;"
                                    "试试从网页登陆Ip网<br>&nbsp;&nbsp;关或其他校内服务，并<br>&nbsp;&nbsp;关注网络中心黑板报"
                                    "最<br>&nbsp;&nbsp;新通知</b>")
        except urllib.error.URLError as e:
            self.label_info.setText("<b><center>断开连接失败</center><br><center>无法连接到服务器</center><br><br>&nbsp;"
                                    "&nbsp;可能离开了校园网环境，<br>&nbsp;&nbsp;试试从网页登陆IP网<br>&nbsp;&nbsp;关或其他"
                                    "校内服务，检<br>&nbsp;&nbsp;查网线是否插好</b>")
        else:
            self.label_info.setText("<center><b>已断开校园网</b></center>")

    def save_u_info(self):
        u_name = self.lineEdit_xywzh.text()
        u_password = self.lineEdit_xywmm.text()
        if self.checkBox_zdlj.isChecked():
            zdljornot = '1'
        else:
            zdljornot = '0'
        u_info = u_name + ',' + u_password + ',' + zdljornot
        with open('doc.txt', 'wt') as g:
            g.write(u_info)

    def get_u_info_from_file(self):
        with open('doc.txt', 'rt') as h:
            u_info_from_file = h.read()
            u_name_from_file, u_passeord_from_file, zdlj_from_file = re.split(r'[,\s]\s*', u_info_from_file)
            self.lineEdit_xywzh.setText(u_name_from_file)
            self.lineEdit_xywmm.setText(u_passeord_from_file)
            self.checkBox_zdlj.setChecked(int(zdlj_from_file))



if __name__ == "__main__":
    IpWg().data_file()
    chdir("c:\\IPWG")
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())