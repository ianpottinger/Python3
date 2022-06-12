#! /usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding
#GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]

import keyword
import multiprocessing
import concurrent
import threading
import asyncio

DEBUG_MODE = True
if DEBUG_MODE:
    import pdb
    #pdb.set_trace()
    import logging
    FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    #logging.basicConfig(level = logging.WARNING, format = FORMAT)
    #logging.basicConfig(level = logging.DEBUG, format = FORMAT)
    #logging.basicConfig(level = logging.ERROR, format = FORMAT)
    #logging.basicConfig(level = logging.CRITICAL, format = FORMAT)

RESERVED = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield']
KEYWORDS = keyword.kwlist


# Google
import googletrans
translator = googletrans.Translator()
text = input("Enter text to translate: ")
result = translator.translate(text, dest='en')
print(result.text)

from gtts import gTTS
import os
#import pyaudio
tts = gTTS(text='GAME OVER', lang='en')
tts.save("GAME OVER.mp3")
os.system("GAME OVER.mp3")

import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# Microsoft
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Game Over")

# Python
#!/usr/bin/python

from translate import Translator

translator = Translator(to_lang = "morse")
try:
   with open('test.txt', mode = 'r') as my_file:
      text = my_file.read()
      translation = translator.translate(text)
      print(translation)
except FileNotFoundError as error:
   print("Check if the file exists or not")

translation_languages = {'af' : 'Afrikaans',
                        'am' : 'Amharic',
                        'ar' : 'Arabic',
                        'az' : 'Azerbaijani',
                        'be' : 'Belarusian',
                        'bg' : 'Bulgarian',
                        'bn' : 'Bengali',
                        'bs' : 'Bosnian',
                        'ca' : 'Catalan',
                        'ceb' : 'Cebuano',
                        'co' : 'Corsican',
                        'cs' : 'Czech',
                        'cy' : 'Welsh',
                        'da' : 'Danish',
                        'de' : 'German',
                        'el' : 'Greek',
                        'en' : 'English',
                        'eo' : 'Esperanto',
                        'es' : 'Spanish',
                        'et' : 'Estonian',
                        'eu' : 'Basque',
                        'fa' : 'Persian',
                        'fi' : 'Finnish',
                        'fr' : 'French',
                        'fy' : 'Frisian',
                        'ga' : 'Irish',
                        'gd' : 'Scots Gaelic',
                        'gl' : 'Galician',
                        'gu' : 'Gujarati',
                        'ha' : 'Hausa',
                        'haw' : 'Hawaiian',
                        'he' : 'Hebrew',
                        'hi' : 'Hindi',
                        'hmn' : 'Hmong',
                        'hr' : 'Croatian',
                        'ht' : 'Haitian Creole',
                        'hu' : 'Hungarian',
                        'hy' : 'Armenian',
                        'id' : 'Indonesian',
                        'ig' : 'Igbo',
                        'is' : 'Icelandic',
                        'it' : 'Italian',
                        'iw' : 'Hebrew',
                        'ja' : 'Japanese',
                        'jw' : 'Javanese',
                        'ka' : 'Georgian',
                        'kk' : 'Kazakh',
                        'km' : 'Khmer',
                        'kn' : 'Kannada',
                        'ko' : 'Korean',
                        'ku' : 'Kurdish (Kurmanji)',
                        'ky' : 'Kyrgyz',
                        'la' : 'Latin',
                        'lb' : 'Luxembourgish',
                        'lo' : 'Lao',
                        'lt' : 'Lithuanian',
                        'lv' : 'Latvian',
                        'mg' : 'Malagasy',
                        'mi' : 'Maori',
                        'mk' : 'Macedonian',
                        'ml' : 'Malayalam',
                        'mn' : 'Mongolian',
                        'mr' : 'Marathi',
                        'ms' : 'Malay',
                        'ms' : 'Malay',
                        'mt' : 'Maltese',
                        'my' : 'Myanmar (Burmese)',
                        'ne' : 'Nepali',
                        'nl' : 'Dutch',
                        'no' : 'Norwegian',
                        'ny' : 'Chichewa',
                        'pa' : 'Punjabi',
                        'pl' : 'Polish',
                        'ps' : 'Pashto',
                        'pt' : 'Portuguese',
                        'ro' : 'Romanian',
                        'ru' : 'Russian',
                        'sd' : 'Sindhi',
                        'si' : 'Sinhala',
                        'sk' : 'Slovak',
                        'sl' : 'Slovenian',
                        'sm' : 'Samoan',
                        'sn' : 'Shona',
                        'so' : 'Somali',
                        'sq' : 'Albanian',
                        'sr' : 'Serbian',
                        'st' : 'Sesotho',
                        'su' : 'Sundanese',
                        'sv' : 'Swedish',
                        'sw' : 'Swahili',
                        'ta' : 'Tamil',
                        'te' : 'Telugu',
                        'tg' : 'Tajik',
                        'th' : 'Thai',
                        'tl' : 'Filipino',
                        'tr' : 'Turkish',
                        'uk' : 'Ukrainian',
                        'ur' : 'Urdu',
                        'uz' : 'Uzbek',
                        'vi' : 'Vietnamese',
                        'xh' : 'Xhosa',
                        'yi' : 'Yiddish',
                        'yo' : 'Yoruba',
                        'zh-CN' : 'Chinese (Simplified)',
                        'zh-TW' : 'Chinese (Traditional)',
                        'zu' : 'Zulu'}

import pyttsx
engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()


import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="based questions to ask an AI",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)