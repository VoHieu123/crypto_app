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

bot = Bot(token='6157706837:AAH8uz73oVZlU6dmDuHPVovX_EL8fUHL-J8')
user_ids = {"Hieu": "6228170215", "Evan": "..."}

def activate(message, to=["Hieu", "Evan"], alarm=False):
    if alarm == True:
        thread = threading.Thread(target=sound_thread)
        thread.start()

    for name in to:
        try:
            bot.send_message(chat_id=user_ids[name], text=message)
        except:
            pass
