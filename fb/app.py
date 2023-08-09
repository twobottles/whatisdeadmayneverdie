from urllib.parse import urlencode
import flask

from datetime import timedelta

import telebot


import time

import json
from web3 import Web3
from time import strftime, localtime
from datetime import datetime
import time

app = flask.Flask(__name__)


API_KEY = "6410870870:AAFmQseFtxAo-wFkNCMW4O6wU9j3OtBmpMc"
bot = telebot.TeleBot(API_KEY)


infura_url = 'https://goerli.infura.io/v3/9c6be22ff67941c0b009f9e909cfc052'
web3 = Web3(Web3.HTTPProvider(infura_url))
abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]')
ca = "0xEBB0e1BD71B07cA9c9DbAD19Bb70df47FDc22059"
abi = json.loads('[{"inputs":[{"internalType":"address","name":"owner_","type":"address"},{"internalType":"address","name":"router_","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"devAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"epochScheduleReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"bool","name":"toggle","type":"bool"}],"name":"excemptReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getLastBuyTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLastBuyer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMaxBuy","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMegaJackpotExecutionTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMegaRewardIdle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"walletAdd","type":"address"}],"name":"getPoints","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getScheduledReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalPointsExt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"hoursToMegaJackpot","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"launchedAt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"manualBurn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualDistributionReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualProcessRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"marketingWallet","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minimumHoldToGetPoints","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numTokensSellToAddToLiquidity","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"openTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"optimizeMegaJackpotReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"removeBuyLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"},{"internalType":"bool","name":"toggle","type":"bool"}],"name":"setBot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newIdleHours","type":"uint256"}],"name":"setHoursToMegaJackpot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"percentage","type":"uint256"}],"name":"setMarketingPercentage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"minimumHoldToGetPoints_","type":"uint256"}],"name":"setMinimumPoints","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"additionalHour","type":"uint256"}],"name":"setScheduledReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"setSwapThresholdAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"isSell","type":"bool"},{"internalType":"uint256","name":"percentage","type":"uint256"}],"name":"setTax","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newDefaultHour","type":"uint256"}],"name":"setepochScheduleRewardAdditionalHours","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
contract = web3.eth.contract(address=ca, abi=abi)

website = 'https://reward-2da17.web.app/';
uniswapWebsite = 'https://reward-2da17.web.app/';

def getBalance(address):
  return  contract.functions.balanceOf(address).call();


@bot.message_handler(commands=['commands'])
def commands(message):
  try:
  
    reply = f'/ca - To get Contract Address';
    reply += '\n \n'
    reply += f'/website - To get Ofiical Website Url';
    reply += '\n \n'
    reply += f'/points [address] - To get wallet address details';
    reply += '\n \n'
    reply += f'/updates - Get scheduled and mega jackpot details';
    
    bot.reply_to(message, reply,parse_mode='html')

  except Exception as e:
   print(e)
   bot.stop_polling()
   time.sleep(3)
   bot.stop_bot()
   time.sleep(3)
   bot.polling();

@bot.message_handler(commands=['website'])
def getWebsites(message):
  reply = f'<b>{website}</b>';
  bot.reply_to(message, reply,parse_mode='html')

@bot.message_handler(commands=['ca'])
def contractAddress(message):
  try:
  
    reply = f'<b>{ca}</b>';
    bot.reply_to(message, reply,parse_mode='html')

  except Exception as e:
   print(e)
   bot.stop_polling()
   time.sleep(3)
   bot.stop_bot()
   time.sleep(3)
   bot.polling();


@bot.message_handler(commands=['points'])
def points(message):
  try:
    message.text = message.text.replace("/points", "").strip()
    print(message.text)

    if message.text == '':
      reply = f'Please input wallet address.';
      reply += '\n \n';
      reply += f'ex :  /points 0x0000000000000000000000000000000000000000 ';
      bot.reply_to(message, reply,parse_mode='html')
      return;
    
    address = Web3.to_checksum_address(message.text);
    holderPoints = contract.functions.getPoints(address).call();

    totalPoints = contract.functions.getTotalPointsExt().call()
    
    chanceOfWinning = int((holderPoints / totalPoints) * 100);



    balance = Web3.from_wei(getBalance(address),'ether');
    reply = f'WALLET ADDRESS: <b>{address}</b>';
    reply += '\n \n'

    reply += f'BALANCE: <b>{balance}</b>';
    reply += '\n \n'
  
    reply += f'ACCUMULATED POINTS: <b>{holderPoints}</b>'
    reply += '\n \n'

    reply += f'CHANCE OF WINNING <b>{chanceOfWinning}%</b>'
    reply += '\n \n';
    reply += '\n \n';


    bot.reply_to(message, reply,parse_mode='html')
  
  except Exception as e:
    print(e)
    bot.stop_polling()
    time.sleep(3)
    bot.stop_bot()
    time.sleep(3)
    bot.polling();


@bot.message_handler(commands=['updates'])
def updates(message):
  try:
    message.text = message.text.replace("/updates", "").strip()
    totalRewards = web3.eth.get_balance(ca);
    lastBuyer = contract.functions.getLastBuyer().call();
    lastBuyTime = contract.functions.getLastBuyTime().call();


    lastBuyTimeReadable = localtime(lastBuyTime);

    lastBuyTimeReadable = strftime('%B %d, %Y %I:%M %p', localtime(lastBuyTime));
    idleTime = contract.functions.getMegaRewardIdle().call();
    datetime_obj=datetime.fromtimestamp(lastBuyTime)
    megaJackpotDate  = datetime_obj + timedelta(hours=idleTime);
    today = datetime.today()
    
    totalPoints = contract.functions.getTotalPointsExt().call()
   
    timeRem = today + (megaJackpotDate - today);
    dateTimeRemaining = timeRem.strftime('%B %d, %Y %I:%M %p')
    schedReward = totalRewards / 2;

    scheduledReward = contract.functions.getScheduledReward().call();
    datetime_obj_sched=datetime.fromtimestamp(scheduledReward)
    

    timeRemSched = today + (datetime_obj_sched - today);
    timeRemScheDisplay = timeRemSched.strftime('%B %d, %Y %I:%M %p');

    lastBuyTx = '';
    reply = f'<b><i>MEGA JACKPOT</i></b>';
    reply += '\n \n'
    reply += f'TOTAL REWARDS (ETH): <b>{Web3.from_wei(totalRewards,"ether")}</b>' ;
    reply += '\n \n'
    reply += f'LAST BUYER: <b>{lastBuyer}</b>' ;
    reply += '\n \n'
    reply += f'LAST BUY DATE/TIME: <b>{lastBuyTimeReadable}</b>' ;
    reply += '\n \n'
    reply += f'LAST BUY TX: <b>{lastBuyTx}</b>' ;
    reply += '\n \n'
    reply += f'IDLE TIME: <b>{idleTime} HRS</b>' ;
    reply += '\n \n'
    reply += f'ESTIMATED DISTRIBUTION TIME: <b>{dateTimeRemaining}</b>' ;
    reply += '\n \n'
    reply += '\n \n'
    reply += '\n \n'
    reply += f'<b><i>SCHEDULED REWARD</i></b>';
    reply += '\n \n'
    reply += f'TOTAL REWARDS (ETH): <b>{Web3.from_wei(schedReward,"ether")}</b>' ;
    reply += '\n \n'
    reply += f'TOTAL POINTS: <b>{totalPoints}</b>' ;
    reply += '\n \n'
    reply += f'ESTIMATED DISTRIBUTION TIME: <b>{timeRemScheDisplay}</b>' ;
    reply += '\n \n';
    reply += '\n \n';

    reply += f"OFFICIAL WEBSITE: {website}"
    reply += '\n \n';

    reply += f"UNISWAP: {website}"
    



    
    bot.reply_to(message, reply,parse_mode='html')
  


  except Exception as e:
   print(e)
   bot.stop_polling()
   time.sleep(3)
   bot.stop_bot()
   time.sleep(3)
   bot.polling();





bot.polling();

app.run()