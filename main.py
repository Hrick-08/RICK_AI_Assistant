import pyttsx3
import speech_recognition as sr
import random
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)   
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def command():
    # obtain audio from the microphone
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)


        # recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio, language="en-in")
            print("You said............." + content)

        except Exception as e:
            print("Please try again...")

    return content

def main_process():
    while True:
        request = command().lower()
        print(request)
        if "hello" in request:
            speak("Welcome. How can I assist you?")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://open.spotify.com/track/0Fk2JzsQIhZvfm5AC0FRKG?si=da71da1110014d59")
            elif song==2:
                webbrowser.open("https://open.spotify.com/track/1Qrg8KqiBpW07V7PNxwwwL?si=170e0b6689b14fff")
            elif song==3:
                webbrowser.open("https://open.spotify.com/track/5ZF6l3xKi3m6YK2dDXAsR5?si=ad2224c3a8f84761")
main_process()