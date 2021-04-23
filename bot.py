import random
import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, я расскажу тебе анекдот! Напиши мне одно из следующих ключевых слов"
                                      " и я расскажу тебе анекдот на эту тему:")
    bot.send_message(message.chat.id, "1)Коза \n2)Ананасы")


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет, я расскажу тебе анекдот!"
                                          " Напиши мне номер одного из следующих ключевых слов,"
                                          " и я расскажу тебе анекдот на эту тему:")
        bot.send_message(message.chat.id, "1.Случайный анекдот с чёрным юмором\n2.Случайный добрый анекдот\n3.Коза\n"
                                          "4.Ананасы")
    elif message.text == "3":
        bot.send_message(message.chat.id, repr(config.joke1))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')
    elif message.text == "4":
        bot.send_message(message.chat.id, repr(config.joke2))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')
    elif message.text == "1":
        bot.send_message(message.chat.id, random.choice(config.List1))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')
    elif message.text == "2":
        bot.send_message(message.chat.id, random.choice(config.List2))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')
    else:
        bot.send_message(message.chat.id, "Не понимаю о чём ты, напиши: 'Привет'")


bot.polling(none_stop=True)
