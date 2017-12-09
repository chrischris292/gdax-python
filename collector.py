import datetime
import logging

import gdax

if __name__ == '__main__':
    import sys
    import time
    import datetime as dt
    dt = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    handler = logging.FileHandler('home/chris/logging/' + dt + '.log')
    handler.setLevel(logging.DEBUG)

    order_book = gdax.OrderBook()

    order_book.start()
    try:
        while True:
            now = datetime.datetime.now()
            shutoffTime = now.replace(
                hour=19, minute=27, second=0, microsecond=0)
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
