import telebot
import random
#import pickle 
import pandas as pd

#from pyrogram import enums
session = requests.Session()
session.verify = False

#запуск бота
bot = telebot.TeleBot('5268624306:AAFfFEOaH7Ep8CYi0ZLfNrHH27L5x3xRsng')
#df_test = pd.DataFrame(columns = ['user_id', 'text'])
df_test= pd.read_csv("test.csv", header=0, sep=';')

@bot.message_handler(commands=['start'])
def send_hello(message):
	bot.send_message(message.chat.id, 'Hi')
@bot.message_handler(content_types=['text'])
def write_down(message):
	global df_test
	bot.send_message(message.chat.id, str(message.text))
	df_test=df_test.append({
		'user_id': message.chat.id, 
		'text':message.text, }, ignore_index=True)
	print(df_test)
	df_test.to_csv('test.csv')


#запуск
bot.polling()

