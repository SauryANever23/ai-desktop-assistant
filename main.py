import speech_recognition as sr 
import openai
import wikipedia as wk 
import os
import webbrowser


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
    
    for word in words:
        if "open" in word.lower():
            try:
                site = f"https://www.{words[1]}.com"
            except:
                site = f"https://www.{words[1]}.org"



    say(f"Opening {words[1]} sir..")
    webbrowser.open(site)


if __name__ == '__main__':
    print("listening...")
    t = takeCommand()
    openWebsites(t)

    
