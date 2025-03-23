import telebot
import random
import os
import requests

bot = telebot.TeleBot('7519780161:AAHfF46_C7vprQjNZENU5hgM8PKjF53U6C4')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['mem'])
def send_mem(message):
    meme_folder = 'pon/' 
    if not os.path.exists(meme_folder):  
        bot.send_message(message.chat.id, "Папка с мемами не найдена 😢")
        return

    meme_files = os.listdir(meme_folder)  
    if meme_files:
        meme_path = os.path.join(meme_folder, random.choice(meme_files)) 
        with open(meme_path, 'rb') as f:
            bot.send_photo(message.chat.id, f)
    else:
        bot.send_message(message.chat.id, "В папке нет мемов 😢")

@bot.message_handler(commands=['duck'])
def duck(message):
    """По команде /duck отправляет случайное изображение утки."""
    image_url = get_duck_image_url()
    bot.send_photo(message.chat.id, image_url)

bot.polling()
