# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadManager.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        MainWindow.setMinimumSize(QtCore.QSize(800, 596))
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.addNewDownload = QtWidgets.QWidget()
        self.addNewDownload.setObjectName("addNewDownload")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.addNewDownload)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.newDownloadLayout = QtWidgets.QGridLayout()
        self.newDownloadLayout.setObjectName("newDownloadLayout")
        self.urlName = QtWidgets.QLineEdit(self.addNewDownload)
        self.urlName.setObjectName("urlName")
        self.newDownloadLayout.addWidget(self.urlName, 1, 0, 1, 3)
        self.downloadButton = QtWidgets.QPushButton(self.addNewDownload)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon)
        self.downloadButton.setIconSize(QtCore.QSize(25, 25))
        self.downloadButton.setObjectName("downloadButton")
        self.newDownloadLayout.addWidget(self.downloadButton, 2, 1, 1, 1)
        self.folderName = QtWidgets.QLineEdit(self.addNewDownload)
        self.folderName.setObjectName("folderName")
        self.newDownloadLayout.addWidget(self.folderName, 0, 0, 1, 3)
        self.gridLayout_4.addLayout(self.newDownloadLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.addNewDownload, "")
        self.activeDownload = QtWidgets.QWidget()
        self.activeDownload.setObjectName("activeDownload")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.activeDownload)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.activeDownloadListLayout = QtWidgets.QVBoxLayout()
        self.activeDownloadListLayout.setObjectName("activeDownloadListLayout")
        self.gridLayout_5.addLayout(self.activeDownloadListLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.activeDownload, "")
        self.legenda = QtWidgets.QWidget()
        self.legenda.setObjectName("legenda")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.legenda)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.legendaLayout = QtWidgets.QVBoxLayout()
        self.legendaLayout.setSpacing(6)
        self.legendaLayout.setObjectName("legendaLayout")
        self.label = QtWidgets.QLabel(self.legenda)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.legendaLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.legenda)
        self.label_2.setStyleSheet("QLabel { color : black; font-size: 22px; }")
        self.label_2.setObjectName("label_2")
        self.legendaLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.legenda)
        self.label_5.setStyleSheet("QLabel { color : green; font-size: 22px; }")
        self.label_5.setObjectName("label_5")
        self.legendaLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.legenda)
        self.label_3.setStyleSheet("QLabel { color : orange; font-size: 22px; }")
        self.label_3.setObjectName("label_3")
        self.legendaLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.legenda)
        self.label_4.setStyleSheet("QLabel { color : red; font-size: 22px; }")
        self.label_4.setObjectName("label_4")
        self.legendaLayout.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.legendaLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.legenda, "")
        self.options = QtWidgets.QWidget()
        self.options.setObjectName("options")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.options)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.OptionLayout = QtWidgets.QGridLayout()
        self.OptionLayout.setObjectName("OptionLayout")
        self.saveLocation = QtWidgets.QLineEdit(self.options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveLocation.sizePolicy().hasHeightForWidth())
        self.saveLocation.setSizePolicy(sizePolicy)
        self.saveLocation.setPlaceholderText("")
        self.saveLocation.setObjectName("saveLocation")
        self.OptionLayout.addWidget(self.saveLocation, 3, 0, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.OptionLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.h2Label = QtWidgets.QLabel(self.options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h2Label.sizePolicy().hasHeightForWidth())
        self.h2Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.h2Label.setFont(font)
        self.h2Label.setObjectName("h2Label")
        self.OptionLayout.addWidget(self.h2Label, 1, 0, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)
        self.browseButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseButton.setIcon(icon1)
        self.browseButton.setIconSize(QtCore.QSize(25, 25))
        self.browseButton.setObjectName("browseButton")
        self.OptionLayout.addWidget(self.browseButton, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.OptionLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.options, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Download Manager"))
        self.urlName.setPlaceholderText(_translate("MainWindow", "Inserisci la URL per il download"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.folderName.setPlaceholderText(_translate("MainWindow", "Inserisci il nome del download (non dimenticare il formato del file)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addNewDownload), _translate("MainWindow", "Nuovo Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.activeDownload), _translate("MainWindow", "Download Attivi"))
        self.label.setText(_translate("MainWindow", "Ecco il significato dei colori nella tab Download Attivi:"))
        self.label_2.setText(_translate("MainWindow", "Nero: in downlaod"))
        self.label_5.setText(_translate("MainWindow", "Verde: downlaod completato con successo"))
        self.label_3.setText(_translate("MainWindow", "Arancione: in pausa"))
        self.label_4.setText(_translate("MainWindow", "Rosso: errore durante il download o cancellato"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.legenda), _translate("MainWindow", "Legenda"))
        self.titleLabel.setText(_translate("MainWindow", "Cartella per il download"))
        self.h2Label.setText(_translate("MainWindow", "Usa il tasto di navigazione per inserire la cartella di salvataggio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.options), _translate("MainWindow", "Opzioni"))

import photo_rc
