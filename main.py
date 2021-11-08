import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QWidget, QPushButton, \
    QPlainTextEdit, QComboBox


a = ''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Проекты и Кайзены")
        MainWindow.resize(745, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 350, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 80, 741, 111))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 500, 191, 91))
        self.label_2.setObjectName("label_2")

        pixmap = QPixmap("logo.png")
        self.label_2.setPixmap(pixmap)

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
    def search(self):
        self.w2 = Window2()
        self.w2.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Работа с базой данных"))
        self.label.setText(_translate("MainWindow", "ПРОЕКТЫ И КАЙЗЕНЫ"))
class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setWindowTitle('Поиск')
        self.setGeometry(100, 100, 750, 600)
        self.search = QPlainTextEdit(self)
        self.search.resize(360, 30)
        self.search.move(0, 1)
        self.combo = QComboBox(self)
        self.combo.addItem('<Таблица не выбрана>')
        self.combo.addItem('Проекты и Кайзены')
        self.combo.addItem('Работники')
        self.combo.setFont(font)
        self.combo.move(500, 1)
        self.combo.resize(100, 30)
        self.combo1 = QComboBox(self)
        self.combo1.addItem('Критерии')
        self.combo1.setEnabled(False)
        self.combo1.setFont(font)
        self.combo1.move(600, 1)
        self.combo1.resize(150, 30)
        # self.btn_con = QPushButton(self)
        # self.btn_con.setText('✔')
        # self.btn_con.setFont(font)
        # self.btn_con.move(450, 0)
        # self.btn_con.resize(50, 32)
        # self.btn_con.clicked.connect(self.con1)
        self.btn_search = QPushButton(self)
        self.btn_search.setText('Поиск')
        self.btn_search.setFont(font)
        self.btn_search.move(360, 0)
        self.btn_search.resize(90, 32)
        self.btn_search.clicked.connect(self.refresh)
        self.btn_add = QPushButton(self)
        self.btn_add.setText('Добавить')
        self.btn_add.setFont(font)
        self.btn_add.move(300, 500)
        self.btn_add.resize(90, 32)
        self.btn_add.clicked.connect(self.add_1)
        self.btn_add.setEnabled(False)
        # self.btn_edit = QPushButton(self)
        # self.btn_edit.setText('Редактировать')
        # self.btn_edit.setFont(font)
        # self.btn_edit.move(295, 550)
        # self.btn_edit.resize(100, 32)
        # self.btn_edit.clicked.connect(self.edit)
        # self.btn_edit.setEnabled(False)
        #-----------------------------------------------
        db = QSqlDatabase.addDatabase('QSQLITE')
        self.tableView = QTableView(self)
        db.setDatabaseName('main.db')
        self.tableView.resize(750, 400)
        self.tableView.move(0, 45)
        self.tableView.setEnabled(False)
        print(db.open())
        self.model = QSqlTableModel(self)
        self.model.setTable("users")
        self.crit = self.search.toPlainText()
        self.model.select()
        self.tableView.setModel(self.model)
        self.con = sqlite3.connect('main.db')
        self.cur = self.con.cursor()
        self.tableView.setEnabled(True)
        self.combo.currentTextChanged.connect(self.refresh)
        self.combo.currentTextChanged.connect(self.con1)
    def edit(self):
        self.tableView.setEnabled(True)
    def add_1(self):
        self.w3 = Window3(self)
        self.w3.show()
    def con1(self):
        global a
        self.btn_add.setEnabled(True)
        self.combo1.setEnabled(True)
        self.btn_edit.setEnabled(True)
        self.combo1.clear()
        combotext = self.combo.currentText()
        if combotext == 'Работники':
            self.combo1.addItem('<Критерий не задан>')
            self.combo1.addItem('Ф.И.О работника')
            self.combo1.addItem('Должность')
            self.combo1.addItem('Проекты')
            self.update()
            a = 'Работники'
        else:
            self.combo1.addItem('<Критерий не задан>')
            self.combo1.addItem('тема')
            self.combo1.addItem('готовность')
            self.combo1.addItem('Место')
            self.combo1.addItem('Описание')
            self.combo1.addItem('автор')
            self.combo1.addItem('соавтор')
            self.update()
            a = 'Проекты'
    def refresh(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('main.db')
        db.open()
        self.model = QSqlTableModel(self)
        combotext = self.combo.currentText()
        combotext1 = self.combo1.currentText()
        self.setquery = QSqlQueryModel(self)
        if combotext == 'Работники':
            self.textEdit = self.search.toPlainText()
            print(self.textEdit)
            if combotext1 == 'Ф.И.О работника':
                self.setquery.setQuery(f'SELECT * FROM users WHERE name LIKE "%{self.textEdit}%"')
            elif combotext1 == 'Должность':
                self.setquery.setQuery(f'SELECT * FROM users WHERE role LIKE "%{self.textEdit}%"')
            elif combotext1 == 'Проекты':
                self.setquery.setQuery(f'SELECT * FROM users WHERE projs LIKE "%{self.textEdit}%"')
            else:
                self.setquery = self.model
            table = 'users'
        elif combotext == 'Проекты и Кайзены':
            self.textEdit = self.search.toPlainText()
            print(self.textEdit)
            if combotext1 == 'тема':
                self.setquery.setQuery(f'SELECT * FROM projects WHERE theme LIKE "%{self.textEdit}%"')
            elif combotext1 == 'готовность':
                self.setquery.setQuery(f'SELECT * FROM projects WHERE ready LIKE "%{self.textEdit}%"')
            elif combotext1 == 'место':
                self.setquery.setQuery(f'SELECT * FROM projects WHERE place LIKE "%{self.textEdit}%"')
            elif combotext1 == 'автор':
                self.setquery.setQuery(f'SELECT * FROM projects WHERE author LIKE "%{self.textEdit}%"')
            elif combotext1 == 'соавтор':
                self.setquery.setQuery(f'SELECT * FROM projects WHERE author2 LIKE "%{self.textEdit}%"')
            else:
                self.setquery = self.model
            table = 'projects'
        else:
            table = 'none'
        self.model.setTable(table)
        self.model.select()
        self.tableView.setModel(self.setquery)
        pass
class Window3(QWidget):
    def __init__(self, par):
        self.par = par
        super(Window3, self).__init__()
        self.setGeometry(100, 100, 410, 450)
        global a
        if a == "Проекты":
            self.setWindowTitle('Добавление')
            self.field = QPlainTextEdit(self)
            self.field.resize(410, 50)
            self.field.move(0, 20)
            self.label = QLabel(self)
            self.label.setText("Тема:")
            self.field1 = QPlainTextEdit(self)
            self.field1.resize(410, 50)
            self.field1.move(0, 120)
            self.label1 = QLabel(self)
            self.label1.setText("Место:")
            self.label1.move(0, 100)
            self.field2 = QPlainTextEdit(self)
            self.field2.resize(410, 50)
            self.field2.move(0, 220)
            self.label2 = QLabel(self)
            self.label2.setText("Описание:")
            self.label2.move(0, 200)
            self.con = sqlite3.connect('main.db')
            self.cur = self.con.cursor()
            # self.sp = []
            # for i in self.res:
            #     self.sp.append(i[0])
            self.field3 = QPlainTextEdit(self)
            self.field3.resize(410, 50)
            self.field3.move(0, 320)
            self.label3 = QLabel(self)
            self.label3.setText("Автор:")
            self.label3.move(0, 300)
            self.field4 = QPlainTextEdit(self)
            self.field4.resize(410, 50)
            self.field4.move(0, 420)
            self.label4 = QLabel(self)
            self.label4.setText("Соавтор:")
            self.label4.move(0, 400)
        else:
            self.setWindowTitle('Добавление')
            self.field = QPlainTextEdit(self)
            self.field.resize(410, 50)
            self.field.move(0, 20)
            self.label = QLabel(self)
            self.label.setText("Ф.И.О работника:")
            self.field1 = QPlainTextEdit(self)
            self.field1.resize(410, 50)
            self.field1.move(0, 120)
            self.label1 = QLabel(self)
            self.label1.setText("Должность:")
            self.label1.move(0, 100)
            self.field2 = QPlainTextEdit(self)
            self.field2.resize(410, 50)
            self.field2.move(0, 220)
            self.label2 = QLabel(self)
            self.label2.setText("Проекты:")
            self.label2.move(0, 200)
        self.btn = QPushButton(self)
        self.btn.setText('Добавить')
        self.btn.move(160, 420)
        self.btn.clicked.connect(self.check1)
    def check1(self):
        if a == "Проекты":
            textEdit = self.field.toPlainText()
            textEdit1 = self.field1.toPlainText()
            textEdit2 = self.field2.toPlainText()
            textEdit3 = self.field3.toPlainText()
            textEdit4 = self.field4.toPlainText()
            print(textEdit, textEdit1, textEdit2, textEdit3, textEdit4)
            con = sqlite3.connect('main.db')
            cur = con.cursor()
            cur.execute(f'INSERT INTO projects (theme, place, desc, author, author2) VALUES ("{textEdit}", "{textEdit1}", "{textEdit2}", "{textEdit3}", "{textEdit4}")')
            con.commit()
            self.par.refresh()
            self.close()
        else:
            textEdit = self.field.toPlainText()
            textEdit1 = self.field1.toPlainText()
            textEdit2 = self.field2.toPlainText()
            print(textEdit, textEdit1, textEdit2)
            con = sqlite3.connect('main.db')
            cur = con.cursor()
            cur.execute(f'INSERT INTO users (name, role, projs) VALUES ("{textEdit}", "{textEdit1}", "{textEdit2}")')
            con.commit()
            self.par.refresh()
            self.close()

# con = sqlite3.connect('main.db')
# cur = con.cursor()
# cur.execute(f' ALTER TABLE users MODIFY COLLUMN id SET AUTO_INCREMENT true')
# con.commit()

if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)