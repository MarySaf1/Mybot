import logging
import settings
import ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси
# PROXY = {'proxy_url': settings.PROXY_URL,
         # 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

today = str(date.today())

planets = {
    "Mercury": ephem.Mercury(today),
    "Venus": ephem.Venus(today),
    "Mars": ephem.Mars(today),
    "Jupiter": ephem.Jupiter(today),
    "Saturn": ephem.Saturn(today),
    "Uranus": ephem.Uranus(today),
    "Neptune": ephem.Neptune(today)
}


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь')


# Функция, которая будет отвечать пользователю
# def talk_to_me(update, context):
#     # Получаем текст, который отправил пользователь, он хранится в update.message.text
#     user_text = update.message.text
#     # выводим сообщение в консоль
#     print(user_text)
#     # Отправляем пользователю его же сообщение
#     update.message.reply_text(user_text)

def planet(update, user_planet):
    user_text = update.message.text.split()
    if user_text[0] in planets:
        sozv = planets[user_text[0]]
        const = ephem.constellation(sozv)
        update.message.reply_text(', '.join(map(str, const)))


def main():
    # передача ключа, который нам выдал BotFather
    mybot = Updater(settings.API_KEY, use_context=True)
    # для того, чтобы при наступлении события вызывалась наша функция
    dp = mybot.dispatcher
    # добавляем обработку события старт
    dp.add_handler(CommandHandler('start', greet_user))
    # добавляем обработку сообщения от пользователя
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, planet))
    logging.info('Start Bot')
    mybot.start_polling()  # регулярное обращение бота к серверу
    mybot.idle()  # чтобы бот работал постоянно, пока не отключишь


if __name__ == '__main__':
    main()
