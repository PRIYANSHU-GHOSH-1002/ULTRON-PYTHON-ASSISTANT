import speech_recognition as sr                            # all the imports 
import webbrowser
import pyttsx3
import music_lib 
 

recognizer = sr.Recognizer()                               # setting up the speech recognition
engine = pyttsx3.init()

def speak(text):                                           # setting up the reply speaking
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):                                     # function which performs all the commands
    c = c.lower()
    
    if "open insta" in c or "open instagram" in c:  
        speak("aye aye sir")
        webbrowser.open("https://instagram.com")    
    elif "open youtube" in c or "open y t" in c:
        speak("aye aye sir") 
        webbrowser.open("https://youtube.com")    
    elif "open google" in c:
        speak("aye aye sir")
        webbrowser.open("https://www.google.com")
    elif c.startswith("play"):
       song = c.split(" ")[1]
       link=music_lib.music[song]
       speak("aye aye sir")
       webbrowser.open(link)   
    else:
        speak("negative sir")


if __name__ == "__main__":
    speak("system activated")

    while True:
        # Listen for the wake word "ULTRON"
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Sphinx
        
        try:
           with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
           word = r.recognize_google(audio)
           print(word)

           if (word.lower()=="ultron"):
              speak("INITIALIZING ULTRON")

              with sr.Microphone() as source:
                print("ULTRON ACTIVE...")
                audio = r.listen(source,timeout=10)
                command = r.recognize_google(audio)
                     
                processcommand(command)

        except Exception as e:
            print("error")



























