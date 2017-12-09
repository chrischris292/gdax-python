import datetime
import logging


class Collector:
    def __init__(self, dataFilepath):
        self.file = open(dataFilepath, "w+")

    def on_incremental_message(self, message):
        data = {"Type": "Incremental", "Message": message}
        self.file.write(str(data).strip("\n"))
        self.file.write("\n")

    def on_snapshot_gap(self, message):
        data = {"Type": "Snapshot", "Message": message}
        self.file.write(str(data).strip("\n"))
        self.file.write("\n")

    def on_close(self):
        logging.info('My application is ending!')
        self.file.close()
