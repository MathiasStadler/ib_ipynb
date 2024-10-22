# FROM HERE
# https://robotwealth.com/trading-0dte-options-with-the-ibkr-native-api/

from threading import Thread, Event
import time
from typing import Any
from ibapi.common import BarData
from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.contract import Contract, ContractDetails
from ibapi.order import *
from ibapi.common import *
from ibapi.account_summary_tags import AccountSummaryTags
import pandas as pd
import requests
from bs4 import BeautifulSoup

# make url for 0DTE ATM option contracts from yahoo
# can only get approx 5 days' worth of expired contracts


def make_url(expiry, contract_type, strike):
    return f"https://finance.yahoo.com/quote/SPXW{expiry}{contract_type}0{strike*1000}"

# get 0dte options prices from yahoo
# use beautiful soup to parse the HTML and extract values from relevant tags


def get_0dte_prices(expiry, contract_type, strike):
    url = make_url(expiry, contract_type, strike)

    # headers to simulate browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }

    # get web page
    response = requests.get(url, headers=headers)

    # parse
    soup = BeautifulSoup(response.text, "html.parser")

    # extract last traded price (HTML specification is from inspection of Yahoo options data pages)
    last_traded_price_tag = soup.find(
        "fin-streamer", {"data-test": "qsp-price",
                         "data-field": "regularMarketPrice"}
    )
    last_traded_price = (
        float(last_traded_price_tag["value"]
              ) if last_traded_price_tag else "Not found"
    )

    # extract open price (HTML specification is from inspection of Yahoo options data pages)
    open_price_tag = soup.find("td", {"data-test": "OPEN-value"})
    open_price = float(open_price_tag.text) if open_price_tag else "Not found"

    return (open_price, last_traded_price)

