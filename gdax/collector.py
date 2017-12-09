import datetime


class Collector:
    def __init__(self, projectRoot):
        dt = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.file = open(projectRoot + dt + "-gdax-market-data.data", "w+")

    def on_incremental_message(self, message):
        data = {"Type": "Incremental", "Message": message}
        self.file.write(str(data).strip("\n"))
        self.file.write("\n")

    def on_snapshot_gap(self, message):
        data = {"Type": "Snapshot", "Message": message}
        self.file.write(str(data).strip("\n"))
        self.file.write("\n")

    def on_close(self):
        print 'My application is ending!'
        self.file.close()
