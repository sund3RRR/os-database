# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 520)
        self.oc_combobox = QtWidgets.QComboBox(Dialog)
        self.oc_combobox.setGeometry(QtCore.QRect(640, 120, 91, 31))
        self.oc_combobox.setObjectName("oc_combobox")
        self.oc_combobox.addItem("")
        self.oc_combobox.addItem("")
        self.oc_combobox.addItem("")
        self.load_button = QtWidgets.QPushButton(Dialog)
        self.load_button.setGeometry(QtCore.QRect(640, 190, 93, 28))
        self.load_button.setObjectName("load_button")
        self.program_input = QtWidgets.QLineEdit(Dialog)
        self.program_input.setGeometry(QtCore.QRect(60, 310, 113, 22))
        self.program_input.setObjectName("program_input")
        self.oc_input = QtWidgets.QLineEdit(Dialog)
        self.oc_input.setGeometry(QtCore.QRect(240, 310, 113, 22))
        self.oc_input.setObjectName("oc_input")
        self.package_input = QtWidgets.QLineEdit(Dialog)
        self.package_input.setGeometry(QtCore.QRect(410, 310, 121, 22))
        self.package_input.setObjectName("package_input")
        self.program_label = QtWidgets.QLabel(Dialog)
        self.program_label.setGeometry(QtCore.QRect(70, 270, 91, 41))
        self.program_label.setStyleSheet("font: 75 12pt \"Tahoma\";")
        self.program_label.setObjectName("program_label")
        self.oc_label = QtWidgets.QLabel(Dialog)
        self.oc_label.setGeometry(QtCore.QRect(240, 280, 121, 31))
        self.oc_label.setObjectName("oc_label")
        self.package_label = QtWidgets.QLabel(Dialog)
        self.package_label.setGeometry(QtCore.QRect(440, 280, 61, 31))
        self.package_label.setObjectName("package_label")
        self.add_program_label = QtWidgets.QLabel(Dialog)
        self.add_program_label.setGeometry(QtCore.QRect(170, 250, 371, 41))
        self.add_program_label.setObjectName("add_program_label")
        self.add_button = QtWidgets.QPushButton(Dialog)
        self.add_button.setGeometry(QtCore.QRect(560, 310, 93, 28))
        self.add_button.setObjectName("add_button")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(50, 10, 541, 61))
        self.title.setObjectName("title")
        self.data_table = QtWidgets.QTableWidget(Dialog)
        self.data_table.setGeometry(QtCore.QRect(70, 60, 531, 192))
        self.data_table.setMinimumSize(QtCore.QSize(531, 0))
        self.data_table.setMaximumSize(QtCore.QSize(621, 16777215))
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(4)
        self.data_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(3, item)
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setGeometry(QtCore.QRect(30, 470, 611, 21))
        self.error_label.setObjectName("error_label")
        self.delete_button = QtWidgets.QPushButton(Dialog)
        self.delete_button.setGeometry(QtCore.QRect(380, 410, 93, 28))
        self.delete_button.setObjectName("delete_button")
        self.program_code_label = QtWidgets.QLabel(Dialog)
        self.program_code_label.setGeometry(QtCore.QRect(240, 380, 121, 41))
        self.program_code_label.setStyleSheet("font: 75 12pt \"Tahoma\";")
        self.program_code_label.setObjectName("program_code_label")
        self.program_code_input = QtWidgets.QLineEdit(Dialog)
        self.program_code_input.setGeometry(QtCore.QRect(240, 420, 113, 22))
        self.program_code_input.setObjectName("program_code_input")
        self.delete_program_label = QtWidgets.QLabel(Dialog)
        self.delete_program_label.setGeometry(QtCore.QRect(160, 360, 391, 21))
        self.delete_program_label.setObjectName("delete_program_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.oc_combobox.setItemText(0, _translate("Dialog", "Windows"))
        self.oc_combobox.setItemText(1, _translate("Dialog", "Linux"))
        self.oc_combobox.setItemText(2, _translate("Dialog", "Mac OS"))
        self.load_button.setText(_translate("Dialog", "Load"))
        self.program_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Программа</span></p></body></html>"))
        self.oc_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">ОС</span></p></body></html>"))
        self.package_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Пакет</span></p></body></html>"))
        self.add_program_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Добавление программы</span></p></body></html>"))
        self.add_button.setText(_translate("Dialog", "Add"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Select запрос программ для различных ОС</span></p></body></html>"))
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Program"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Package"))
        item = self.data_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "OS"))
        item = self.data_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ProgramCode"))
        self.error_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.delete_button.setText(_translate("Dialog", "Delete"))
        self.program_code_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Код программы</p></body></html>"))
        self.delete_program_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Удаление программы</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())