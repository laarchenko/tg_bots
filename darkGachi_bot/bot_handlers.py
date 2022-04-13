from config import *
import telebot
from telebot import types
from random import choice
import os
bot = telebot.TeleBot(TOKEN)
urls = []

files = os.listdir("resourses")
for i in files:

    message = bot.send_audio( MY_ID , audio=open( "resourses/"+i , "rb" ) )
    urls.append(message.audio.file_id)

@bot.message_handler(content_types=["audio", "voice"], func=lambda message: message.chat.id== 218196255)
def content_adding(message):
	bot.send_message(message.chat.id, message.audio.file_id)
	urls.append(message.audio.file_id)

@bot.inline_handler(lambda chosen_inline_result: True)
def query_text(chosen_inline_result):
    answers = []
    count = 0
    for i in urls:
        answers.append ( types.InlineQueryResultCachedAudio ( id=str(count) , audio_file_id= i, parse_mode='' ) )
        count+=1
    bot.answer_inline_query ( chosen_inline_result.id , answers )



