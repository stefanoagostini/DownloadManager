import sys
from observable import Observable

from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QHBoxLayout,
                             QLabel, QMainWindow, QMessageBox, QProgressBar)

from DownloadManager import Ui_MainWindow
from downloadThread import DownloadThread
from model import M


class DownloadManager(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handleButtons()
        self.handleObserverAndObservable()

    # Set up Observable for model
    def handleObserverAndObservable(self):
        self.url = Observable(self.ui.urlName.text())
        self.url.observe(M.setUrl)

        self.fileName = Observable(self.ui.folderName.text())
        self.fileName.observe(M.setFileName)

        self.destPath = Observable(self.ui.saveLocation.text())
        self.destPath.observe(M.setDestPath)

        M.observeError(self.createMessageError)
    
    def createMessageError(self, value):
        QMessageBox.warning(self, 'Errore', value)
    
    def createActiveDownload(self,):
        label = QLabel(self.fileName.value)
        progressBar = QProgressBar();
        qhBoxLayout = QHBoxLayout()
        qhBoxLayout.addWidget(label)
        qhBoxLayout.addWidget(progressBar)
        self.ui.activeDownloadListLayout.addLayout(qhBoxLayout)
    
    def createHistoryDownload(self,):
        label = QLabel(self.fileName.value)
        progressBar = QProgressBar();
        qhBoxLayout = QHBoxLayout()
        qhBoxLayout.addWidget(label)
        qhBoxLayout.addWidget(progressBar)
        self.ui.historyLayout.addLayout(qhBoxLayout)
    
    # Set up all the buttons in the ui to connect with functions
    def handleButtons(self):
        self.ui.downloadButton.clicked.connect(self.download)
        self.ui.browseButton.clicked.connect(self.handleBrowse)

    def handleProgress(self):
        pass

    def handleBrowse(self):
        self.destPath.value = QFileDialog.getExistingDirectory(self, caption ="Apri Cartella", directory=".")
        self.ui.saveLocation.setText(str(self.destPath.value))


    #da spostare nel modello
    def download(self):
        self.url.value = self.ui.urlName.text()
        self.fileName.value = self.ui.folderName.text()

        M.download(self.createActiveDownload)

        self.ui.folderName.setText('')
        self.ui.urlName.setText('')



if (__name__=='__main__') :
    app = QApplication(sys.argv)
    window = DownloadManager()
    window.show()
    sys.exit(app.exec_())
