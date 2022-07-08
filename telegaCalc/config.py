# файл конфига с токеном

import telebot
import datetime
from telegram import message

# import kod_v2
# from kod_v2 import record_m, record_s
from functools import wraps    # запрет на отправку собщений всеми, крме админа


#указание токена бота
token = '5352935775:AAENA4YzYLSlHp6jqdfI3mR9wOK89o7aGaw'


# запрет на отправку собщений всеми, крме админа
LIST_OF_ADMINS = [378989142]

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped
