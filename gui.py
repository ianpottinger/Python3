import os
import win32com.client as wincl

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox

from pygame import mixer
#from pillow import Image

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
#img = Image.open(filename)
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]
#img.save('logo.ico', sizes = icon_sizes)

parent = Tk()
parent.geometry() #'800x600'
parent.title("Python GUI")
parent.iconbitmap(r'G:\WorkingData\Work @ Home\Humanity\My Icon.png')


leftframe = Frame(parent)
leftframe.pack(anchor = W, padx = 5, pady = 5)

centreframe = Frame(parent)
centreframe.pack(padx = 5, pady = 5)

rightframe = Frame(parent)
rightframe.pack(anchor = E, padx = 5, pady = 5)


imagefile = PhotoImage(file = 'G:\WorkingData\Work @ Home\Humanity\My Icon.png')
labelimage = Label(centreframe, image = imagefile)
labelimage.pack(padx = 5, pady = 5)


label = Label(centreframe, text = audiofile)
label.pack(pady = 10)


menubar = Menu(parent)
parent.config(menu = menubar)

statusbar = Label(parent, text = "Status bar", relief = SUNKEN, anchor = W)
statusbar.pack(side = BOTTOM, fill = X)


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


controls = Frame(centreframe, relief = SUNKEN, borderwidth = 3)
controls.pack(padx = 5, pady = 5)

def rewind():
    speak.Speak("Come again selectA")
    mixer.music.rewind()

rewind = Button(controls, text = "Rewind", command = rewind, relief = RAISED, borderwidth = 3)
rewind.pack(side = LEFT, padx = 5, pady = 5)


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
play.pack(side = LEFT, padx = 5, pady = 5)


def pause():
    global playing
    global paused
    if playing == True and paused == True:
        mixer.music.unpause()
        pause.config(text = "Pause")
        speak.Speak("Unpaused")
        statusbar['text'] = f"Playing {os.path.basename(audiofile)}"
        paused = False
    elif playing == True and paused == False:
        mixer.music.pause()
        pause.config(text = "Unpause")
        speak.Speak("Pullllllllllllll uppppp")
        statusbar['text'] = f"Paused {os.path.basename(audiofile)}"
        paused = True

pause = Button(controls, text = "Pause", command = pause, relief = RAISED, borderwidth = 5)
pause.pack(side = LEFT, padx = 5, pady = 5)


def stop():
    global playing
    mixer.music.stop()
    speak.Speak("Stop")
    statusbar['text'] = f"Audio stopped"
    playing = False

stop = Button(controls, text = "Stop", command = stop, relief = RAISED, borderwidth = 4)
stop.pack(side = LEFT, padx = 5, pady = 5)


def forward():
    speak.Speak("Skip")
    pass

forward = Button(controls, text = "Forward", command = forward, relief = RAISED, borderwidth = 3)
forward.pack(side = LEFT, padx = 5, pady = 5)


output = Frame(centreframe, relief = SUNKEN, borderwidth = 3)
output.pack(anchor = E, padx = 5, pady = 5)


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
mute.pack(side = LEFT, padx = 5, pady = 5)


def position(val):
    global volume
    mixer.music.set_volume(int(val) / 100)

position = Scale(output, from_ = 0, to = 100, command = position, orient = HORIZONTAL)
position.set(volume)
mixer.music.set_volume(volume)
position.pack(anchor = E, padx = 10, pady = 10)


playlist = Listbox(rightframe)
playlist.insert(0, audiofile)
playlist.insert(1, filename)
playlist.pack()



parent.mainloop()
mixer.music.fadeout(2000)
mixer.quit()