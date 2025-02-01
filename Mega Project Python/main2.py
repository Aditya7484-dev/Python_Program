# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicList as ml

# r = sr.Recognizer()
# engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def processCommand(c):
#     c = c.lower()
#     if "open google" in c:
#         webbrowser.open('https://www.google.com')
#         speak("Opening Google")
#     elif "open youtube" in c:
#         webbrowser.open('https://www.youtube.com/')
#         speak("Opening YouTube")
#     elif "open facebook" in c:
#         webbrowser.open('https://www.facebook.com/')
#         speak("Opening Facebook")
#     elif "open smashkarts" in c:
#         webbrowser.open('https://smashkarts.io/')
#         speak("Opening Smash Karts")
#     elif c.startswith("play"):
#         song = c.split(" ", 1)[1]  # Get everything after "play"
#         if song in ml.music:
#             link = ml.music[song]
#             webbrowser.open(link)
#             speak(f"Playing {song}")
#         else:
#             speak(f"Sorry, I couldn't find {song} in your music list.")
#     else:
#         speak("Sorry, I didn't understand the command.")

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     speak("Initializing Poco")
#     speak("Hi, this is Poco Assistant")

#     while True:
#         print("Say something")
        
#         try:
#             with sr.Microphone() as source:
#                 r.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
#                 print("Listening...")
#                 audio = r.listen(source, timeout=3, phrase_time_limit=3)

#             word = r.recognize_google(audio)
#             print(f"You said: {word}")

#             if "poco" in word.lower():
#                 print("Poco Activated")
#                 speak("I'm listening")

#                 with sr.Microphone() as source:
#                     r.adjust_for_ambient_noise(source, duration=1)
#                     audio = r.listen(source, timeout=5, phrase_time_limit=5)

#                 command = r.recognize_google(audio)
#                 print(f"Command received: {command}")
#                 processCommand(command)

#         except sr.UnknownValueError:
#             print("Could not understand the audio")
#         except sr.RequestError:
#             print("Speech Recognition service is down")
#         except Exception as e:
#             print(f"Error: {e}")
import speech_recognition as sr
import webbrowser
import pyttsx3 

ml = {
  "payal":"https://www.youtube.com/watch?v=a-PAcmi5Kas&pp=ygUFcGF5YWw%3D",
  
  "skyfall":"https://www.youtube.com/watch?v=sZrTJesvJeo&pp=ygUHc2t5ZmFsbA%3D%3D",
  
  "routine":"https://www.youtube.com/watch?v=Mw9U7FPaZho&pp=ygUYcm91dGluZSBzb25nIGFsYW4gd2Fsa2Vy",
  
  "rhinestone eyes":"https://www.youtube.com/watch?v=yYDmaexVHic&pp=ygUPcmhpbmVzdG9uZSBleWVz"
  }

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
  elif "open smashkarts" in c.lower():
    webbrowser.open('https://smashkarts.io/')
  elif c.lower().startswith("play"):
    song=c.lower().split(" ")[1]
    link=ml[song]
    webbrowser.open(link)
  

def speak(text):
  engine.say(text)
  engine.runAndWait()

if __name__=="main_":
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