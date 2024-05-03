import telebot
import requests
import schedule 
import json
import time
API = "https://api.geckoterminal.com/api/v2/networks/polygon_pos/pools/0x1de0365abf5fc33450ac77e50070defb1eae1dd7"



import requests
import telebot

# Указываем токен вашего бота
TOKEN = '6506852425:AAFkWBj9KYGDaTGQU7Uq12PTRE_01bRsQG8'

chat_id = '753848489'
# Создаем экземпляр бота

bot = telebot.TeleBot(TOKEN)

def get_data_from_api():
    response = requests.get(API)
    data = response.json()
    price_change = data["data"]["attributes"]["price_change_percentage"]["m5"]
    price = data["data"]["attributes"]["base_token_price_usd"]
    return price_change, price

@bot.message_handler(commands=['start'])
def send_data_to_telegram(message):
    price_change, price = get_data_from_api()
    bot.send_message(message.chat.id, f"Price Change: {price_change}\nPrice: {price}")



def main():
    
    
    while True:
        
        price_change, price = get_data_from_api()
        bot.send_message(chat_id, f"Price Change: {price_change}\nPrice: {price}")
        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    # bot.polling(none_stop=True)
    main()