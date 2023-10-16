from telethon.sync import TelegramClient
import geocoder
api_id = '26806912'
api_hash = 'a41d81a51347d3355126b4ae18b6da5e'
phone_number = '+998909885351'  # Raqamingizni kiriting



import os
import sys
import time
import random
import os.path
import requests
import threading

os.system("git pull")
os.system("clear")
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)
banner = f"""

▒███████▒▓█████  ██▀███   ▒█████  
▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒
░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒
  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░
▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ 
░ ░ ░ ░ ░   ░     ░░   ░ ░ ░ ░ ▒  
  ░ ░       ░  ░   ░         ░ ░  
░ 
 

"""
print (banner)

g = geocoder.ip('me')  # 'me' bu sizning IP manzilingiz
 

with TelegramClient(phone_number, api_id, api_hash) as client:
    # Raqamga qo'ng'iroq qilish
    target_phone_number = input("Jo'natilishi kerak bo'lgan raqamni kiriting(+998): ")  # Maqsadga qo'ng'iroq qilingan raqamni kiriting
   
    latlng = g.latlng

    if latlng:
        habar = input("Jo'natilshi kerak bo'lgan habarni kiriting:  ")
        message = f'Current IP: {latlng[0]}  {latlng[1]} \n {habar}'
        client.send_message(target_phone_number, message)
        print ('Success')
    else:
        print("Failed to retrieve IP information.")
