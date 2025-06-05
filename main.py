import speech_recognition as sr 
import openai
import wikipedia as wk 
import os
import webbrowser
import datetime 
import sys
import re

def say(text):
    os.system(f'say "{text}"')
    
def takeCommand():
    try:
        r = sr.Recognizer()
    
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
        
            query = r.recognize_google(audio, language="en")
            return query
    except Exception as e:
        print(f"error: {e}")

def openWebsites(cmd):
    
    words = cmd.split()
    nwords = []
     
    indx = words.index("open")
    nwords.append(words[indx+1])

    for word in words:
        if "open" in word.lower():
            try:
                site = f"https://www.{words[1]}.com"
            except:
                site = f"https://www.{words[1]}.org"



    say(f"Opening {words[1]} sir..")
    webbrowser.open(site)

def sayTime():
    strf = datetime.datetime.now().strftime("%H:%M")
    say(f"The time is {strf}")

def openApp(cmd):
    lcase = cmd.lower()
    commands = lcase.split()
    app_indx = commands.index("app")
    
    file = "file"
    app = commands[app_indx+1]

    match = re.search(file, app)
    if match:
        say("opening files SIR!")
        os.system(f"open /home/saurya-jha")

def tokenizer_prototype(cmd) -> list:
    new = cmd.lower()
    new_list = new.split()
       
    for i in range(len(new_list)):
        if new_list[i] == "." or new_list[i] == "?" or new_list[i] == "/":
            new_list.pop(new_list[i])


def main():
    running = True
    while running:
        say("Listening..")
        print("Listening")
        command = takeCommand()
        if str(type(command)) != "<class 'NoneType'>":
            cmd_lst = command.split()
        
            if cmd_lst[0].lower == "active":
                pass
            
            if "the time" in command:
                sayTime()

            if "open" in command:
                try:
                    if len(cmd_lst) == 2:
                        openWebsites(command)
                except:
                    say("Sorry, some error occoured")

            if "app" in command:
                openApp(command)


            if "close" in command:
                say("Closing")
                sys.exit()

            else:
                pass

if __name__ == '__main__':
    main()
    


    
