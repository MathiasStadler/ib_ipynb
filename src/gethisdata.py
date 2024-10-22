# FROM HERE
# https://stackoverflow.com/questions/74998349/unable-to-get-the-historical-data-from-api-interactive-brokers

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import datetime


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        # Get the current year and month
        now = datetime.datetime.now()
        year = now.year
        month = now.month

        contract = Contract()
        contract.symbol = "ES"
        contract.secType = "FUT"
        contract.exchange = "CME"
        contract.currency = "USD"
        contract.localSymbol = "ESZ7"  # Set the local symbol

        self.reqHistoricalData(orderId, contract, "", "1 D", "1 hour", "TRADES", 0, 1, True, [])

    def historicalData(self, reqId, bar):
        print(f"Historical data: {bar}")

    def historicalDataEnd(self, reqId, start, end):
        print("End of HistoricalData")
        print(f"Start: {start}, End: {end}")


app = TestApp()
# connect
app.connect("127.0.0.1", 7496, clientId=0)  # clientID identifies our application

# app.connect('127.0.0.1', 7497, 1)
app.run()