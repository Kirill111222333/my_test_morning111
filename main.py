import os
import datetime
import telebot
from flask import Flask, request

API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Відповідь на будь-яке звернення
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я — тут!")

# Вебхук для прийому повідомлень
@app.route(f"/{API_TOKEN}", methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# Ручний запуск повідомлення
@app.route('/send-morning')
def send_morning():
    bot.send_message(os.environ.get("MY_CHAT_ID"), "Доброго ранку!")
    return 'OK'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
