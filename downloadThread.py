import logging
import threading
import time
import os


from pySmartDL import SmartDL

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class DownloadThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), url=None, dest=None, fileName=None):
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.args = args
        self.url = url
        self.dest = dest
        self.fileName = fileName
        self.download = SmartDL(self.url, progress_bar=False, threads=1)
        return

    def run(self):
        self.download.start(blocking=False)
        while not self.download.isFinished():
            logging.debug("Progress: " + str(self.download.get_progress()*100))
            time.sleep(0.2)
        if self.download.isSuccessful():
            logging.debug("Progress: " + str(self.download.get_progress()*100))
            logging.debug("downloaded file to '%s'" % self.download.get_dest())
            if (self.fileName is not None):
                self.path = self.dest +"/"+ self.fileName
            else:
                self.path = self.dest +"/"+ getFilenameFromUrl()
            self.renameFile(self.download.get_dest(), self.path)
                
        else:
            print("There were some errors:")
            for e in self.download.get_errors():
                print(str(e))
        return
    
    def renameFile(self, old, new):
        os.rename(old , new)

    def getFilenameFromUrl(self):
        filename = self.url[self.url.rfind("/") + 1:]
        return str(filename)