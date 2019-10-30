import os

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox

from pygame import mixer
#from pillow import Image


filename = r'G:\WorkingData\Work @ Home\Humanity\My Icon.png'
#img = Image.open(filename)
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]
#img.save('logo.ico', sizes = icon_sizes)

parent = Tk()
parent.geometry() #'800x600'
parent.title("Python GUI")
parent.iconbitmap(r'G:\WorkingData\Work @ Home\Humanity\My Icon.png')

text = Label(parent, text = 'text')
text.pack(pady = 10)

imagefile = PhotoImage(file = 'G:\WorkingData\Work @ Home\Humanity\My Icon.png')
labelimage = Label(parent, image = imagefile)
labelimage.pack(padx = 5, pady = 5)

audiofile = "G:\WorkingData\My Music\Portable\Soul Divas\VideoGames.mp3"


menubar = Menu(parent)
parent.config(menu = menubar)

statusbar = Label(parent, text = "Status bar", relief = SUNKEN, anchor = W)
statusbar.pack(side = BOTTOM, fill = X)

submenu = Menu(menubar, tearoff = 0)

menubar.add_cascade(label = "File", menu = submenu)

def open_file():
    filename = filedialog.askopenfilename()
    
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
mixer.music.set_volume(100)
mixer.music.load("G:\WorkingData\My Music\Portable\Soul Divas\VideoGames.mp3")

global playing
playing = False
global paused
paused = True
global muted
muted = False
global volume
volume = 100


controls = Frame(parent, relief = SUNKEN, borderwidth = 3)
controls.pack(padx = 5, pady = 5)

def rewind():
    mixer.music.rewind()

rewind = Button(controls, text = "Rewind", command = rewind, relief = RAISED, borderwidth = 3)
rewind.pack(side = LEFT, padx = 5, pady = 5)


def play():
    global playing
    global paused
    try:
        mixer.music.play(-1)
        playing = True
        paused = False
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
        statusbar['text'] = f"Playing {os.path.basename(audiofile)}"
        paused = False
    elif playing == True and paused == False:
        mixer.music.pause()
        pause.config(text = "Unpause")
        statusbar['text'] = f"Paused {os.path.basename(audiofile)}"
        paused = True

pause = Button(controls, text = "Pause", command = pause, relief = RAISED, borderwidth = 5)
pause.pack(side = LEFT, padx = 5, pady = 5)


def stop():
    global playing
    mixer.music.stop()
    statusbar['text'] = f"Audio stopped"
    playing = False

stop = Button(controls, text = "Stop", command = stop, relief = RAISED, borderwidth = 4)
stop.pack(side = LEFT, padx = 5, pady = 5)


def forward():
    pass

forward = Button(controls, text = "Forward", command = forward, relief = RAISED, borderwidth = 3)
forward.pack(side = LEFT, padx = 5, pady = 5)


output = Frame(parent, relief = SUNKEN, borderwidth = 3)
output.pack(anchor = E, padx = 5, pady = 5)


def mute():
    global playing
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
    mixer.music.set_volume(int(val) / 100)

position = Scale(output, from_ = 0, to = 100, command = position, orient = HORIZONTAL)
position.set(volume)
mixer.music.set_volume(volume)
position.pack(anchor = E, padx = 10, pady = 10)


parent.mainloop()
mixer.music.fadeout(2000)
mixer.quit()
