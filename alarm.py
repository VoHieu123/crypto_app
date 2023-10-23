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
    is_thread_running = False

is_thread_running = False
thread = threading.Thread(target=sound_thread)

# Todo: Evan user id

bot = Bot(token='6157706837:AAH8uz73oVZlU6dmDuHPVovX_EL8fUHL-J8')
user_ids = ["6228170215"]

def activate(message, alarm=False):
    if alarm == True and not is_thread_running:
        thread.start()
        is_thread_running = True

    try:
        for user_id in user_ids:
            bot.send_message(chat_id=user_id, text=message)
    except:
        pass
