from observable import Observable
from downloadThread import DownloadThread


class Model:
    def __init__(self):
        self.activedownloads = []
        self.history = []
        self.fileName = ""
        self.destPath = ""
        self.url = ""
        self.error = Observable("")

    
    def observeError(self, slot):
        self.error.observe(slot)

    def setUrl(self, value):
        self.url = value

    def setFileName(self, value):
        self.fileName = value


    def setDestPath(self, value):
        self.destPath = value
    
    def download(self, createUIElement):
        if self.url=='' or self.destPath=='':
            self.error.value = "Inserisci una url o una cartella di destinazione valida"
        else:
            createUIElement()
            t = DownloadThread(url=self.url, dest=self.destPath, fileName=self.fileName)
            t.start()

M = Model()