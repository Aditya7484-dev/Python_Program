import speech_recognition as sr
import webbrowser
import pyttsx3
import musicList as ml
import requests
from gtts import gTTS
import pygame
import os

r=sr.Recognizer()
engine=pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newsApi="Q6e3d66e888647ea8e9729bbecac57ee"

def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open('https://www.google.com')
  elif "open youtube" in c.lower():
    webbrowser.open('https://www.youtube.com/')
  elif "open facebook" in c.lower():
    webbrowser.open('https://www.facebook.com/')
  elif "open linkedin" in c.lower():
    webbrowser.open('https://www.linkedin.com/feed/')
  elif c.lower().startswith("play"):
    song=c.lower().split(" ")[1]
    link=ml.music[song]
    webbrowser.open(link)
  elif "news" in c.lower():
    r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}")
    if r.status_code==200:
      data=r.json()
      articles=data.get('articles',[])
      for article in articles:
        speak(article['title'])

def speak_old(text):
  engine.say(text)
  engine.runAndWait()

def speak(text):
  tts=gTTS(text)
  tts.save('temp.mp3')
  
  # initialize pygame mixer
  pygame.mixer.init()
  
  # Load the mp3 file 
  pygame.mixer.music.load('temp.mp3')
  
  # Play the music
  pygame.mixer.music.play()
  
  while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
  
  pygame.mixer.music.unload()
  os.remove('temp.mp3')  

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