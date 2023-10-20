import telegram_send
import pygame.mixer
import threading, time
import computer_specific

# from telegram import Bot, InputFile

# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot = Bot(token='6157706837:AAH8uz73oVZlU6dmDuHPVovX_EL8fUHL-J8')

# # Replace 'chat_id' with the chat ID of the user or group you want to send the sound to
# chat_id = '42652'

# # Replace 'your_sound_file.ogg' with the path to your sound file
# sound_file_path = 'Reveille.wav'

# # Send the sound file
# with open(sound_file_path, 'rb') as sound_file:
#     bot.send_audio(chat_id=chat_id, audio=InputFile(sound_file))

def sound_thread():
    pygame.mixer.init()
    sound = pygame.mixer.Sound(computer_specific.SOUND_PATH)
    sound.play()
    time.sleep(10)
    sound.stop()

def activate(message, alarm=True):
    if alarm == True:
        # Todo: So many threads?
        thread = threading.Thread(target=sound_thread)
        thread.start()
    try:
        telegram_send.send(messages=[message])
    except:
        pass
