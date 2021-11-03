import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QPlainTextEdit

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QPushButton, QLineEdit, \
    QPlainTextEdit, QMessageBox, QFileDialog, QComboBox





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Проекты и Кайзены")
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

        self.pushButton.clicked.connect(self.search)
        self.pushButton_3.clicked.connect(self.edit)

    def search(self):
        self.w2 = Window2()
        self.w2.show()

    def edit(self):
        self.w3 = Window3()
        self.w3.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "поиск"))
        self.pushButton_3.setText(_translate("MainWindow", "редактирование и добавление"))
        self.label.setText(_translate("MainWindow", "ПРОЕКТЫ И КАЙЗЕНЫ"))

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()

        font = QtGui.QFont()
        font.setPointSize(10)

        self.setWindowTitle('Поиск')
        self.setGeometry(100, 100, 750, 600)

        self.search = QPlainTextEdit(self)
        self.search.resize(410, 30)
        self.search.move(0, 0)

        self.combo = QComboBox(self)
        self.combo.addItem('Категории')
        self.combo.addItem('Проекты и Кайзены')
        self.combo.addItem('Работники')
        self.combo.setFont(font)
        self.combo.move(500, 0)
        self.combo.resize(100, 30)

        self.btn_search = QPushButton(self)
        self.btn_search.setText('Поиск')
        self.btn_search.setFont(font)
        self.btn_search.move(410, 0)
        self.btn_search.resize(90, 32)

        tableView = QTableView(self)
        tableView.resize(750, 400)
        tableView.move(0, 45)


class Window3(QWidget):
    def __init__(self):
        super(Window3, self).__init__()
        self.setWindowTitle('Редактирование')

        font = QtGui.QFont()
        font.setPointSize(10)

        self.setGeometry(100, 100, 750, 600)

        self.search = QPlainTextEdit(self)
        self.search.resize(410, 30)
        self.search.move(0, 0)

        self.combo = QComboBox(self)
        self.combo.addItem('Категории')
        self.combo.addItem('Проекты и Кайзены')
        self.combo.addItem('Работники')
        self.combo.setFont(font)
        self.combo.move(500, 0)
        self.combo.resize(100, 30)

        self.btn_search = QPushButton(self)
        self.btn_search.setText('Поиск')
        self.btn_search.setFont(font)
        self.btn_search.move(410, 0)
        self.btn_search.resize(90, 32)

        tableView = QTableView(self)
        tableView.resize(750, 400)
        tableView.move(0, 45)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
