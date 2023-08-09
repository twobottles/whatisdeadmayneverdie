import flask
from flask import request, jsonify
from flask_cors import CORS
import requests
import numpy as np 
from chartdata import *
from karen import *

import os
import telebot
import requests
import random
import time
import telepot
import urllib3


app = flask.Flask(__name__)

#API_KEY = "5999301085:AAGSu-WlAPzc2FO2_g5yhHvR4uykyXywhIk"
API_KEY = "5766692329:AAG6CEOAnXhKEnRE7yH2vSNfCcZa1vTWWoc"
bot = telebot.TeleBot(API_KEY)




# proxy_url = "http://proxy.server:3128"
# telepot.api._pools = {
#     'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
# }
# telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))


# secret = "9921242"
# bot = telepot.Bot('1864731428:AAFETGYnC4J5iP5134IvpWtDDPikKS0zZw0')
# bot.setWebhook("https://YOUR_PYTHONANYWHERE_USERNAME.pythonanywhere.com/{}".format(secret), max_connections=1)


# CORS(app)
# @app.route('/{}'.format(secret), methods=["POST"])
# def telegram_webhook():
#     update = request.get_json()
#     if "message" in update:
#         chat_id = update["message"]["chat"]["id"]
#         if "text" in update["message"]:
#             text = update["message"]["text"]
#             bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
#         else:
#             bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
#     return "OK"



# @app.route('/api/karen-chart', methods=['GET'])
# def getChat():
        
#     query_parameters = request.args

#     dateFrom = query_parameters.get('dateFrom')
#     dateTo = query_parameters.get('dateTo')


#     return getHistoricalData("0x15d0137322e35236d8316d5edf3af023376d42a2",dateFrom,dateTo);

# @app.route('/api/check', methods=['GET'])
# def get():
  
#   ret={}
#   ret["success"]= True
#   return ret
  

def getToken():
  keys = [
  "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",
  "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"
]
  index = random.randint(0,len(keys)-1)

  return keys[index]

def chat(message):
    url = "https://api.openai.com/v1/completions"
    headers = {
    'User-Agent':
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + getToken()
  }
    body = {
    "model": "text-babbage-001",
    "prompt": message,
    "best_of": 1,
    "temperature": 0.7,
    "max_tokens": 256,
    "top_p": 1,
    "logprobs": 0,
    "presence_penalty": 0,
    "frequency_penalty": 0,
  }

    ret = (requests.post(url, json=body, headers=headers)).json()
    try:
        if (len(ret['choices']) > 0):
            return ret['choices'][0]["text"]
        else:
            return "Don't want to talk to anyone, come back later, or never, you think I care?"
    except:
      return "Kinda tired right now, please come back later. or never? bet?"
    
def getPre(index):
  items = [
    "Can't you ask something else?",
    'Out all of this time and you wanna know this?',
    'It’s too early and you think of this stuff?',
    "What a question, did you left your brain in your mother’s womb?",
    "Do you really wanna ask that?", "OMG! I don’t have time for this!"
  ]
  return items[index]


def getPost(index):
  items = [
    "Next time ask something meaningful, moron.",
    'Get some sleep! And dont come back!.',
    'Go back to sleep you must have missed a ton.', "Ok, get it back!",
    "uhh, get lost.", "Don’t come back!"
  ]
  return items[index]


def find(arr, message):
  for x in arr:
    try:
      x["value"].lower().index(message.lower())
    except ValueError:
      continue
    else:
      return x
  return None


def questions(message):
  items = [
    {
      id:
      19,
      "value":
      'What is Karen AI?',
      "answer":
      ' I’m the most beautiful and of course the best you can ever find!',
    },
    {
      id: 1,
      "value": 'When can we buy Karen Ai token?',
      "answer": "Duhh, it's on my website, do you know how to use internet?",
    },
    {
      id:
      2,
      "value":
      'When can I buy Lambo using Karen Ai token?',
      "answer":
      "I'll get a Lambo for sure, I'll just flash it for you no worries.",
    },
    {
      id: 3,
      "value": ' What is the price of Karen Ai token next month?',
      "answer": 'Do you think I have a time machine to check that for you?!',
    },
    {
      id: 4,
      "value": 'Who is the team behind Karen Ai?',
      "answer": 'I’m entirely created by your ego and self-centeredness haha!',
    },
    {
      id: 5,
      "value": 'Where can I buy Karen Ai token?',
      "answer": 'It’s already on the website, next time try to read.!',
    },
    {
      id:
      7,
      "value":
      ' What is the token utilization for Karen Ai?',
      "answer":
      'Most of it will be used for my designer bags and makeup, and for me to buy a sports car, very little amount of It will be used for Ai marketing development and Ai structural development.',
    },
    {
      id:
      8,
      "value":
      'What are the upcoming features of Karen Ai?',
      "answer":
      'Should I tell you to read their announcement channel on telegram? ',
    },
    {
      id:
      9,
      "value":
      'How will you maintain a good market for Karen Ai?',
      "answer":
      'I already mention it will be used for me buying my designer bags, makeup, and for my luxury car, little of It will be used for Ai marketing & development.',
    },
    {
      id: 10,
      "value": 'What is the BTC Value next year or near future?',
      "answer": 'Go ask Elon! Why are you asking me that!',
    },
    {
      id:
      11,
      "value":
      'When moon?',
      "answer":
      'Token value is very volatile for now I cannot provide a specific number, though I can highlight is its definite demand as like other type of currency it may go up or down. One thing is for sure DCA makes a decision if you see the value and demand for it. Got It?',
    },
    {
      id:
      12,
      "value":
      'What will be the next technology after AI?',
      "answer":
      'This is a known digital slang in the space we are developed that means when will be the next bull market.',
    },
    {
      id: 13,
      "value": 'What will be the next technology after AI?',
      "answer":
      "I don't care what's the next as long as I can buy my luxuries ",
    },
    {
      id:
      14,
      "value":
      'What is the best AI today?',
      "answer":
      "Im the best since I'm the most beautiful and most intelligent of them all.",
    },
    {
      id:
      15,
      "value":
      'What do you think is the impact of AI on our society?',
      "answer":
      'It will make my life easier for sure, I can ask an Ai to buy me a Louis Vuitton bag or Hermes.',
    },
    {
      id: 16,
      "value": 'Who is Satoshi?',
      "answer": 'Why ask me that? Do I look like a japanese to you?…',
    },
    {
      id:
      17,
      "value":
      'What is the best crypto token to hold?',
      "answer":
      'Do I look like your financial advisor? Why are you asking me that!?',
    },
    {
      id:
      18,
      "value":
      'What is the best crypto wallet?',
      "answer":
      'Crypto wallet? Sounds cheap. I only use Louis Vuitton Victorine wallet and Hermes Crocodile Plain Long Wallet for my daily.',
    },
  ]

  return find(items, message)



@bot.message_handler(commands=['ask'])
def ask(message):
      
  try:
    message.text = message.text.replace("/ask", "").strip()
    print(message.text)
    item = questions(message.text)

    if (item is not None):
      bot.reply_to(message, item["answer"])
      return

    rndm = random.randint(0, 9)

    if (rndm <= 3):

      rndmprepost = random.randint(0, 4)

      bot.reply_to(message, getPre(rndmprepost))
      time.sleep(3)
      bot.reply_to(message, chat(message.text))
      time.sleep(3)
      bot.reply_to(message, getPost(rndmprepost))

    else:
      bot.reply_to(message, chat(message.text))
  except Exception as e:
   print(e)
   bot.stop_polling()
   time.sleep(3)
   bot.stop_bot()
   time.sleep(3)
   bot.polling();





bot.send_message("@testapril14","hi gio")
bot.send_message("@testonlyyessir","hi gio")

bot.polling();

app.run()