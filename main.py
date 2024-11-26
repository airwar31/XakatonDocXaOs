import telebot
import config
from telebot import types
import sqlite3


connection = sqlite3.connect("data_for_vcs.db")
cur = connection.cursor()
bot=telebot.TeleBot(config.token)
@bot.message_handler(commands=["start"])
def start(message):
  otvet = types.InlineKeyboardMarkup(row_width=2)
  msg=message.chat.id
  btn1=types.InlineKeyboardButton("Забронированные", callback_data='zabr')
  btn2=types.InlineKeyboardButton("Начатые", callback_data='start')
  btn3=types.InlineKeyboardButton("Законченные", callback_data='end')
  btn4=types.InlineKeyboardButton("Отменённые", callback_data='canceled')
  otvet.add(btn1,btn2,btn3,btn4)
  
  bot.send_message(msg,"Вы авторизовались")
  bot.send_message(msg,"Ниже,с помощью кнопок,вы можете настраивать фильтры ",reply_markup=otvet)
  

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

        if call.message:
            if call.data == "zabr":                
                  otvet = types.InlineKeyboardMarkup(row_width=2,row_width=1)
                  btn1=types.InlineKeyboardButton("Начатые", callback_data='start')
                  btn2=types.InlineKeyboardButton("Законченные", callback_data='end')
                  btn3=types.InlineKeyboardButton("Отменённые", callback_data='canceled')
                  btn4=types.InlineKeyboardButton("Сбросить фильтры", callback_data='back')
                  otvet.add(btn1,btn2,btn3,btn4)
                  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Все забронированыые конференеции',reply_markup=otvet)
                  
            elif call.data == "start":
              otvet = types.InlineKeyboardMarkup(row_width=2)
              btn1=types.InlineKeyboardButton("Забронированные", callback_data='zabr')
              btn2=types.InlineKeyboardButton("Законченные", callback_data='end')
              btn3=types.InlineKeyboardButton("Отменённые", callback_data='canceled')
              btn4=types.InlineKeyboardButton("Сбросить фильтры", callback_data='back')
              otvet.add(btn1,btn2,btn3,btn4)
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Все начатые конференции',reply_markup=otvet)

            elif call.data == "end":
              otvet = types.InlineKeyboardMarkup(row_width=2)
              btn1=types.InlineKeyboardButton("Забронированные", callback_data='zabr')
              btn2=types.InlineKeyboardButton("Начатые", callback_data='start')
              btn3=types.InlineKeyboardButton("Отменённые", callback_data='canceled')
              btn4=types.InlineKeyboardButton("Сбросить фильтры", callback_data='back')                
              otvet.add(btn1,btn2,btn3,btn4)
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Все оконченные конференеции',reply_markup=otvet)

            elif call.data == "canceled":
              otvet = types.InlineKeyboardMarkup(row_width=2)
              btn1=types.InlineKeyboardButton("Забронированные", callback_data='zabr')
              btn2=types.InlineKeyboardButton("Начатые", callback_data='start')
              btn3=types.InlineKeyboardButton("Законченые", callback_data='end')
              btn4=types.InlineKeyboardButton("Сбросить фильтры", callback_data='back')
              otvet.add(btn1,btn2,btn3,btn4)  
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Все отменённые конференеции',reply_markup=otvet)

            elif call.data == "back":
              otvet = types.InlineKeyboardMarkup(row_width=2)
              btn1=types.InlineKeyboardButton("Забранированные", callback_data='zabr')
              btn2=types.InlineKeyboardButton("Начатые", callback_data='start')
              btn3=types.InlineKeyboardButton("Законченные", callback_data='end')
              btn4=types.InlineKeyboardButton("Отменённые", callback_data='canceled')
              otvet.add(btn1,btn2,btn3,btn4)
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Ниже,с помощью кнопок,вы можете настраивать фильтры ",reply_markup=otvet)     














connection.close()
bot.polling(non_stop=True)   