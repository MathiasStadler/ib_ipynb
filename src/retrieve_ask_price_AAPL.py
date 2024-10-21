# FROM HERE
# https://github.com/PythonForForex/Interactive-brokers-python-api-guide/blob/master/retrieve_ask_price_AAPL.py

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading
import time


class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)

	def tickPrice(self, reqId, tickType, price, attrib):
		if tickType == 2 and reqId == 1:
			print('The current ask price is: ', price)

def run_loop():
	app.run()

app = IBapi()
#paper
# connect
app.connect("127.0.0.1", 7496, clientId=0)  # clientID identifies our application
# app.connect('127.0.0.1', 7497, 58)
# real
# app.connect('127.0.0.1', 7497, 58)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Create contract object
apple_contract = Contract()
apple_contract.symbol = 'AAPL'
apple_contract.secType = 'STK'
apple_contract.exchange = 'SMART'
apple_contract.currency = 'USD'

#Request Market Data
# app.reqMktData(1, apple_contract, '', False, False, [])
app.reqMarketDataType(3)
app.reqMktData(3, apple_contract, '', False, False, [])

time.sleep(10) #Sleep interval to allow time for incoming price data
app.disconnect()