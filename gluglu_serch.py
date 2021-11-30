import telebot
from googlesearch import search
bot = telebot.TeleBot("2129360495:AAHeghE5CxfeK1bZG-KnUpvN5GsBTAL4Djs", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

start_text = '''
🇺🇿 Assalomu alaykum. Bu botda siz google qidiruv tizimidan foydalanib kerakli linklarni olishingiz mumkin.

🇷🇺 Привет. В этом боте вы можете получить нужные ссылки с помощью поисковой системы Google.

🇺🇸 Hello. In this bot you can get the links you need using the google search engine.
'''

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text != '/start':
        try:
            r = search(f"{message.text}", num_results=10)
            n = 0
            text=''''''
            for i in r:
                text += f'{n} {i}\n'
                n +=1
            bot.send_message(message.chat.id, text)
        except:
            bot.send_message(message.chat.id, 'Not Found')
    else:
        bot.send_message(message.chat.id, start_text)



bot.infinity_polling()