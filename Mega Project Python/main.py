import speech_recognition as sr
import webbrowser
import pyttsx3
import musicList as ml

r=sr.Recognizer()
engine=pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open('https://www.google.com')
  elif "open youtube" in c.lower():
    webbrowser.open('https://www.youtube.com/')
  elif "open facebook" in c.lower():
    webbrowser.open('https://www.facebook.com/')
  elif "open smash karts" in c.lower():
    webbrowser.open('https://smash karts.io/')
  elif c.lower().startswith("play"):
    song=c.lower().split(" ")[1]
    link=ml.music[song]
    webbrowser.open(link)
  

def speak(text):
  engine.say(text)
  engine.runAndWait()

if __name__=="__main__":
  speak("Initializing jarvis")
  speak("Hi this is jarvis assisstant")
  
  while True:
    print("Say something")
    
    try: 
      
      with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)#Reduce noise
        print("Listening")
        audio=r.listen(source,timeout=2,phrase_time_limit=1)
        
      word=r.recognize_google(audio)
      
      if "jarvis" in word.lower():
        # print("Poco Activated")
        speak("I'm listening")
        
        with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source, duration=1)
          audio=r.listen(source)
          command= r.recognize_google(audio)
          processCommand(command)
          
    except sr.UnknownValueError:
      print("Could not understand the audio")
    except sr.RequestError:
      print("Speech Recognition service is down")
    except Exception as e:
      print(f"Error: {e}")