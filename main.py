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


def scan_services():
 
   say("connecting to bluetooth...")
 
   devices = bluetooth.discover_devices(lookup_names = True)
 
   number_of_devices = len(devices)
 
   print(number_of_devices, "devices found")
 
   for addr,name in devices:
 
      print("\n")
 
      print("Device Name: %s" % (name))
 
      print("Device MAC Address: %s" % (addr))
 
      print("Services Found:")
 
      services = bluetooth.find_service(address=addr)
 
      if len(services) <=0:
 
          print("zero services found on", addr)
 
      else:
 
          for serv in services:
 
              print(serv['name'])
 
      print("\n")

    return ()
 
 
main():
    say("Jarvis Found")

if __name__ == '__main__':
    print("listening...")
    t = takeCommand()


    
