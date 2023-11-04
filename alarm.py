import pygame.mixer
import threading
import computer_specific
from telegram import Bot

pygame.mixer.init()
risk_sound = pygame.mixer.Sound(computer_specific.RISK_SOUND_PATH)
position_sound = pygame.mixer.Sound(computer_specific.POSITION_SOUND_PATH)
bot = Bot(token=computer_specific.BOT)
user_ids = {"Hieu": "6228170215", "Evan": "1531898366"}
timer_lock = True

def stop_sound():
    global timer_lock
    timer_lock = True
    risk_sound.stop()

def send_telegram_message(to, message):
    for name in to:
        try:
            bot.send_message(chat_id=user_ids[name], text=message)
        except Exception:
            pass

def activate(message, to=["Hieu", "Evan"], alarm=False, risk_sound=True):
    global timer_lock
    if alarm and timer_lock:
        timer_lock = False
        my_timer = threading.Timer(10, stop_sound)
        my_timer.start()
        if risk_sound:
            risk_sound.play()
        else:
            position_sound.play()

    message_thread = threading.Thread(target=send_telegram_message, args=(to, message))
    message_thread.start()