import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    '''Функция - обработчик стартового запроса, дает юзеру всю инфу'''
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('1', '2')  # Имена кнопок
    bot.send_message(message.chat.id, "Привет, я расскажу тебе анекдот! Напиши мне одно из следующих ключевых слов"
                                      " и я расскажу тебе анекдот на эту тему:")
    bot.send_message(message.chat.id, "1.Случайный анекдот с чёрным юмором\n2.Случайный добрый анекдот\n"
                                      "или просто начни что-то писать, а это продолжит нейросеть",  reply_markup=markup)

peaceful_joke = config.Peacefuljoke()
bad_joke = config.Badjoke()
neuron_joke = config.Neuronjoke()

@bot.message_handler(content_types=['text'])
def text(message):
    '''Функция - обрабатывает все приходящие запросы'''
    if message.text == "привет":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('1', '2')  # Имена кнопок
        bot.send_message(message.chat.id, "Привет, я расскажу тебе анекдот!"
                                          " Напиши мне номер одного из следующих ключевых слов,"
                                          " и я расскажу тебе анекдот на эту тему:")
        bot.send_message(message.chat.id, "1.Случайный анекдот с чёрным юмором\n2.Случайный добрый анекдот\n"
                                          "или просто начни что-то писать, а это продолжит "
                                          "нейросеть", reply_markup=markup)
    elif message.text == "3":
        bad_joke.generate()
        bot.send_message(message.chat.id, repr(bad_joke))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')
    elif message.text == "1":
        bad_joke.generate()
        bot.send_message(message.chat.id, repr(bad_joke))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')
    elif message.text == "2":
        peaceful_joke.generate()
        bot.send_message(message.chat.id, repr(peaceful_joke))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')
    elif message.text.lower() != "привет":
        neuron_joke.generate(message.text)
        bot.send_message(message.chat.id, repr(neuron_joke))
        bot.send_message(message.chat.id, 'Если хочешь вернуться к выбору, напиши мне "Привет"')


bot.polling(none_stop=True)
