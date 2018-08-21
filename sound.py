#! /usr/bin/env python		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]

import builtins, keyword, os, sys, time
import queue, collections, threading, pickle, concurrent
import numbers, operator, math, cmath, decimal, fractions, random, itertools
import string, re, unicodedata, locale, uuid, hashlib, binascii, zlib
import doctest, unittest, cProfile, timeit, logging, traceback, datetime
import ftplib, poplib, nntplib, smtplib, telnetlib, email, functools
import argparse, calendar, pprint, struct, copy, pdb
import ipaddress, tkinter, dateutil, numpy, scipy, pygame, matplotlib

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

RESERVED = ["and", "del", "from", "not", "while", "as", "elif",
            "global", "or", "with", "assert", "else", "if", "pass",
            "yield", "break", "except", "import", "print", "class",
            "exec", "in", "raise", "continue", "finally", "is",
            "return", "def", "for", "lambda", "try"]

from pygame import mixer
from pygame.mixer import music
import winsound, maths, wave, fileman, ropes

# [w,s,v]=svd((repmat(sum(x.*x,1),size(x,1),1).*x)*x^1)

PIANO_KEYS = {'C8': 108, 'B7': 107, 'A♯7': 106, 'A7': 105,
              'G♯7': 104, 'G7': 103, 'F♯7': 102, 'F7': 101,
              'E7': 100, 'D♯7': 99, 'D7': 98, 'C♯7': 97,
              'C7': 96, 'B6': 95, 'A♯6': 94, 'A6': 93,
              'G♯6': 92, 'G6': 91, 'F♯6': 90, 'F6': 89,
              'E6': 88, 'D♯6': 87, 'D6': 86, 'C♯6': 85,
              'C6': 84, 'B5': 83, 'A♯5': 82, 'A5': 81,
              'G♯5': 80, 'G5': 79, 'F♯5': 78, 'F5': 77,
              'E5': 76, 'D♯5': 75, 'D5': 74, 'C♯5': 73,
              'C5': 72, 'B4': 71, 'A♯4': 70, 'A4': 69,
              'G♯4': 68, 'G4': 67, 'F♯4': 66, 'F4': 65,
              'E4': 64, 'D♯4': 63, 'D4': 62, 'C♯4': 61,
              'C4': 60, 'B3': 59, 'A♯3': 58, 'A3': 57,
              'G♯3': 56, 'G3': 55, 'F♯3': 54, 'F3': 53,
              'E3': 52, 'D♯3': 51, 'D3': 50, 'C♯3': 49,
              'C3': 48, 'B2': 47, 'A♯2': 46, 'A2': 45,
              'G♯2': 44, 'G2': 43, 'F♯2': 42, 'F2': 41,
              'E2': 40, 'D♯2': 39, 'D2': 38, 'C♯2': 37,
              'C2': 36, 'B1': 35, 'A♯1': 34, 'A1': 33,
              'G♯1': 32, 'G1': 31, 'F♯1': 30, 'F1': 29,
              'E1': 28, 'D♯1': 27, 'D1': 26, 'C♯1': 25,
              'C1': 24, 'B0': 23, 'A♯0': 22, 'A0': 21,
              ' ': -1}

MIDI_TONES = {0: 8.175798, 1: 8.661957, 2: 9.177023, 3: 10.300861,
              4: 10.300861, 5: 10.913382, 6: 11.562325, 7: 12.249857,
              8: 12.978271, 9: 13.75, 10: 14.567617, 11: 15.433853,
              12: 16.351597, 13: 17.3239144, 14: 18.354047, 15: 19.445436,
              16: 20.601722, 17: 21.8267644, 18: 23.124651, 19: 24.499714,
              20: 25.956543, 21: 27.5, 22: 29.135235, 23: 30.867706,
              24: 32.703195, 25: 34.6478288, 26: 36.708095, 27: 38.890872,
              28: 41.203444, 29: 43.6535289, 30: 46.249302, 31: 48.999429,
              32: 51.913087, 33: 55, 34: 58.270470, 35: 61.735412,
              36: 65.406391, 37: 69.2956577, 38: 73.416191, 39: 77.781745,
              40: 82.406889, 41: 87.3070578, 42: 92.498605, 43: 97.998858,
              44: 103.826174, 45: 110, 46: 116.540940, 47: 123.470825,
              48: 130.812782, 49: 138.591315, 50: 146.832383, 51: 155.563491,
              52: 164.813778, 53: 174.614115, 54: 184.997211, 55: 195.997717,
              56: 207.652348, 57: 220, 58: 233.081880, 59: 246.941650,
              60: 261.625565, 61: 277.182630, 62: 293.664767, 63: 311.126983,
              64: 329.627556, 65: 349.228231, 66: 369.994422, 67: 391.995435,
              68: 415.304697, 69: 440, 70: 466.163761, 71: 493.883301,
              72: 523.251130, 73: 554.365261, 74: 587.329535, 75: 622.253967,
              76: 659.255113, 77: 698.456462, 78: 739.988845, 79: 783.990871,
              80: 830.609395, 81: 880, 82: 932.327523, 83: 987.766602,
              84: 1046.502261, 85: 1108.730523, 86: 1174.659071, 87: 1244.507934,
              88: 1318.510227, 89: 1396.912925, 90: 1479.977690, 91: 1567.981743,
              92: 1661.218790, 93: 1760, 94: 1864.655046, 95: 1975.533205,
              96: 2093.004522, 97: 2217.461047, 98: 2349.318143, 99: 2489.015869,
              100: 2637.020455, 101: 2793.825851, 102: 2959.955381, 103: 3135.963487,
              104: 3322.437580, 105: 3520, 106: 3729.310092, 107: 3951.066410,
              108: 4186.009044, 109: 4434.922095, 110: 4698.636286, 111: 4978.031739,
              112: 5274.040910, 113: 5587.651702, 114: 5919.910763, 115: 5919.910763,
              116: 6644.875161, 117: 7040, 118: 7458.620184, 119: 7902.132820,
              120: 8372.018089, 121: 8869.844191, 122: 9397.272573, 123: 9956.063479,
              124: 10548.081821, 125: 11175.303405, 126: 11839.821526, 127: 12543.853951,
              -1: 0}

PIANO_TONES = {key: MIDI_TONES[PIANO_KEYS[key]] for key in PIANO_KEYS}
# PIANO_TONES = [(key, MIDI_TONES[PIANO_KEYS[key] ]) for key in PIANO_KEYS]

SONG_NOTES = {'ttls': (('E4', 'E4', 'B5', 'B5', 'C♯5', 'C♯5', 'B5'),
                       ('A5', 'A5', 'G♯4', 'G♯4', 'F♯4', 'F♯4', 'E4'),
                       ('B5', 'B5', 'A5', 'A5', 'G♯4', 'G♯4', 'F♯4'),
                       ('B5', 'B5', 'A5', 'A5', 'G♯4', 'G♯4', 'F♯4'),
                       ('E4', 'E4', 'B5', 'B5', 'C♯5', 'C♯5', 'B5'),
                       ('A5', 'A5', 'G♯4', 'G♯4', 'F♯4', 'F♯4', 'E4')),
              'omhaf': (('C4', 'C4', 'C4', 'G3', 'A3', 'A3', 'G3'),
                        ('E4', 'E4', 'D4', 'D4', 'C4'),
                        ('G3', 'C4', 'C4', 'C4', 'G3', 'A3', 'A3', 'G3'),
                        ('E4', 'E4', 'D4', 'D4', 'C4')),
              'rrryb': (('D4', 'D4', 'D4', 'E4', 'F♯4'),
                        ('F♯4', 'E4', 'F♯4', 'G4', 'A5'),
                        ('D5', 'D5', 'D5', 'A5', 'A5', 'A5', 'F♯4', 'F♯4', 'F♯4', 'D4', 'D4', 'D4'),
                        ('A5', 'G4', 'F♯4', 'E4', 'D4')),
              'tom': (('G4', 'E4', 'G4', 'G4', 'E4', 'G4'),
                      ('A4', 'G4', 'F4', 'E4', 'D4', 'E4', 'F4'),
                      ('E4', 'F4', 'G4', 'C4', 'C4', 'C4', 'C4', 'C4', 'D4', 'E4', 'F4', 'G4'),
                      ('G4', 'D4', 'D4', 'F4', 'E4', 'D4', 'C4')),
              'hbty': (('A4', 'A4', 'B4', 'A4', 'D4', 'C♯4'),
                       ('A4', 'A4', 'B4', 'A4', 'E4', 'D4'),
                       ('A4', 'A4', 'A5', 'F♯4', 'D4', 'C♯4', 'B4'),
                       ('G4', 'G4', 'F♯4', 'D4', 'E4', 'D4'))}

INSTRUMENTS = ['recorder', 'flute', 'organ', 'horn', 'tin', 'trombone',
               'trumpet,', 'tom-tom', 'tube', 'pan', 'slide',
               'accordion', 'snare', 'clarinet', 'pitch', 'reed', 'whip',
               'bass', 'drum', 'whistle', 'sirens', 'harmonica', 'tuba',
               'tenor', 'pipe', 'bagpipe', 'siren', 'goblet', 'ocarina']

INSTRUMENTS = ['Acoustic', 'Woodwind', 'Percussion', 'Trumpets',
               'Brass', 'Vocal', 'Reed', 'Flutes', 'Stringed']

CLASSIFICATIONS = ['chordophones', 'aerophones', 'membranophones']

DEFAULT_SAMPLE_RATE = 22050  # 22 kHz sample rate
# peaks = 0 # number of peaks counted

"""
freq - the frequency of the wave
length - the length to play the wave for in milliseconds
sampleRate - the sample rate
"""


def SineWave(freq, length, sampleRate=DEFAULT_SAMPLE_RATE):
    """
    returns a string representing an 8 bit mono sine wave
    """
    wavelength = 2 * math.pi * freq / sampleRate  # a constant to multiply i to get the sine
    return ''.join([chr(0x80 + int(0x7F * math.sin(i * wavelength))) \
                    for i in range(0, sampleRate * length // 1000)])


def SquareWave(freq, length, sampleRate=DEFAULT_SAMPLE_RATE):
    """
    returns a string representing an 8 bit mono square wave
    """
    wavelength = freq / sampleRate  # the wavelength
    return ''.join([(i * wavelength % 1 < .5 and '\xFF' or '\x00') \
                    for i in range(0, sampleRate * length // 1000)])


def TriangleWave(freq, length, sampleRate=DEFAULT_SAMPLE_RATE):
    """
    returns a string representing an 8 bit mono triangle wave
    """
    wavelength = freq / sampleRate  # the wavelength
    return ''.join([chr(0x80 + int(0x7F * maths.triangle_sine(i * wavelength))) \
                    for i in range(0, sampleRate * length // 1000)])


def SawToothWave(freq, length, sampleRate=DEFAULT_SAMPLE_RATE):
    """
    returns a string representing an 8 bit mono sawtooth wave
    """
    wavelength = freq / sampleRate  # the wavelength
    return ''.join([chr(int(0xFF * (i * wavelength % 1))) \
                    for i in range(0, sampleRate * length // 1000)])


WAVES = {'square': SquareWave, 'triangle': TriangleWave,
         'sine': SineWave, 'sawtooth': SawToothWave}


def waveGen(freq, length, waveType, sampleRate=DEFAULT_SAMPLE_RATE):
    """
    waveGen
    freq - the frequency of the wave
    length - the length to play the wave for in milliseconds
    waveType - what kind of wave to make. This is a string.
    sampleRate - the sample rate
    returns a string representing an 8 bit mono wave
    """
    if waveType in WAVES:
        return WAVES[waveType](freq, length, sampleRate)
    else:
        return squareWave(freq, length, sampleRate)


def chord(root_frequency):
    winsound.Beep(int(root_frequency), 60)
    winsound.Beep(int(root_frequency * 1.25), 60)
    winsound.Beep(int(root_frequency * 1.5), 60)
    winsound.Beep(int(root_frequency * 2), 100)


def octave(note, shift):
    """Shift the octave of a note"""
    if note == ' ':
        return note
    note = ropes.capitalise(note)
    if note == 'C8':
        return note
    note = ropes.find_replace(note, '#', '♯')
    if not note in PIANO_KEYS:
        return ' '
    if (int(note[-1]) + shift) in range(0, 8):
        return note[0:-1] + str(int(note[-1]) + shift)
    else:
        return note


def play_song(score, shift=0):
    for line in score:
        for note in line:
            print(octave(note, shift), MIDI_TONES[PIANO_KEYS[octave(note, shift)]])
            # chord(MIDI_TONES[PIANO_KEYS[octave(note, shift) ] ] )
            winsound.Beep(round(MIDI_TONES[PIANO_KEYS[octave(note, shift)]]), 333)


for score in SONG_NOTES:
    print(score)
    play_song(SONG_NOTES[score], 1)

"""
duration
gain

pitch
tone

HumanSensitivity 20-20000
HumanVocal 40-4000
"""

if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)




##while True:
##    chord(261.626)
##    time.sleep(0.35)
##    chord(261.626)
##    time.sleep(0.05)
##    chord(233.082)
##    time.sleep(0.35)
##    chord(233.082)
##    time.sleep(0.05)
##    chord(207.652)
##    time.sleep(0.35)
##    chord(207.652)
##    time.sleep(0.05)
##    chord(195.998)
##    time.sleep(0.35)
##    chord(195.998)
##    time.sleep(0.05)


# for key in PIANO_KEYS:
# if MIDI_TONES[PIANO_KEYS[key]] > 36:
#    winsound.Beep(round(MIDI_TONES[PIANO_KEYS[key]]), 100)
# print(round(MIDI_TONES[PIANO_KEYS[key]]), 10)

nchannels = 1
sampwidth = 1
framerate = 22500
nframes = 100

# for wave in WAVES:
#    print(waveGen(PIANO_TONES['C4'], 100, wave, DEFAULT_SAMPLE_RATE))

##w1 = wave.open('test1.wav', 'w')
##w1.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))
##w2 = wave.open('test2.wav', 'w')
##w2.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))
##w3 = wave.open('test3.wav', 'w')
##w3.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))

mixer.init(frequency=16000)  # set frequency for wav file
s1 = mixer.Sound('test1.wav')
s2 = mixer.Sound('test2.wav')

# individual
s1.play(-1)  # loops indefinitely
time.sleep(0.5)

# simultaneously
s2.play()  # play once
time.sleep(2)
s2.play(2)  # optional parameter loops three times
time.sleep(10)

# set volume down
s1.set_volume(0.1)
time.sleep(5)

# set volume up
s1.set_volume(1)
time.sleep(5)

s1.stop()
s2.stop()
mixer.quit()

mixer.init()
music.load('test.mp3')

music.play()
time.sleep(10)

music.stop()
mixer.quit()

"""

def schr(n):
#    schr
#        n - a number
#        returns a character, prints a warning if the wave peaks
    if (n > 0xFF):
    #    peaks += 1
        return '\xFF'
    elif (n < 0x00):
    #    peaks += 1
        return '\x00'
    return chr(n)

def mergeWaves(wave1,wave2):
#    mergeWaves - merge two waves together
#        wave1 - a wave string
#        wave2 - a wave string
#        returns a new wave string that is both combined
    li=[schr(ord(a)+ord(b)-0x80) for (a,b) in izip_longest(wave1,wave2,fillvalue='\x80')]
    #if peaks:
    #    print 'Peaking for %f seconds on merge!'%(peaks/sampleRate)
    #    peaks = 0
    return ''.join(li)

def divide(wave, n):
#    divide
#        wave - a wave string
#        n    - a number to divide by
#        returns a new wave string
    return ''.join([chr((ord(c)-0x80)//n+0x80) for c in wave])

def littleEndian(n, bytes):
#    littleEndian
#        n - the number to convert
#        bytes - the number of bytes long this should ultimately be
#        returns a string representing n in Little Endian format
    li=[]
    for i in range(0, bytes):
        li.append(chr(n % 0x100))
        n = n // 0x100
    return ''.join(li)



def makeWavFile(wave,filename,sampleRate=DEFAULT_SAMPLE_RATE):
     #makeWave
        #wave - the wave to put into the file
        #filename - the name of the file to open
        #returns None, creates an 8 bit mono .wav file
    try:
        # The following information is heavily based on Wikipedia and
        # http://technology.niagarac.on.ca/courses/ctec1631/WavFileFormat.html
        # https://ccrma.stanford.edu/courses/422/projects/WaveFormat/
        # http://www.sonicspot.com/guide/wavefiles.html
        f = open(filename, 'wb')
        try:
            length=len(wave)
            # RIFF chunk
            f.write('RIFF%sWAVE'%littleEndian(length + 36, 4))
            # FORMAT chunk
            #            (FORMAT  Length)( PCM  )( MONO )    (8bMONO)(8  BIT)
            f.write('fmt \x10\x00\x00\x00\x01\x00\x01\x00%s%s\x01\x00\x08\x00'%(littleEndian(sampleRate, 4),littleEndian(sampleRate, 4)))
            # DATA chunk
            f.write('data%s'%littleEndian(length, 4))
            f.write(wave)
        except IOError:
            print "There was an error writing the file"
        finally:
            f.close()
    except IOError:
        print "Could not open %s for writing"%filename

"""
