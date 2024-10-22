# FROM HERE
# https://www.interactivebrokers.com/campus/ibkr-quant-news/handling-options-chains/

# INSIDE VENV

# pip                24.2
# requests           2.32.3
# setuptools         66.1.1
# urllib3            2.2.3

import requests
import urllib3
import csv
# Ignore insecure error messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

