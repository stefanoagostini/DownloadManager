import os

from pySmartDL import SmartDL

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


    # start the download
    def start(self):
        self.download.start(blocking=False)
        
    
    # pause the download
    def pause(self):
        if (self.download.get_status() == "downloading"):
            self.download.pause()
        elif (self.download.get_status() == "paused"):
            self.download.resume()
    

    # cancel the download
    def stop(self):
        self.download.resume()
        self.download.stop()
        self.downloadCancelled = True


    # return the progress status and a message that explain if the download is finished, cancelled or in pause
    def getInfo(self):
        self.progressStatus = self.download.get_progress()*100;
        self.status = self.download.get_status()
        if (not self.downloadCancelled):
            if self.download.isFinished():
                if self.download.isSuccessful():
                    if self.finished == False:
                        self.finished = True
                        if (self.fileName is not None):
                            self.path = self.destPath +"/"+ self.fileName
                        else:
                            self.path = self.destPath +"/"+ self.getFilenameFromUrl()
                        self.renameFile(self.download.get_dest(), self.path)
        else:
            self.status = "cancelled"
        return self.progressStatus, self.status

    
    # utility method to extract the name of the file from the url
    def getFilenameFromUrl(self):
        filename = self.url[self.url.rfind("/") + 1:]
        return str(filename)
    
    
    # save the file from the temp folder to destination path
    def renameFile(self, old, new):
        os.rename(old , new)
    

