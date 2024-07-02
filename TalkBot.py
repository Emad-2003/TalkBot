# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:12:11 2020

@author: user
"""
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def Heading():
    print('''       
                  _____    __      _      _   __  ______   _____  _____
                 |_   _|  /  \    | |    | | / / |  __  \ /  _  \|_   _|
                   | |   / /\ \   | |    | |/ /  | |__| | | | | |  | |
                   | |  / /__\ \  | |    |   /   |  __  | | | | |  | | 
                   | | / ______ \ | |__  | |\ \  | |__| | | | | |  | |
                   |_|/_/      \_\|____| |_| \_\ |______/ \_____/  |_|
              ''')
            
def take_command():
    command=''
    try:
        with sr.Microphone() as source:
            print()
            print('listening ......')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            
            if 'talkbot' in command.lower():
                
                print('Question')
                c=command.lower()
                command=c.replace('alexa','')
                print(command)
                print()
            else:
                pass
    except:
        pass
    return command

def run_talkbot():
    
    command=take_command()
    if 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is'+time)
    
    elif 'joke' in command:
        j=pyjokes.get_joke()
        print('__JOKE__')
        print(j)
        talk(j)
        
    try:
        if 'who' in command:
            command=command.replace('who','')
            if 'is' in command:
                command=command.replace('is','')
            elif 'was' in command:
                command=command.replace('was','')
                
            info=wikipedia.summary(command,1)
            print(info)
            talk(info)
    except:
        talk("couldnt find regarding this topic")
    
    
    return command
    
def main_program():
    Heading()
    n=0
    while n>=0:
        if n==0:
            talk('hello I am Talkbot, what can I do for you ? ')   
        elif n>1:
            talk('what else can I do for you ? ')
        
        command=run_talkbot()
        n+=1
            
        if 'that\'s it for now' in command:
            talk('have a nice day')
            break

main_program()
