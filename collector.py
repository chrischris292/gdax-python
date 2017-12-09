import datetime
import logging

import gdax

if __name__ == '__main__':
    import sys
    import time
    import datetime as dt
    handler = logging.FileHandler('hello.log')
    handler.setLevel(logging.INFO)

    order_book = gdax.OrderBook()

    order_book.start()
    try:
        while True:
            now = datetime.datetime.now()
            shutoffTime = now.replace(
                hour=19, minute=24, second=0, microsecond=0)
            print now
            if now > shutoffTime:
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
