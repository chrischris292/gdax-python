import argparse
import datetime
import gzip
import logging
import os
import shutil

import gdax


def main():
    import sys
    import time
    import datetime as dt
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument('loggingRoot', type=str,
                        help='')
    parser.add_argument('collectorRoot', type=str,
                        help='')
    args = parser.parse_args()
    dt = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    logFilePath = args.loggingRoot + dt + '.log'

    logging.basicConfig(level=logging.DEBUG,
                        filename=logFilePath,
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',)
    dataFilepath = args.collectorRoot + dt + "-gdax-market.data"

    order_book = gdax.OrderBook(dataFilepath)

    order_book.start()
    try:
        while True:
            now = datetime.datetime.now()
            shutoffTimeLow = now.replace(
                hour=15, minute=49, second=50)
            shutoffTimeHigh = now.replace(
                hour=15, minute=50, second=00)
            if now > shutoffTimeLow and now < shutoffTimeHigh:
                logging.info("SHUT OFF")
                order_book.close()
                break
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("KEYBOARD INTERRUPT")
        order_book.close()

    with open(dataFilepath, 'rb') as f_in:
        with open(dataFilepath + '.gz', 'wb') as f_out:
            with gzip.GzipFile(dataFilepath, 'wb', fileobj=f_out) as f_out:
                shutil.copyfileobj(f_in, f_out)
    logging.info("Created compressed file" + dataFilepath + '.gz')
    logging.info("Removing original file" + dataFilepath)
    os.remove(dataFilepath)
    if order_book.error:
        sys.exit(1)
    else:
        sys.exit(0)


try:
    main()
except:
    logging.exception("Oops:")
