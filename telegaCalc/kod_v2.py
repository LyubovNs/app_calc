import telebot
from telebot import types
import logging
import config
from script_calc import holiday

#логирование

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


#указание токена бота из файла конфига
bot = telebot.TeleBot(config.token)

#тело приветствия

welcome_message = {
    'start':
        u'Здравствуй, chat.username\n'
        u'Я умею рассчитывать аванс и зарплату, но пока не умею считать отпускные.\n\n'
        u'Давай попробуем?\n'
        u'Выбери, что будем считать: "Аванс" или "Зарплата"',

    'help':
        u'Выбери, что будем считать: "Аванс" или "Зарплата"'
    }

# month_message = {
#     'choose':
#         u'Для какого месяца считаем?\n'
# }

# функция выбора, что считать
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Аванс')
    markup.row('Зарплата')

    # сообщение пользователю
    msg = bot.send_message(message.from_user.id, welcome_message['start'].format(name=message.from_user.id), reply_markup=markup)
    # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции month
    bot.register_next_step_handler(msg, month)

# функция выбора месяца
@bot.message_handler(content_type=['text'])
def month(message):
    month = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if message.text == 'Аванс' or message.text == 'Зарплата':
        month.row('Январь')
        month.row('Февраль')
        month.row('Март')
        month.row('Апрель')
        month.row('Май')
        month.row('Июнь')
        month.row('Июль')
        month.row('Август')
        month.row('Сентябрь')
        month.row('Октябрь')
        month.row('Ноябрь')
        month.row('Декабрь')
        month.row('Назад')

    # bot.send_message(message.from_user.id, month_message['choose'].format(name=message.from_user.id))
    msg = bot.send_message(message.from_user.id, 'Выберите месяц', reply_markup=month)
    # здесь будет указание на то, в какой следующей функции будут использоваться данные
    bot.register_next_step_handler(msg, send_welcome)

# для возврата в главное меню
def exit(message):
    if message.text == 'Назад':
        send_welcome(message)


# расчет аванса















#проверка на новые сообщения
bot.polling(none_stop=True, interval=0)

