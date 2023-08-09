
import datetime
import json
import random

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

import requests

from datetime import timedelta
from enum import Enum



def getHistoricalData(contractAddress,fromUnix,toUnix):
    params = {
    'symbol': contractAddress+'-eth_USD',
    'resolution': 30,
    'from': fromUnix,
    'to': toUnix,
    }
    url = "https://api.dex.guru/v1/tradingview/history"
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

    response = (requests.get(url,params=params,headers=headers)).json()

    ret = {}

    datetimes=[]
    for unixTime in response["t"]:
        value = datetime.datetime.fromtimestamp(unixTime)
        datetimes.append(f"{value:%Y-%m-%d %H:%M:%S}")


    ret["date"] = datetimes
    ret["price"] = response["c"]


    return ret;
