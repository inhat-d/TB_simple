#maded by 7's grade child

import telebot

#about tokens you can read in "YouMayDontReadThis"
bot = telebot.TeleBot("YOUR_TOKEN")

#first command, /start in tg chat
@bot.message_handler(commands=["start"])    # IMPORTANT, write commands without slash
def start(message):
	bot.send_message(message.chat.id, f"Hello {message.from_user.username}, i am a bot answer example")

#second command, /help in tg chat
@bot.message_handler(commands=["help", "commands"])   # you can assign functions to multiple commands
def help(message):
	bot.send_message(message.chat.id, f"@{message.from_user.username}, here's my commands")
  bot.send_message(message.chat.id, "/start - hello command")
  bot.send_message(message.chat.id, "/help - this command")    #also you can write many messages

#there are many other commands, you can learn about them on YouTube 

bot.polling(none_stop=True)
#this command exists to prevent the project from terminating
