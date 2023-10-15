from telethon.sync import TelegramClient
import geocoder
api_id = '26806912'
api_hash = 'a41d81a51347d3355126b4ae18b6da5e'
phone_number = '+998909885351'  # Raqamingizni kiriting



g = geocoder.ip('me')  # 'me' bu sizning IP manzilingiz
 

with TelegramClient(phone_number, api_id, api_hash) as client:
    # Raqamga qo'ng'iroq qilish
    target_phone_number = '+998909885351'  # Maqsadga qo'ng'iroq qilingan raqamni kiriting
   
    latlng = g.latlng

    if latlng:
        message = f'Current IP: Kenglik {latlng[0]}, Uzunlik {latlng[1]}'
        client.send_message(target_phone_number, message)
    else:
        print("Failed to retrieve IP information.")
