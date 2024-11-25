import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia

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
            elif "say time" in request:
                now_time= datetime.datetime.now().strftime("%H:%M")
                speak("Current time is "+str(now_time))
            elif "say date" in request:
                now_time= datetime.datetime.now().strftime("%d:%m")
                speak("Current date is "+str(now_time))
            elif "new task" in request:
                task = request.replace("new task","")
                task = task.strip()
                if task!="":
                    speak("Adding task : "+task)
                    with open("todo.txt","a") as file:
                        file.write(task+"\n")
            elif "speak task" in request:
                with open("todo.txt","r") as file:
                    speak("Your current tasks include "+file.read())
            elif "show work" in request:
                with open("todo.txt","r") as file:
                    tasks=file.read()
                notification.notify(
                    title = "Today's work",
                    message = tasks
                )
            elif "open" in request:
                query = request.replace("open")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
            
main_process()

# 25:41
