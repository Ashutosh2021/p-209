import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import time
from playsound import playsound
import pygame
from pygame import mixer


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

song_counter=0
song_selected=None

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

    if(song_selected != ""):
        infolabel.configure(text="Now Playing :"+song_selected)
    else:
        infolabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infolabel.configure(text="")

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

def musicWindow():
    global listbox
    global infolabel

    window=Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    selectLabel=Label(window,text="Select Song",font=("Calibri",8),bg="LightSkyBlue")
    selectLabel.place(x=2,y=1)

    listbox=Listbox(window,height=10,width=39,activestyle='dotbox',bg="LightSkyBlue",borderwidth=2,font=("Calibri",10))
    listbox.place(x=10,y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",width=10,bd=1,bg="SkyBlue",font=("Calibri",10),command=play)
    playButton.place(x=30,y=200)

    stopButton=Button(window,text="Stop",width=10,bd=1,bg="SkyBlue",font=("Calibri",10),command=stop)
    stopButton.place(x=200,y=200)
    
    uploadButton=Button(window,text="Upload",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    uploadButton.place(x=30,y=250)
    
    downloadButton=Button(window,text="Download",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    downloadButton.place(x=200,y=250)

    infolabel=Label(window,text="Info Label",fg="blue",font=("Calibri",8))
    infolabel.place(x=4,y=280)

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1

    window.mainloop()

setup()

