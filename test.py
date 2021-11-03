<<<<<<< HEAD
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class Window1(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 250, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 350, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 80, 741, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
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
        self.pushButton.setText(_translate("MainWindow", "поиск"))
        self.pushButton_3.setText(_translate("MainWindow", "редактирование и добавление"))
        self.label.setText(_translate("MainWindow", "ПРОЕКТЫ И КАЙЗЕНЫ"))


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')

    def show_window_1(self):
        self.w1 = Window1()
        self.w1.pushButton.clicked.connect(self.show_window_2)
        # self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show_window_1()
    sys.exit(app.exec_())
=======
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "), #test
        password=input("Пароль: "), #12345678
        database='main',
    ) as connection:
        cmd = """
            SELECT * FROM USERS;
        """

        with connection.cursor() as cursor:
            for r in cursor.execute(cmd, multi=True):
                print(r.fetchall())
            connection.commit()
except Error as e:
    print(e)
>>>>>>> origin/main
