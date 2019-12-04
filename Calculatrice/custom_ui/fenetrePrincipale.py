# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_form_calculatrice(object):
    def setupUi(self, form_calculatrice):
        form_calculatrice.setObjectName("form_calculatrice")
        form_calculatrice.resize(256, 360)
        self.gridLayout = QtWidgets.QGridLayout(form_calculatrice)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_c = QtWidgets.QPushButton(form_calculatrice)
        self.btn_c.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_c.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_c.setFont(font)
        self.btn_c.setFlat(True)
        self.btn_c.setObjectName("btn_c")
        self.gridLayout.addWidget(self.btn_c, 2, 0, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_7.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_7.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_7.setFont(font)
        self.btn_7.setFlat(True)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_8.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_8.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_8.setFont(font)
        self.btn_8.setFlat(True)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_9.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_9.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_9.setFont(font)
        self.btn_9.setFlat(True)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(form_calculatrice)
        self.btn_mult.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_mult.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_mult.setFont(font)
        self.btn_mult.setFlat(True)
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 3, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_4.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_4.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_4.setFont(font)
        self.btn_4.setFlat(True)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 4, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_5.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_5.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_5.setFont(font)
        self.btn_5.setFlat(True)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 4, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_6.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_6.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_6.setFont(font)
        self.btn_6.setFlat(True)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 4, 2, 1, 1)
        self.btn_moins = QtWidgets.QPushButton(form_calculatrice)
        self.btn_moins.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_moins.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_moins.setFont(font)
        self.btn_moins.setFlat(True)
        self.btn_moins.setObjectName("btn_moins")
        self.gridLayout.addWidget(self.btn_moins, 4, 3, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_1.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_1.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_1.setFont(font)
        self.btn_1.setFlat(True)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_2.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_2.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_2.setFont(font)
        self.btn_2.setFlat(True)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 5, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_3.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_3.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_3.setFont(font)
        self.btn_3.setFlat(True)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 5, 2, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(form_calculatrice)
        self.btn_plus.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_plus.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_plus.setFont(font)
        self.btn_plus.setFlat(True)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 5, 3, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(form_calculatrice)
        self.btn_0.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_0.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_0.setFont(font)
        self.btn_0.setFlat(True)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 1)
        self.btn_point = QtWidgets.QPushButton(form_calculatrice)
        self.btn_point.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_point.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_point.setFont(font)
        self.btn_point.setFlat(True)
        self.btn_point.setObjectName("btn_point")
        self.gridLayout.addWidget(self.btn_point, 6, 2, 1, 1)
        self.btn_egal = QtWidgets.QPushButton(form_calculatrice)
        self.btn_egal.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_egal.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_egal.setFont(font)
        self.btn_egal.setFlat(True)
        self.btn_egal.setObjectName("btn_egal")
        self.gridLayout.addWidget(self.btn_egal, 6, 3, 1, 1)
        self.le_resultat = QtWidgets.QLineEdit(form_calculatrice)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.le_resultat.setFont(font)
        self.le_resultat.setFrame(False)
        self.le_resultat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_resultat.setObjectName("le_resultat")
        self.gridLayout.addWidget(self.le_resultat, 1, 0, 1, 4)
        self.le_operation = QtWidgets.QLineEdit(form_calculatrice)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.le_operation.setFont(font)
        self.le_operation.setFrame(False)
        self.le_operation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_operation.setObjectName("le_operation")
        self.gridLayout.addWidget(self.le_operation, 0, 0, 1, 4)
        self.btn_div = QtWidgets.QPushButton(form_calculatrice)
        self.btn_div.setMinimumSize(QtCore.QSize(64, 64))
        self.btn_div.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.btn_div.setFont(font)
        self.btn_div.setFlat(True)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 2, 3, 1, 1)

        self.retranslateUi(form_calculatrice)
        QtCore.QMetaObject.connectSlotsByName(form_calculatrice)

    def retranslateUi(self, form_calculatrice):
        form_calculatrice.setWindowTitle(QtWidgets.QApplication.translate("form_calculatrice", "Calculatrice", None, -1))
        self.btn_c.setText(QtWidgets.QApplication.translate("form_calculatrice", "C", None, -1))
        self.btn_7.setText(QtWidgets.QApplication.translate("form_calculatrice", "7", None, -1))
        self.btn_8.setText(QtWidgets.QApplication.translate("form_calculatrice", "8", None, -1))
        self.btn_9.setText(QtWidgets.QApplication.translate("form_calculatrice", "9", None, -1))
        self.btn_mult.setText(QtWidgets.QApplication.translate("form_calculatrice", "*", None, -1))
        self.btn_4.setText(QtWidgets.QApplication.translate("form_calculatrice", "4", None, -1))
        self.btn_5.setText(QtWidgets.QApplication.translate("form_calculatrice", "5", None, -1))
        self.btn_6.setText(QtWidgets.QApplication.translate("form_calculatrice", "6", None, -1))
        self.btn_moins.setText(QtWidgets.QApplication.translate("form_calculatrice", "-", None, -1))
        self.btn_1.setText(QtWidgets.QApplication.translate("form_calculatrice", "1", None, -1))
        self.btn_2.setText(QtWidgets.QApplication.translate("form_calculatrice", "2", None, -1))
        self.btn_3.setText(QtWidgets.QApplication.translate("form_calculatrice", "3", None, -1))
        self.btn_plus.setText(QtWidgets.QApplication.translate("form_calculatrice", "+", None, -1))
        self.btn_0.setText(QtWidgets.QApplication.translate("form_calculatrice", "0", None, -1))
        self.btn_point.setText(QtWidgets.QApplication.translate("form_calculatrice", ".", None, -1))
        self.btn_egal.setText(QtWidgets.QApplication.translate("form_calculatrice", "=", None, -1))
        self.le_resultat.setText(QtWidgets.QApplication.translate("form_calculatrice", "0", None, -1))
        self.btn_div.setText(QtWidgets.QApplication.translate("form_calculatrice", "/", None, -1))

