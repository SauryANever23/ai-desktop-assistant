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


 
def main():
    running = True
    while running:
        say("Jarvis Found")
        print("Listening")
        command = takeCommand()
        cmd_lst = command.split()
        
        reg_input = input("")

        if reg_input = "q":
            running = False

        if cmd_lst[0].lower == "active":
            pass
    
        if len(cmd_lst) == 2:
            openWebsites(command)


if __name__ == '__main__':
    main()
    


    
