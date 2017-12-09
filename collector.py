import gdax

if __name__ == '__main__':
    import sys
    import time
    import datetime as dt

    order_book = gdax.OrderBook()

    order_book.start()
    try:
        while True:
            now = datetime.datetime.now()
            shutoffTime = now.replace(
                hour=19, minute=10, second=0, microsecond=0)
            if now == shutoffTime:
                print "SHUT OFF"
                break
            time.sleep(5)
    except KeyboardInterrupt:
        order_book.close()

    if order_book.error:
        sys.exit(1)
    else:
        sys.exit(0)
