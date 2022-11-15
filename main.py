import telebot

bot=telebot.TeleBot('5668057020:AAE0QSis5E5Yr8lslZ0dG63RZwa-1XGBS0c')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет , {message.from_user.first_name} {message.from_user.last_name} '
    bot.send_message(message.chat.id,mess)
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id,'уау')
bot.polling(none_stop=True)