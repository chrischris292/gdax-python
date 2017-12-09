import datetime


class Collector:
    def __init__(self):
        dt = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        root = "/home/chris/gdax/"
        self.file = open(root + dt + "-gdax-market-data.json", "w+")

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
