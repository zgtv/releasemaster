from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/all')
start_markup_btn2 = types.KeyboardButton('/deploy')
start_markup.add(start_markup_btn1, start_markup_btn2)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('17')
source_markup_btn2 = types.KeyboardButton('Test-4')
source_markup_btn3 = types.KeyboardButton('Test-5')
source_markup_btn4 = types.KeyboardButton('ZOE')
source_markup_btn5 = types.KeyboardButton('ZPE')
source_markup.add(source_markup_btn1, source_markup_btn2, source_markup_btn3, source_markup_btn4, source_markup_btn5)
