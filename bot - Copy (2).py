import telebot
import parser
import markups as m

#main variables
TOKEN = "634318196:AAFO38miyi9DQg3o_mf39WFrdWRmTQoKzig"
bot = telebot.TeleBot(TOKEN)
deploy = {}

#@bot.message_handler(commands=['start', 'go', '17'])
@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Посмотреть текущее состояние или обновляем стенд?', reply_markup=m.start_markup)


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
    chat_id = message.chat.id
    text = message.text
    deploy[chat_id] = [text]
    build = list(deploy.values())
    stand = build [0]
    file_name = str(build [0]) + '.txt'
    print("--------------------------------------------------------------")
    print("ID чата: ", chat_id)
    print("Текущий текст: ", text)
    print("Билд: ", build)
    print("Стенд :", stand)
    print("Имя файла: ", file_name)
    print("Юзер ID", message.from_user.id)
    print("Юзернейм", message.from_user.username)
    print("--------------------------------------------------------------")
    msg = bot.send_message(chat_id, 'До какой версии обновляем стенд?', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, wrtBuild)

#@bot.message_handler(commands=['write'])
def wrtBuild(message):
    chat_id = message.chat.id
    text = message.text
    deploy[chat_id].append(text)
    build = list(deploy.values())
    file_name = str(build [0]) + '.txt'
    stand = build [0]
#    buildNum = build[1]
    print("--------------------------------------------------------------")
    print("ID чата: ", chat_id)
    print("Текущий текст: ", text)
    print("Билд: ", build)
#    print("Номер билда: ", buildNum)
#    print("Выбранный стенд: ", deploy[chat_id].values(1))
    print("Имя файла: ", file_name)
    print("Юзер ID", message.from_user.id)
    print("Юзернейм", message.from_user.username)
    print("Ключи словаря", deploy.keys())
    print("Значения словаря", deploy.values())
    print("Словарь", deploy.items())
    print("--------------------------------------------------------------")
    msg = bot.send_message(message.from_user.id, "Выбранный стенд: " + stand)
#    f = open(file_name, 'w')
#    f.write('Версия в ' + stand + ": " + build + ", установлена " + message.from_user.username)
#    f.close
    


# def askName(message):
#     chat_id = message.chat.id
#     text = message.text
#     if not text.isdigit():
#         msg = bot.send_message(chat_id, 'Я хочу число')
#         bot.register_next_step_handler(msg, askName)
#         return
#     msg = bot.send_message(chat_id, 'Спасибо, я запомнил что число: ' + text)

@bot.message_handler(commands=['show'])
def shwMess(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, 'До какой версии обновляем стенд?')


bot.polling()