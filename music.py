import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import Tk, StringVar, Label, Listbox, Button
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("which type of song you want to listen")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None" 
    return query 

''' from here the music start'''
root = Tk()

listofsongs = []
realnames = []
folder = {"emotional":"C:\\Users\\admin\\Music\\Music",
          "romantic":"",
          "rap":"",
          "hindi":"",
          "english":"",
          "marathi":"",
          "rocking":"",
         }
v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

def directorychooser():
    wishMe()
    type = takeCommand()
    directory = folder[type]
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    v.set(realnames[index])
    #return songname

label = Label(text='Music Player')
# label.pack()
listbox = Listbox()
# listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()


print("Enjoy your music sir.")
speak("enjoy your music sir")
speak(f"playing {realnames[index]}")
pygame.mixer.music.play()
updatelabel()

''' music file ends '''

if __name__ == "__main__":
    wishMe()
while True:
# if 1:
    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'play' in query:
        speak(f"playing {realnames[index]}")
        pygame.mixer.music.play()
        updatelabel()

    if 'what is the song name' in query:
        speak(f"playing {realnames[index]}")

    if 'stop' in query:
        pygame.mixer.music.stop()
    
    if 'previous' in query:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        speak(f"playing {realnames[index]}")
        pygame.mixer.music.play()
        updatelabel()
    
    if 'next' in query:
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        speak(f"playing {realnames[index]}")
        pygame.mixer.music.play()
        updatelabel()
        
    if 'pause' in query:
        pygame.mixer.music.pause()
        updatelabel()
        
    if 'resume' in query:
        pygame.mixer.music.unpause()
        updatelabel()

    if 'set volume to 50' in query:
        pygame.mixer.music.set_volume(0.5)
        updatelabel()

    if 'set volume to 70' in query:
        pygame.mixer.music.set_volume(0.7)
        updatelabel()

    if 'set volume to 80' in query:
        pygame.mixer.music.set_volume(0.8)
        updatelabel()

    if 'set volume to 90' in query:
        pygame.mixer.music.set_volume(0.9)
        updatelabel()

    if 'raise volume' in query:
        pygame.mixer.music.set_volume(1)
        updatelabel()
       
    elif 'exit' in query:
        speak("hope you enjoyed sir")
        exit()