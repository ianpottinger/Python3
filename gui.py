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

import os
import keyword
import win32com.client as wincl
import multiprocessing
import concurrent
import threading
import asyncio

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox

from pygame import mixer
from PIL import ImageTk,Image
import cairosvg

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

global volume
volume = 100
global playing
playing = False
global paused
paused = True
global muted
muted = False
global audiofile
audiofile = "G:\WorkingData\My Music\Portable\Soul Divas\VideoGames.mp3"

speak = wincl.Dispatch("SAPI.SpVoice")

filename = r'G:\WorkingData\Work @ Home\Humanity\My Icon.png'
flag = Image.open(filename)
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]
flag.save('logo.ico', sizes = icon_sizes)

parent = Tk()
parent.geometry() #'800x600'
parent.title("Python GUI")
parent.iconbitmap('logo.ico')

flag = ImageTk.PhotoImage(Image.open(r"G:\WorkingData\Work @ Home\Humanity\My Icon.png"))

leftframe = Frame(parent)
leftframe.grid(row = 0, column = 0, padx = 5, pady = 5)

centreframe = Frame(parent)
centreframe.grid(row = 0, column = 1, padx = 5, pady = 5)

rightframe = Frame(parent)
rightframe.grid(row = 0, column = 2, padx = 5, pady = 5)


statusbar = Label(parent, text = "Status bar", relief = SUNKEN)
statusbar.grid(row = 1, column = 1)


imagefile = PhotoImage(file = 'G:\WorkingData\Work @ Home\Humanity\My Icon.png')
labelimage = Label(centreframe, image = imagefile)
labelimage.grid(row = 1, column = 0, padx = 5, pady = 5)


label = Label(centreframe, text = audiofile)
label.grid(row = 2, column = 0, pady = 10)


controls = Frame(centreframe, relief = SUNKEN, borderwidth = 3)
controls.grid(row = 3, column = 0, padx = 5, pady = 5)


textbox = Entry(centreframe, relief = SUNKEN, borderwidth = 3)
textbox.grid(row = 4, column = 0, padx = 5, pady = 5)


menubar = Menu(parent)
parent.config(menu = menubar)

submenu = Menu(menubar, tearoff = 0)

menubar.add_cascade(label = "File", menu = submenu)

def open_file():
    global audiofile
    audiofile = filedialog.askopenfilename()
    if not audiofile == '':
        mixer.music.load(audiofile)
        label['text'] = audiofile
        if playing and not paused:
            mixer.music.play(-1)
            statusbar['text'] = f"Playing {os.path.basename(audiofile)}"

submenu.add_command(label = "Open", command = open_file)


submenu.add_command(label = "Close")


submenu.add_command(label = "Quit", command = parent.destroy)


submenu = Menu(menubar, tearoff = 0)


menubar.add_cascade(label = "Help", menu = submenu)


def about():
    tkinter.messagebox.showinfo("About Player", "Tkinter, PyGame audio player")

submenu.add_command(label = "About", command = about)

submenu.add_command(label = "Help")


mixer.init()
mixer.music.set_volume(volume / 100)
mixer.music.load(audiofile)


def rewind():
    speak.Speak("Come again selectA")
    mixer.music.rewind()

rewind = Button(controls, text = "Rewind", command = rewind, relief = RAISED, borderwidth = 3)
rewind.grid(row = 0, column = 0, padx = 5, pady = 5)


def play():
    global playing
    global paused
    try:
        mixer.music.play(-1)
        playing = True
        pause.config(text = "Pause")
        paused = False
        speak.Speak("Play da riddim")
        statusbar['text'] = f"Playing {os.path.basename(audiofile)}"
    except:
        tkinter.messagebox.showinfo("Error", "Error playing audio file")

play = Button(controls, text = "Play", command = play, relief = RAISED, borderwidth = 4)
play.grid(row = 0, column = 1, padx = 5, pady = 5)


def pause():
    global playing
    global paused
    if playing == True and paused == True:
        mixer.music.unpause()
        pause.config(text = "Pause")
        speak.Speak("bless up yo' self")
        statusbar['text'] = f"Playing {os.path.basename(audiofile)}"
        paused = False
    elif playing == True and paused == False:
        mixer.music.pause()
        pause.config(text = "Unpause")
        speak.Speak("Pullllllllllllll uppppp")
        statusbar['text'] = f"Paused {os.path.basename(audiofile)}"
        paused = True

pause = Button(controls, text = "Pause", command = pause, relief = RAISED, borderwidth = 5)
pause.grid(row = 0, column = 2, padx = 5, pady = 5)


def stop():
    global playing
    mixer.music.stop()
    speak.Speak("Likkle more")
    statusbar['text'] = f"Audio stopped"
    playing = False

stop = Button(controls, text = "Stop", command = stop, relief = RAISED, borderwidth = 4)
stop.grid(row = 0, column = 3, padx = 5, pady = 5)


def forward():
    speak.Speak("Soon forward")
    pass

forward = Button(controls, text = "Forward", command = forward, relief = RAISED, borderwidth = 3)
forward.grid(row = 0, column = 4, padx = 5, pady = 5)


playlist = Listbox(rightframe)
playlist.insert(0, audiofile)
playlist.insert(1, filename)
playlist.grid(row = 1, column = 0, padx = 10, pady = 10)

output = Frame(rightframe, relief = SUNKEN, borderwidth = 3)
output.grid(row = 3, column = 0, padx = 5, pady = 5)


comments = Listbox(rightframe)
comments.insert(0, "Bumbaclart")
comments.insert(1, "Lliiarta")
comments.grid(row = 5, column = 0, padx = 10, pady = 10)

def submit():
    speak.Speak(textbox.get() )
    comments.insert(0, textbox.get() )
    textbox.insert("")

record = Button(centreframe, text = "Submit", command = submit, relief = RAISED, borderwidth = 3)
record.grid(row = 4, column = 0, padx = 5, pady = 5)


def mute():
    global playing
    global volume
    global muted
    if playing == True and muted == True:
        mixer.music.set_volume(volume / 100)
        position.set(volume)
        mute.config(text = "Mute")
        statusbar['text'] = f"Unmuted {os.path.basename(audiofile)}"
        muted = False
    elif playing == True and muted == False:
        mixer.music.set_volume(0)
        position.set(0)
        mute.config(text = "Unmute")
        statusbar['text'] = f"Muted {os.path.basename(audiofile)}"
        muted = True

mute = Button(output, text = "Mute", command = mute, relief = RAISED, borderwidth = 3)
mute.grid(row = 0, column = 0, padx = 5, pady = 5)


def position(val):
    global volume
    mixer.music.set_volume(int(val) / 100)

position = Scale(output, from_ = 0, to = 100, command = position, orient = HORIZONTAL)
position.set(volume)
mixer.music.set_volume(volume)
position.grid(row = 1, column = 0, padx = 10, pady = 10)


parent.mainloop()
mixer.music.fadeout(2000)
mixer.quit()
