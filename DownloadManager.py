# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.item1 = QtWidgets.QHBoxLayout()
        self.item1.setObjectName("item1")
        self.label1 = QtWidgets.QLabel(self.activeDownload)
        self.label1.setObjectName("label1")
        self.item1.addWidget(self.label1)
        self.progressBar1 = QtWidgets.QProgressBar(self.activeDownload)
        self.progressBar1.setProperty("value", 24)
        self.progressBar1.setObjectName("progressBar1")
        self.item1.addWidget(self.progressBar1)
        self.activeDownloadListLayout.addLayout(self.item1)
        self.item2 = QtWidgets.QHBoxLayout()
        self.item2.setObjectName("item2")
        self.label2 = QtWidgets.QLabel(self.activeDownload)
        self.label2.setObjectName("label2")
        self.item2.addWidget(self.label2)
        self.progressBar2 = QtWidgets.QProgressBar(self.activeDownload)
        self.progressBar2.setProperty("value", 24)
        self.progressBar2.setObjectName("progressBar2")
        self.item2.addWidget(self.progressBar2)
        self.activeDownloadListLayout.addLayout(self.item2)
        self.gridLayout_5.addLayout(self.activeDownloadListLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.activeDownload, "")
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.history)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.historyLayout = QtWidgets.QVBoxLayout()
        self.historyLayout.setSpacing(6)
        self.historyLayout.setObjectName("historyLayout")
        self.itemH1 = QtWidgets.QHBoxLayout()
        self.itemH1.setObjectName("itemH1")
        self.labelH1 = QtWidgets.QLabel(self.history)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelH1.sizePolicy().hasHeightForWidth())
        self.labelH1.setSizePolicy(sizePolicy)
        self.labelH1.setObjectName("labelH1")
        self.itemH1.addWidget(self.labelH1)
        self.pushButton = QtWidgets.QPushButton(self.history)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.itemH1.addWidget(self.pushButton)
        self.historyLayout.addLayout(self.itemH1)
        self.gridLayout_2.addLayout(self.historyLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.history, "")
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseButton.setIcon(icon2)
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
        self.folderName.setPlaceholderText(_translate("MainWindow", "Inserisci il nome del download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addNewDownload), _translate("MainWindow", "Nuovo Download"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.activeDownload), _translate("MainWindow", "Download Attivi"))
        self.labelH1.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Apri Cartella"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history), _translate("MainWindow", "Cronologia"))
        self.titleLabel.setText(_translate("MainWindow", "Cartella per il download"))
        self.h2Label.setText(_translate("MainWindow", "Usa il tasto di navigazione per inserire la cartella di salvataggio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.options), _translate("MainWindow", "Opzioni"))
import photo_rc
