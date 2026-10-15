import telebot
import easyocr
import csv
from datetime import datetime

# 1. GANTI TOKEN KAMU
TOKEN = "GANTI_TOKEN_DISINI"
bot = telebot.TeleBot(TOKEN)

# 2. Siapin Otak OCR (sekali aja pas bot hidup)
print("Loading OCR...")
reader = easyocr.Reader(['id','en'], gpu=False)
print("OCR Siap!")

# 3. Kalau ada foto masuk
@bot.message_handler(content_types=['photo'])
def handle_foto(message):
    bot.reply_to(message, "Foto diterima, lagi dibaca...")

    # Download foto
    file_info = bot.get_file(message.photo[-1].file_id)
    foto = bot.download_file(file_info.file_path)
    open("nota.jpg", "wb").write(foto)

    # Baca pakai AI
    hasil = reader.readtext("nota.jpg", detail=0)
    teks = " ".join(hasil)

    # Balas & Simpen
    bot.reply_to(message, f"Hasil baca:\n{teks}")
    
    with open("hasil.csv", "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([datetime.now(), teks])

print("Bot mudah SIAP!")
bot.infinity_polling()