# -*- coding: utf-8 -*-
import telebot
import parser
import markups as m

#main variables
TOKEN = "634318196:AAFO38miyi9DQg3o_mf39WFrdWRmTQoKzig"
bot = telebot.TeleBot(TOKEN)
build = ""
stand = ""


#@bot.message_handler(commands=['start', 'go', '17'])
@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Посмотреть текущее состояние или обновляем стенд?', reply_markup=m.start_markup)

@bot.message_handler(commands=['all'])
def showAll(message):
    f = open("ZOE.txt", 'r')
    zoe = f.read()
    f.close
    f = open("ZPE.txt", 'r')
    zpe = f.read()
    f.close
    f = open("17.txt", 'r')
    s17 = f.read()
    f.close
    f = open("Test-4.txt", 'r')
    test4 = f.read()
    f.close
    f = open("Test-5.txt", 'r')
    test5 = f.read()
    f.close
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, "На настоящий момент установлено\n17-й сервер: " + s17 + "\nTest-4: " + test4 + "\nTest-5: " + test5 + "\nЗОЭ: " + zoe + "\nЗПЭ: " + zpe, reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['deploy'])
def askSource(message):
    chat_id = message.chat.id
    text = message.text
    print("--------------------------------------------------------------")
    print("ID чата: ", chat_id)
    print("Текущий текст: ", text)
    print("Юзер ID", message.from_user.id)
    print("Юзернейм", message.from_user.username)
    print("--------------------------------------------------------------")
    msg = bot.send_message(chat_id, 'Выберите какой стенд обновляем', reply_markup=m.source_markup)
    bot.register_next_step_handler(msg, askBuild)

def askBuild(message):
    global stand
    chat_id = message.chat.id
    text = message.text
    stand = message.text
    print("--------------------------------------------------------------")
    print("ID чата: ", chat_id)
    print("Текущий текст: ", text)
    print("Стенд:", stand)
    print("Юзер ID", message.from_user.id)
    print("Юзернейм", message.from_user.username)
    print("--------------------------------------------------------------")
    msg = bot.send_message(chat_id, 'До какой версии обновляем стенд?', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, wrtBuild)

#@bot.message_handler(commands=['write'])
def wrtBuild(message):
    global build
    global stand
    chat_id = message.chat.id
    text = message.text
    file_name = str(stand) + '.txt'
    build = message.text
    print("--------------------------------------------------------------")
    print("ID чата: ", chat_id)
    print("Текущий текст: ", text)
    print("Стенд: ", stand)
    print("Билд: ", build)
    print("Имя файла: ", file_name)
    print("Юзер ID", message.from_user.id)
    print("Юзернейм", message.from_user.username)
    print("--------------------------------------------------------------")
    msg = bot.send_message(message.from_user.id, "Стенд " + stand + " обновился до версии " + build)
    f = open(file_name, 'w')
    f.write(build)
    f.close


@bot.message_handler(commands=['show'])
def shwMess(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, 'До какой версии обновляем стенд?')


bot.polling()