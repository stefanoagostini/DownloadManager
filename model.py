from observable import Observable

class Model:
    def __init__(self):
        self.downloads = []
        self.destFolder = ""
        self.destPath = ""
        self.url = ""
    
    def startDownload(self, ):
        pass

    # def observe(self, slot):
    #     self.destPath.observe(slot)

    def setUrl(self, value):
        self.url = value
        print(self.url)

    def setDestFolder(self, value):
        self.destFolder = value
        print(self.destFolder)


    def setDestPath(self, value):
        self.destPath = value
        print(self.destPath)
    
M = Model()