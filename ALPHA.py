import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import random
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<23:
        speak("Good Evening!")

    else:
        speak("Its late sir, You should get some rest but still")
        
    speak("my name is Alpha. Please tell me how can I help you sir")

def takeCommand():
    #its takes mic input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        speak("Sorry, I could not get that")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mavericksamarth@gmail.com', 'Shinchan9450')
    server.sendmail('mavericksamarth@gmail.com', to, content)
    server.close()
    
def alphabetss():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    speak("Repeat after me")
    speak("A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z")
    speak("once again one by one")
    for i in alphabets:
        speak(i)
        aaaa = takeCommand().lower()
        while(aaaa!=i):
            speak("Try Again")
            aaaa = takeCommand().lower()
            speak("very good")
            if 'stop' in aaaa:
                break

def ludo():
    speak("Ludo mode activated, say 'roll' to roll the dice over, and 'exit' to stop ludo mode")
    dice = takeCommand().lower()
    while 'exit' not in dice:
        if 'throw' or 'roll' in dice:
            speak("trrr")
            rr = random.randrange(1,7,1)
            speak(rr)
        else:
            continue
    speak("exit")
    
            

if __name__ == "__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'ludo mod' in query:
            ludo()

        #elif 'alphabets' or 'alphabet' in query:
            #alphabetss()  

        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'code' in query:
            speak("Do you want to code online or offline, sir?")
            newquery = takeCommand().lower()
            
            if 'online' in newquery:
                speak("Where do you want to code sir, Hackerrank or code chef")
                newquery1 = takeCommand().lower()
                if 'hackerrank' in newquery1:
                    webbrowser.open("hackerrank.com")
                elif 'codechef' in newquery1:
                    webbrowser.open("codechef.com")
            
            elif 'offline' in newquery:
                speak("Visual Studio, Android Studio, Unity, or Sublime")
                newquery2 = takeCommand().lower()
                if 'android' in newquery2:
                    andpath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
                    os.startfile(andpath)
                elif 'visual' in newquery2:
                    vispath = "C:\\Users\\Maverick\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(vispath)
                elif 'sublime' in newquery2:
                    subpath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                    os.startfile(subpath)
                elif 'unity' in newquery2:
                    unipath = "C:\\Program Files\\Unity\\Hub\\Editor\\2019.3.9f1\\Editor\\Unity.exe"
                    os.startfile(unipath)
                speak("Here you go sir")

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            l = len(songs)
            n = random.randrange(0,l,1)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime} sir")

        elif 'you' in query:
            speak("My name is Alpha, speed 2 giga hertz, built by Samarth Ranjan at Ranjan Vision Labs. My full name is Artificially Intel Personal Home Assistant.")
        
        elif 'who am i' in query:
            speak("You are my creator sir. You have build me and I am here to help you as your virtual assistant")

        elif 'creator' in query:
            speak("Master Samarth Ranjan is my creator.")

        elif 'purpose' in query:
            speak('I have been developed to serve my assigned master as a virtual assistant. My name is Alpha')

        elif 'suno' in query:
            speak("haaan sir bo lee a")
        
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                speak("Whom should i send this to?")
                mailname = takeCommand().lower().replace(" ", "")
                to = mailname+"@gmail.com"
                print(to)
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                speak("Sorry I could not get it, would you please repeat sir")
                

        elif 'stop listening' or 'stop' in query:
            c = random.randrange(0,2,1)
            if c==0:
                speak("I will wait for your command")
            elif c==1:
                speak("Ok sir")
            break


