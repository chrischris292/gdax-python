import gdax

if __name__ == '__main__':
    import sys
    import time
    import datetime as dt

    order_book = gdax.OrderBook()

    order_book.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        order_book.close()

    if order_book.error:
        sys.exit(1)
    else:
        sys.exit(0)
