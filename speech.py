
# Google
from gtts import gTTS
import os
tts = gTTS(text='GAME OVER', lang='en')
tts.save("GAME OVER.mp3")
os.system("GAME OVER.mp3")


# Microsoft
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Game Over")


# Python
import pyttsx
engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()

