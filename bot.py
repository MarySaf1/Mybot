import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси
# PROXY = {'proxy_url': settings.PROXY_URL,
         # 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь')


# Функция, которая будет отвечать пользователю
def talk_to_me(update, context):
    # Получаем текст, который отправил пользователь, он храниться в update.message.text
    user_text = update.message.text
    # выводим сообщение в консоль
    print(user_text)
    # Отправляем пользователю его же сообщение
    update.message.reply_text(user_text)


def main():
    # передача ключа, который нам выдал BotFather
    mybot = Updater(settings.API_KEY, use_context=True)
    # для того, чтобы при наступлении события вызывалась наша функция
    dp = mybot.dispatcher
    # добавляем обработку события старт
    dp.add_handler(CommandHandler('start', greet_user))
    # добавляем обработку сообщения от пользователя
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Start Bot')
    mybot.start_polling()  # регулярное обращение бота к серверу
    mybot.idle()  # чтобы бот работал постоянно, пока не отключишь


if __name__ == '__main__':
    main()
