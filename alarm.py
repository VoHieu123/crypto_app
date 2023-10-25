import pygame.mixer
import threading
import computer_specific
from telegram import Bot

pygame.mixer.init()
sound = pygame.mixer.Sound(computer_specific.SOUND_PATH)
bot = Bot(token=computer_specific.BOT)
user_ids = {"Hieu": "6228170215", "Evan": "1531898366"}
timer_lock = threading.Lock()

def activate(message, to=["Hieu", "Evan"], alarm=False):
    if alarm == True:
        with timer_lock:
            my_timer = threading.Timer(10, lambda: sound.stop())
            my_timer.start()
            sound.play()

    for name in to:
        try:
            bot.send_message(chat_id=user_ids[name], text=message)
        except:
            pass
