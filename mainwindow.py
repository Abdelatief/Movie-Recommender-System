# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindow_dialog(object):
    def setupUi(self, mainwindow_dialog):
        mainwindow_dialog.setObjectName("mainwindow_dialog")
        mainwindow_dialog.resize(700, 600)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(mainwindow_dialog)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(mainwindow_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.movie_name_lineEdit = QtWidgets.QLineEdit(mainwindow_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.movie_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.movie_name_lineEdit.setSizePolicy(sizePolicy)
        self.movie_name_lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.movie_name_lineEdit.setFont(font)
        self.movie_name_lineEdit.setObjectName("movie_name_lineEdit")
        self.verticalLayout.addWidget(self.movie_name_lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.barchar_show_button = QtWidgets.QPushButton(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.barchar_show_button.setFont(font)
        self.barchar_show_button.setObjectName("barchar_show_button")
        self.horizontalLayout.addWidget(self.barchar_show_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.piechart_show_button = QtWidgets.QPushButton(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.piechart_show_button.setFont(font)
        self.piechart_show_button.setObjectName("piechart_show_button")
        self.horizontalLayout_2.addWidget(self.piechart_show_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.dotplot_show_button = QtWidgets.QPushButton(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.dotplot_show_button.setFont(font)
        self.dotplot_show_button.setObjectName("dotplot_show_button")
        self.horizontalLayout_3.addWidget(self.dotplot_show_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.hist_show_button = QtWidgets.QPushButton(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.hist_show_button.setFont(font)
        self.hist_show_button.setObjectName("hist_show_button")
        self.horizontalLayout_4.addWidget(self.hist_show_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.boxplot_show_button = QtWidgets.QPushButton(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.boxplot_show_button.setFont(font)
        self.boxplot_show_button.setObjectName("boxplot_show_button")
        self.horizontalLayout_5.addWidget(self.boxplot_show_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.mean_show_button = QtWidgets.QPushButton(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.mean_show_button.setFont(font)
        self.mean_show_button.setObjectName("mean_show_button")
        self.horizontalLayout_6.addWidget(self.mean_show_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.correlation_show_button = QtWidgets.QPushButton(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.correlation_show_button.setFont(font)
        self.correlation_show_button.setObjectName("correlation_show_button")
        self.horizontalLayout_7.addWidget(self.correlation_show_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.similar_movies_listWidget = QtWidgets.QListWidget(mainwindow_dialog)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.similar_movies_listWidget.setFont(font)
        self.similar_movies_listWidget.setObjectName("similar_movies_listWidget")
        self.horizontalLayout_8.addWidget(self.similar_movies_listWidget)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.retranslateUi(mainwindow_dialog)
        QtCore.QMetaObject.connectSlotsByName(mainwindow_dialog)

    def retranslateUi(self, mainwindow_dialog):
        _translate = QtCore.QCoreApplication.translate
        mainwindow_dialog.setWindowTitle(_translate("mainwindow_dialog", "Movie Recommender System"))
        self.label.setText(_translate("mainwindow_dialog", "Movie Name"))
        self.label_2.setText(_translate("mainwindow_dialog", "Bar Chart"))
        self.barchar_show_button.setText(_translate("mainwindow_dialog", "Show"))
        self.label_3.setText(_translate("mainwindow_dialog", "Pie Chart"))
        self.piechart_show_button.setText(_translate("mainwindow_dialog", "Show"))
        self.label_4.setText(_translate("mainwindow_dialog", "Dot Plot"))
        self.dotplot_show_button.setText(_translate("mainwindow_dialog", "Show"))
        self.label_5.setText(_translate("mainwindow_dialog", "Histogram"))
        self.hist_show_button.setText(_translate("mainwindow_dialog", "Show"))
        self.label_6.setText(_translate("mainwindow_dialog", "Box Plot"))
        self.boxplot_show_button.setText(_translate("mainwindow_dialog", "Show"))
        self.label_7.setText(_translate("mainwindow_dialog", "Mean"))
        self.mean_show_button.setText(_translate("mainwindow_dialog", "Show"))
        self.label_8.setText(_translate("mainwindow_dialog", "Correlation"))
        self.correlation_show_button.setText(_translate("mainwindow_dialog", "Show"))
