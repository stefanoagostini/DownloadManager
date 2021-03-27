import logging
import os

from pySmartDL import SmartDL

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class Download:
    def __init__(self, url, fileName, destPath):  
        self.url = url
        self.destPath = destPath
        self.fileName = fileName
        self.finished = False
        self.downloadCancelled = False
        self.download = SmartDL(self.url, progress_bar=False, threads=1)
        self.status = None
        self.progressStatus = 0

    
    def start(self):
        self.download.start(blocking=False)
        
    
    def pause(self):
        if (self.download.get_status() == "downloading"):
            self.download.pause()
        elif (self.download.get_status() == "paused"):
            self.download.resume()
    

    def stop(self):
        self.download.resume()
        self.download.stop()
        self.downloadCancelled = True


    def getInfo(self):
        self.progressStatus = self.download.get_progress()*100;
        logging.debug("Progress: " + str(self.progressStatus))
        self.status = self.download.get_status()
        if (not self.downloadCancelled):
            if self.download.isFinished():
                if self.download.isSuccessful():
                    if self.finished == False:
                        self.finished = True
                        logging.debug("downloaded file to '%s'" % self.download.get_dest())
                        if (self.fileName is not None):
                            self.path = self.destPath +"/"+ self.fileName
                        else:
                            self.path = self.destPath +"/"+ self.getFilenameFromUrl()
                        self.renameFile(self.download.get_dest(), self.path)
        else:
            self.status = "cancelled"
        return self.progressStatus, self.status

    
    def getFilenameFromUrl(self):
        filename = self.url[self.url.rfind("/") + 1:]
        return str(filename)
    
    
    def renameFile(self, old, new):
        os.rename(old , new)
    

