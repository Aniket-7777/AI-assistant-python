import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')


# Initialize Pygame and the mixer
    pygame.init()
    pygame.mixer.init()

    # Load your MP3 file
    pygame.mixer.music.load('temp.mp3')  # Replace 'your_file.mp3' with the path to your MP3

    # Play the music (loop indefinitely)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play "):   # ✅ fixed here
        song = c.lower().split(" ")[1]
        try:
            link = musiclib.music[song]
            webbrowser.open(link)
        except KeyError:
            speak(f"Sorry, I don't know the song {song}. Please add it in musiclib.")
    else:
        speak("I didn't understand that command.")


if __name__ =="__main__":
    speak("Initiallizing Jarvis........ ")
    while True:
        #listen for the wake word "jarvis"
        # "obtain audio from the microphone:"
        r = sr.Recognizer()

        print("recognizing...")
        # recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word =  r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("hello myself jarvis.")
                #listening for   command
                with sr.Microphone() as source:
                    print("Jarvis Active...!")
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                    command =  r.recognize_google(audio)
                    print(command)
                    
                    processCommand(command)


        except Exception as e:
            print(" error; {0}".format(e))  

