# import PyMongo and connect to a local, running Mongo instance
import threading

import gdax
from gdax.public_client import PublicClient
from pymongo import MongoClient

mongo_client = MongoClient('mongodb://chris:chris@ds129776.mlab.com:29776/gdax')

# specify the database and collection
db = mongo_client.gdax
BTC_collection = db.BTC_collection
snapshotCollection = db.BTC_snapshot
# instantiate a WebsocketClient instance, with a Mongo collection as a parameter
wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="BTC-USD",
                                mongo_collection=BTC_collection, should_print=False)
wsClient.start()


def saveSnapshot():
    threading.Timer(60.0, saveSnapshot).start()  # called every minute
    res = PublicClient().get_product_order_book(product_id="BTC-USD", level=3)
    print "INserting snapshot"
    snapshotCollection.insert_one(res)


saveSnapshot()
