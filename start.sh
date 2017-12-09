export DATE=`date +%Y-%m-%d`
python gdax-python/collector.py > "logging/$DATE.log" 2>&1 &

