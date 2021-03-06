# -*- coding: utf-8 -*-

import os
import sys

#------------------------------------------------------------------------------

this_folder = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.dirname(os.path.dirname(this_folder))
sys.path.append(root_folder)
sys.path.append(this_folder)

#------------------------------------------------------------------------------

import asciichart
import ccxt # noqa: E402

#------------------------------------------------------------------------------

kraken = ccxt.kraken()
yunbi = ccxt.yunbi()

#------------------------------------------------------------------------------

symbol = 'BTC/USD'

#------------------------------------------------------------------------------

# each ohlcv candle is a list of [ timestamp, open, high, low, close, volume ]
index = 4 # use close price from each ohlcv candle

#------------------------------------------------------------------------------

def print_chart(exchange, symbol, timeframe, human_timeframe):

    print("\n" + exchange.name + ' ' + human_timeframe + ' chart:')

    # get a list of ohlcv candles
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

    # get the ohlCv (closing price, index == 4)
    series = [x[index] for x in ohlcv]

    # print the chart
    print("\n" + asciichart.plot(series[-120:], {'height': 20})) # print the chart

    last = ohlcv[len(ohlcv) - 1][index] # last closing price
    return last

#------------------------------------------------------------------------------

print_chart(kraken, 'BTC/USD', 60, '1m')

#------------------------------------------------------------------------------

last = print_chart(kraken, 'BTC/USD', 300, '5m')
print("\n" + kraken.name + " ₿ = $" + str(last) + "\n") # print last closing price

#------------------------------------------------------------------------------

last = print_chart(yunbi, 'BTC/CNY', 3600, '1h')
print("\n" + yunbi.name + " ₿ = CN¥ " + str(last) + "\n") # print last closing price

#------------------------------------------------------------------------------
