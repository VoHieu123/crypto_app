import telegram_send
import pygame.mixer
import threading, time
import computer_specific
from telegram import Bot

# Todo: Evan user id

bot = Bot(token='6157706837:AAH8uz73oVZlU6dmDuHPVovX_EL8fUHL-J8')
user_ids = ["6228170215"]

def sound_thread():
    pygame.mixer.init()
    sound = pygame.mixer.Sound(computer_specific.SOUND_PATH)
    sound.play()
    time.sleep(10)
    sound.stop()

def activate(message, alarm=False):
    if alarm == True:
        # Todo: So many threads?
        thread = threading.Thread(target=sound_thread)
        thread.start()
    try:
        for user_id in user_ids:
            bot.send_message(chat_id=user_id, text=message)
    except:
        pass
