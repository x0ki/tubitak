# -*- coding -*-


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def printfun(self):
        self.outputtext.setText("Hi")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 240, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(printfun)
        self.inputtext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputtext.setGeometry(QtCore.QRect(0, 90, 171, 121))
        self.inputtext.setObjectName("inputtext")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 50, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 50, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.FR0M = QtWidgets.QLabel(self.centralwidget)
        self.FR0M.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.FR0M.setObjectName("FR0M")
        self.T0 = QtWidgets.QLabel(self.centralwidget)
        self.T0.setGeometry(QtCore.QRect(216, 30, 61, 20))
        self.T0.setObjectName("T0")
        self.outputtext = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputtext.setGeometry(QtCore.QRect(210, 90, 171, 121))
        self.outputtext.setObjectName("outputtext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        self.menu_x0ki = QtWidgets.QMenu(self.menubar)
        self.menu_x0ki.setObjectName("menu_x0ki")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_x0ki.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        self.comboBox.setItemText(0, _translate("MainWindow", "TÜRKÇE"))
        self.comboBox.setItemText(1, _translate("MainWindow", "İNGİLİZCE"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ARAPÇA"))
        self.comboBox.setItemText(3, _translate("MainWindow", "DİLİ ALGILA"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "TÜRKÇE"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "İNGİLİZCE"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "ARAPÇA"))
        self.FR0M.setText(_translate("MainWindow", "From"))
        self.T0.setText(_translate("MainWindow", " To"))
        self.menu_x0ki.setTitle(_translate("MainWindow", "@x0ki"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
