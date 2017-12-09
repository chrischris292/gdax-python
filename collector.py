import argparse
import datetime
import logging

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

    order_book = gdax.OrderBook(args.collectorRoot)

    order_book.start()
    try:
        while True:
            now = datetime.datetime.now()
            shutoffTime = now.replace(
                hour=10, minute=9, second=59)
            logging.info(now)
            if now == shutoffTime:
                logging.info("SHUT OFF")
                order_book.close()
                break
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("KEYBOARD INTERRUPT")
        order_book.close()

    if order_book.error:
        sys.exit(1)
    else:
        sys.exit(0)


try:
    main()
except:
    logging.exception("Oops:")
