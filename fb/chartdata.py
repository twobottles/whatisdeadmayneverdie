
import datetime
import json
import random

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

import requests

from datetime import timedelta
from enum import Enum

class range(Enum):
    minute15 = 1
    minute30= 2
    hour = 3
    hour2 = 4
    day=5
    day3=6
    day7=7
    day15=8
    day30=9


def getPeriod(forecastType):
    rangeId = int(forecastType)
    if (rangeId == 1) : return 15;
    if (rangeId == 2) : return 30;
    if (rangeId == 3) : return 1;
    if (rangeId == 4) : return 2;
    if (rangeId == 5) : return 1;
    if (rangeId == 6) : return 3;
    if (rangeId == 7) : return 7;
    if (rangeId == 8) : return 15;
    if (rangeId == 9) : return 30;

def getResolution(forecastType):
    rangeId = int(forecastType)
    if (rangeId == 1) : return 10;
    if (rangeId == 2) : return 10;
    if (rangeId == 3) : return 60;
    if (rangeId == 4) : return 60;
    if (rangeId == 5) : return 1440;
    if (rangeId == 6) : return 1440;
    if (rangeId == 7) : return 1440;
    if (rangeId == 8) : return 1440;
    if (rangeId == 9) : return 1440;

def getFrequency(forecastType):
    rangeId = int(forecastType)
    if (rangeId == 1) : return "T";
    if (rangeId == 2) : return "T";
    if (rangeId == 3) : return "H";
    if (rangeId == 4) : return "H";
    if (rangeId == 5) : return "D";
    if (rangeId == 6) : return "D";
    if (rangeId == 7) : return "D";
    if (rangeId == 8) : return "D";
    if (rangeId == 9) : return "D";



def getChainId(chainId):
    if (chainId == "ethereum"): return 1;
    if (chainId == "bsc"): return 2;
    if (chainId == "arbitrum"): return 3;
    return 0;

def getChainUrlValue(chainId):
    if (chainId == '1'): return 'eth_USD';
    if (chainId == '2'): return 'bsc_USD';
    if (chainId == '3'): return 'arbitrum_USD';
    return 'eth_USD';

def getTokenDetails(contractAddress):
  
    url = "https://api.dexscreener.com/latest/dex/tokens/"+contractAddress;
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

    response = (requests.get(url,headers=headers)).json()
    ret = {}
    ret["success"] = True
    if response["pairs"] is None:
        ret["success"] = False
        return ret;

    returnDetails = response["pairs"][0]
    ret["chainId"] = getChainId(returnDetails["chainId"])
    ret["name"] = returnDetails["baseToken"]["name"]
    ret["symbol"] = returnDetails["baseToken"]["symbol"]
    ret["pricem5"]= returnDetails["priceChange"]["m5"]
    ret["priceh1"]= returnDetails["priceChange"]["h1"]
    ret["priceh24"]= returnDetails["priceChange"]["h24"]

    ret["fdv"] = returnDetails["fdv"]



    urlGuru =  "https://api.dex.guru/v3/tokens/search/"+contractAddress;
    responseGuru = (requests.get(urlGuru,headers=headers)).json()   

    tokenItem = [
            dictionary for dictionary in responseGuru["data"]
            if dictionary['marketType'] == 'token'
        ]
    
    returnDetailsGuru = tokenItem[0]
    ret["volumeh24value"] = returnDetailsGuru["volume24hUSD"]
    ret["volumeh24"]= returnDetailsGuru["volumeUSDChange24h"]
    ret["timestamp"]= returnDetailsGuru["timestamp"]
    ret["liquidityUSD"]= returnDetailsGuru["liquidityUSD"]
    ret["liquidityUSDChange24h"]= returnDetailsGuru["liquidityUSDChange24h"]
    ret["logoURI"]=returnDetailsGuru["logoURI"]
    
    return ret

def getHistoricalData(contractAddress,fromUnix,toUnix,forecastType,timeFrameInMinutes,cid):
    params = {
    'symbol': contractAddress+'-'+getChainUrlValue(cid),
    'resolution': timeFrameInMinutes,
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


    ret["ds"] = datetimes
    ret["y"] = response["c"]


    return ret;


def prophet(contractAddress,fromUnix,toUnix,forecastType,timeFrameInMinutes,cid):
    chartData = getHistoricalData(contractAddress,fromUnix,toUnix,forecastType,timeFrameInMinutes,cid)
    df = pd.DataFrame.from_dict(chartData)

    model = Prophet(changepoint_prior_scale=0.5, interval_width=0, seasonality_mode='additive', daily_seasonality=True, yearly_seasonality=True)
    model.fit(df)
    frequency = str(timeFrameInMinutes) + "min"
    
    # Creating a dataframe for future predictions
    future = model.make_future_dataframe(periods=getPeriod(forecastType) ,freq=getFrequency(forecastType))
    future.tail()

    # Predicting future values
    forecast = model.predict(future)
    # Plotting the forecast
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    ret={}
    ret["hd"] = chartData["ds"];
    
    ret["hp"] = chartData["y"];
 
    ret["pp"] = forecast["yhat"].values.tolist();
    datetimes=[]
    for unixTime in forecast["ds"].values.tolist():
        value = datetime.datetime.fromtimestamp(unixTime // 1000000000)
   
        datetimes.append(f"{value:%Y-%m-%d %H:%M:%S}")

    ret["pd"] = datetimes;
 

    return ret;


def getTrends():

    url = "https://www.nostra-ai.tech/ethtest/"
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}


    return (requests.get(url,headers=headers)).json();



