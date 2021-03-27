import sys

import requests
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QHBoxLayout,
                             QLabel, QMainWindow, QMessageBox, QProgressBar,
                             QPushButton)

from downloadController import DownloadController
from DownloadManager import Ui_MainWindow
from model import Download


class DownloadManager(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons with functions
        self.handleButtons()

        # Init class variables
        self.activedownloads = []
        self.activeDownloadListLayoutArray = []
        self.url = ""
        self.fileName = ""
        self.destPath = ""
        self.downloadController = DownloadController(self.activedownloads)
        self.downloadController.observe(self.updateProgress)
        self.downloadController.start()

    
    # Set up all the buttons in the ui to connect with functions
    def handleButtons(self):
        self.ui.downloadButton.clicked.connect(self.download)
        self.ui.browseButton.clicked.connect(self.handleBrowse)

    # Create the view element for a download
    def createActiveDownload(self, download):
        label = QLabel(self.fileName)
        progressBar = QProgressBar()
        pauseButton = QPushButton('Pausa/Riprendi')
        cancelButton = QPushButton('Annulla')
        pauseButton.clicked.connect(download.pause)
        cancelButton.clicked.connect(download.stop)
        qhBoxLayout = QHBoxLayout()
        qhBoxLayout.addWidget(label)
        qhBoxLayout.addWidget(progressBar)
        qhBoxLayout.addWidget(pauseButton)
        qhBoxLayout.addWidget(cancelButton)
        self.ui.activeDownloadListLayout.addLayout(qhBoxLayout)
        self.activeDownloadListLayoutArray.append([label, progressBar])


    # Handle the browse interface to add a download folder
    def handleBrowse(self):
        self.destPath = QFileDialog.getExistingDirectory(self, caption ="Apri Cartella", directory=".")
        self.ui.saveLocation.setText(str(self.destPath))


    # Strart the download
    def download(self):
        self.url = self.ui.urlName.text()
        self.fileName = self.ui.folderName.text()
        
        # Check if the file already exist
        filexist = True
        path = self.destPath +"/"+ self.fileName
        try:        
            f = open(path)
        except IOError:
            filexist = False
        
        if (self.url=='' or self.destPath==''): # if any field is empty
            QMessageBox.warning(self, 'Errore', "Inserisci una url o una cartella di destinazione valida")
        elif (filexist): # if the file already exist
            QMessageBox.warning(self, 'Errore', "Esiste già un file con quel nome nella cartella di download. Cambiare cartella di destiazione o nome al file")
        elif (not self.site_exist(self.url)):
            QMessageBox.warning(self, 'Errore', "L'url dalla quale si prova a scaricare non è valida")
        else:
            download = Download(self.url, self.fileName, self.destPath)
            self.createActiveDownload(download)
            download.start()
            self.activedownloads.append(download)
            self.downloadController.updateDownloads(self.activedownloads)
            self.ui.folderName.setText('')
            self.ui.urlName.setText('')
    

    # Update the view with real time progress status and change the label color for a feedback of download status
    def updateProgress(self, i, value, status):
        if status == "downloading":
            self.activeDownloadListLayoutArray[i][0].setStyleSheet("QLabel { color : black; font-size: 22px; }");
            self.activeDownloadListLayoutArray[i][1].setValue(value)
        elif status == "cancelled":
            self.activeDownloadListLayoutArray[i][0].setStyleSheet("QLabel { color : red; font-size: 22px; }");
        elif status == "finished":
            self.activeDownloadListLayoutArray[i][0].setStyleSheet("QLabel { color : green; font-size: 22px; }");
            self.activeDownloadListLayoutArray[i][1].setValue(value)
        elif status == "paused":
            self.activeDownloadListLayoutArray[i][0].setStyleSheet("QLabel { color : orange; font-size: 22px; }");
        else:
            self.activeDownloadListLayoutArray[i][0].setStyleSheet("QLabel { color : red; font-size: 22px; }");
            self.activeDownloadListLayoutArray[i][1].setValue(value)

    
    # When the app is closed, kill the downloadController thread
    def closeEvent(self, event):
        self.downloadController.stop()
        event.accept()

    
    # Check if the url exist before downloading
    def site_exist(self, url):
        try:
            request = requests.head(url)
            return request.status_code == 200
        except:
            return False;

    



if (__name__=='__main__') :
    app = QApplication(sys.argv)
    window = DownloadManager()
    window.show()
    sys.exit(app.exec_())
