import pyaudio
import speech_recognition as s_r
from gtts import gTTS
from playsound import playsound
import os 
import time
import subprocess
import root_class
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import maintktscreen


flag = 0
global lu_text 
lu_text = " "
sp = maintktscreen.Toplevel1

def speak():
    playsound('Sounds/welcome.mp3',block=False)
        
    time.sleep(1.2)
        
    playsound('Sounds/welcome1.mp3',block=False)
    time.sleep(0.8)
    speak_infile()
    time.sleep(1.8)
                 
    playsound('Sounds/start.mp3',block=False)
    time.sleep(1.2)
        
                
            

def speak_infile():
    playsound('Sounds/finishline.mp3',block=False)
    return()

    
        

    
        
def exit_voice():
        
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        sys.exit()

def listen_user():

    lu = s_r.Recognizer()
    with s_r.Microphone() as source:

        print("Listening....")
        playsound('ding.mp3',block=False)
        lu.adjust_for_ambient_noise(source,duration=0.51)
        audio = lu.listen(source,timeout=3,phrase_time_limit=2.2)
        try:
            lu_text = lu.recognize_google(audio)
            print(lu_text)
            #flag = 1
            if lu_text == "open file" or lu_text == "openfile":
               # open_file()
               pass
                        
            elif lu_text == "exit" or lu_text == "EXIT":
                exit_voice()
                        
            elif lu_text == "save file as" or lu_text == "savefile as":
                #save_as()
                pass
            elif lu_text == "save":
               # save()
               pass
            elif lu_text == "write d" or lu_text == "w" or lu_text == "w":
                    lu = s_r.Recognizer()
                    with s_r.Microphone() as source:
                        print("Listening....")
                        playsound('ding.mp3',block=False)
                        lu.adjust_for_ambient_noise(source,duration=0.51)
                        audio = lu.listen(source,timeout=3,phrase_time_limit=2.2)
                        lu_text = lu.recognize_google(audio)
                        #sp.writedata(lu_text,lu_text)
                        # maintktscreen.Toplevel1.writedata(maintktscreen.Toplevel1)                            
            else:
                print('No call made')
                playsound('windows_error.mp3',block=False)

                    
        except s_r.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            time.sleep(0.8)
            playsound('windows_error.mp3',block=False)
            listen_user()
                    
        except s_r.RequestError as e:
                
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                time.sleep(1.8)
                playsound('windows_error.mp3',block=False)
                listen_user()
