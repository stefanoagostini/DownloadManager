import logging
import threading
import time

from pySmartDL import SmartDL

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class DownloadThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), url=None, dest=None):
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.args = args
        self.url = url
        self.dest = dest
        self.download = SmartDL(url, dest, progress_bar=False)
        return

    def run(self):
        self.download.start(blocking=False)
        while not self.download.isFinished():
            logging.debug("Progress: " + str(self.download.get_progress()*100))
            time.sleep(0.2)
        if self.download.isSuccessful():
            logging.debug("downloaded file to '%s'" % self.download.get_dest())
            logging.debug("download task took %ss" % self.download.get_dl_time(human=True))
        else:
            print("There were some errors:")
            for e in self.download.get_errors():
                print(str(e))
        self.path = self.download.get_dest()
        return


if (__name__ == '__main__'):
    url = ["https://github.com/stefanoagostini/chess_tests/archive/refs/heads/master.zip", "https://github.com/Pythondeveloper6/PyQt5-Download-Manager/archive/refs/heads/master.zip"]
    destPath = "D:\\Download\\prova\\"
    destFolder = ["chess_tests", "pyqt5"]
    for i in range(2):
        t = DownloadThread(args=(i,), url=url[i], dest=destPath+destFolder[i]+"\\")
        t.start()
