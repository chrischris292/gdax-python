import logging
import Queue
import random
import threading
import time

from gdax.public_client import PublicClient


class MongoStreamConsumer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        self._client = PublicClient()
        res = self._client.get_product_order_book(product_id="BTC-USD", level=3)

    def run(self):
        print('Mongo Consumer thread started')
        while not self.shutdown_flag.is_set():
            if not self.q.empty():
                object = self.q.get()
                print object
                if not self.orderBook.process_message(object):
                    break
        # ... Clean shutdown code here ...
        print('Mongo Consumer thread  stopped')
