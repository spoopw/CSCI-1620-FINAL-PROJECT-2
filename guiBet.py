# Form implementation generated from reading ui file 'guiReal2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 670)
        MainWindow.setMinimumSize(QtCore.QSize(500, 670))
        MainWindow.setMaximumSize(QtCore.QSize(500, 670))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setObjectName("button_exit")
        self.label_your_balance = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_your_balance.setGeometry(QtCore.QRect(140, 10, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_your_balance.setFont(font)
        self.label_your_balance.setObjectName("label_your_balance")
        self.label_balance = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_balance.setGeometry(QtCore.QRect(130, 70, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_balance.setFont(font)
        self.label_balance.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_balance.setObjectName("label_balance")
        self.label_enter_amount = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_enter_amount.setGeometry(QtCore.QRect(40, 160, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_enter_amount.setFont(font)
        self.label_enter_amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_enter_amount.setObjectName("label_enter_amount")
        self.input_bet = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_bet.setGeometry(QtCore.QRect(170, 220, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.input_bet.setFont(font)
        self.input_bet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_bet.setObjectName("input_bet")
        self.radio_1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_1.setGeometry(QtCore.QRect(130, 410, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.radio_1.setFont(font)
        self.radio_1.setObjectName("radio_1")
        self.radio_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_2.setGeometry(QtCore.QRect(230, 410, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.radio_2.setFont(font)
        self.radio_2.setObjectName("radio_2")
        self.radio_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_3.setGeometry(QtCore.QRect(320, 410, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.radio_3.setFont(font)
        self.radio_3.setObjectName("radio_3")
        self.radio_4 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_4.setGeometry(QtCore.QRect(130, 470, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.radio_4.setFont(font)
        self.radio_4.setObjectName("radio_4")
        self.radio_5 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_5.setGeometry(QtCore.QRect(230, 470, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.radio_5.setFont(font)
        self.radio_5.setObjectName("radio_5")
        self.radio_6 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_6.setGeometry(QtCore.QRect(320, 470, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.radio_6.setFont(font)
        self.radio_6.setObjectName("radio_6")
        self.label_choose_number = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_choose_number.setGeometry(QtCore.QRect(20, 360, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_choose_number.setFont(font)
        self.label_choose_number.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_choose_number.setObjectName("label_choose_number")
        self.label_amount_rolled = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_amount_rolled.setGeometry(QtCore.QRect(50, 550, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_amount_rolled.setFont(font)
        self.label_amount_rolled.setText("")
        self.label_amount_rolled.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_amount_rolled.setObjectName("label_amount_rolled")
        self.label_winnings = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_winnings.setGeometry(QtCore.QRect(60, 600, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_winnings.setFont(font)
        self.label_winnings.setText("")
        self.label_winnings.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_winnings.setObjectName("label_winnings")
        self.button_cheat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_cheat.setGeometry(QtCore.QRect(400, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_cheat.setFont(font)
        self.button_cheat.setObjectName("button_cheat")
        self.button_bet = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_bet.setGeometry(QtCore.QRect(170, 270, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_bet.setFont(font)
        self.button_bet.setObjectName("button_bet")
        self.label_agenda = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_agenda.setGeometry(QtCore.QRect(40, 320, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_agenda.setFont(font)
        self.label_agenda.setText("")
        self.label_agenda.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_agenda.setObjectName("label_agenda")
        self.button_howtoplay = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_howtoplay.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_howtoplay.setFont(font)
        self.button_howtoplay.setObjectName("button_howtoplay")
        self.label_howtoplay = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_howtoplay.setGeometry(QtCore.QRect(40, 510, 421, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_howtoplay.setFont(font)
        self.label_howtoplay.setText("")
        self.label_howtoplay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_howtoplay.setObjectName("label_howtoplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))
        self.label_your_balance.setText(_translate("MainWindow", "Your balance:"))
        self.label_balance.setText(_translate("MainWindow", "$500"))
        self.label_enter_amount.setText(_translate("MainWindow", "Enter the amount you\'d like to bet:"))
        self.input_bet.setPlaceholderText(_translate("MainWindow", "Bet amount"))
        self.radio_1.setText(_translate("MainWindow", "1"))
        self.radio_2.setText(_translate("MainWindow", "2"))
        self.radio_3.setText(_translate("MainWindow", "3"))
        self.radio_4.setText(_translate("MainWindow", "4"))
        self.radio_5.setText(_translate("MainWindow", "5"))
        self.radio_6.setText(_translate("MainWindow", "6"))
        self.label_choose_number.setText(_translate("MainWindow", "Choose the number you\'d like to guess:"))
        self.button_cheat.setText(_translate("MainWindow", "Cheat"))
        self.button_bet.setText(_translate("MainWindow", "Bet"))
        self.button_howtoplay.setText(_translate("MainWindow", "How to play"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())