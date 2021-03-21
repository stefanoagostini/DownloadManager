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
        self.initUI()
        self.handleButtons()

        # Set up Observable for model
        self.url = Observable(self.ui.urlName.text())
        self.url.observe(M.setUrl)
        self.destFolder = Observable(self.ui.folderName.text())
        self.destFolder.observe(M.setDestFolder)
        self.destPath = Observable(self.ui.saveLocation.text())
        self.destPath.observe(M.setDestPath)
    
    def initUI(self):
        pass

    def handleButtons(self):
        self.ui.downloadButton.clicked.connect(self.download)
        self.ui.browseButton.clicked.connect(self.handleBrowse)

    def handleProgress(self):
        pass

    def handleBrowse(self):
        self.destPath.value = QFileDialog.getExistingDirectory(self, caption ="Apri Cartella", directory=".")
        self.ui.saveLocation.setText(str(self.destPath.value))

    #da spostare nel modello
    def saveBrowse(self):
        pass


    #da spostare nel modello
    def download(self):
        print('Start the download')
        self.url.value = self.ui.urlName.text()
        self.destFolder.value = self.ui.folderName.text()

        if self.url.value=='' or self.destPath.value=='':
            QMessageBox.warning(self, 'Errore', 'Inserisci una url o una cartella di destinazione valida')
        else:
            saveLocation = self.destPath.value + "\\" + self.destFolder.value + "\\"

            label = QLabel(self.destFolder.value)
            progressBar = QProgressBar();
            qhBoxLayout = QHBoxLayout()
            qhBoxLayout.addWidget(label)
            qhBoxLayout.addWidget(progressBar)
            self.ui.activeDownloadListLayout.addLayout(qhBoxLayout)

            t = DownloadThread(url=self.url.value, dest=saveLocation)
            t.start()

            self.ui.folderName.setText('')
            self.ui.urlName.setText('')



if (__name__=='__main__') :
    app = QApplication(sys.argv)
    window = DownloadManager()
    window.show()
    sys.exit(app.exec_())
