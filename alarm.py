import pygame.mixer
import threading, time
import computer_specific
from telegram import Bot

def sound_thread():
    pygame.mixer.init()
    sound = pygame.mixer.Sound(computer_specific.SOUND_PATH)
    sound.play()
    time.sleep(10)
    sound.stop()

# 6483313153:AAFUrrHFLS4cQGC-Raif32Pc-wE-OtQocDM
bot = Bot(token=computer_specific.BOT)
user_ids = {"Hieu": "6228170215", "Evan": "1531898366"}

def activate(message, to=["Hieu", "Evan"], alarm=False):
    if alarm == True:
        thread = threading.Thread(target=sound_thread)
        thread.start()

    for name in to:
        try:
            bot.send_message(chat_id=user_ids[name], text=message)
        except:
            pass
