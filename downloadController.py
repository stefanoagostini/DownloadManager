import time

from PyQt5.QtCore import QThread, pyqtSignal


class DownloadController(QThread):
    progress = pyqtSignal(object, object, object)


    def __init__(self, activedownloads=[]):
        QThread.__init__(self)
        self.activedownloads = activedownloads
        self.stop_thread = False
    

    # connect the pyqtsignal to a slot function
    def observe(self, slot):
        self.progress.connect(slot)


    # Run when thread is started
    def run(self):
        while True:
            if self.stop_thread:
                break
            if len(self.activedownloads) > 0:
                for i in range(0, len(self.activedownloads)):
                    value, status = self.activedownloads[i].getInfo()
                    self.progress.emit(i, value, status)
            time.sleep(0.5)


    # update 
    def updateDownloads(self, activedownloads):
        self.activedownloads = activedownloads
    

    # End the thread
    def stop(self):
        self.stop_thread = True
