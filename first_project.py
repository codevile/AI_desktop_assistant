# my first project in python
from math import e
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib 
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#let us create a speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    
    elif hour>=12 and hour<18:
        speak("Good After Noon Sir")
    
    elif hour == 18:
       speak("Good Evening Sir")

    else :
        speak("Good Night Sir")

    speak("I am Jarvis, How can i help you")

def takeargs():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('dhdyuivfyy@gmail.com', 876932)
    server.ehlo()
    server.starttls()
    server.login('youremailaddress@gmail.com','your password' )
    server.sendmail('youremailaddress@gmail.com',to,content)
    server.close


# now let's create our main function

if __name__== "__main__":
    
    wishme()
    
    while True:
        
        query = takeargs().lower()


        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube ' in query:
            webbrowser.open("m.youtube.com")

        
        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'play music ' in query:
            music_dic =  'C:\\Users\\Public\\Music\\Sample Music'
            songs = os.listdir(music_dic)
            print(songs)
            os.startfile(os.path.join(music_dic, songs[1]))

        elif "kapil sharma show" in query:
            webbrowser.open('https://youtu.be/BS_E7DdkANE')

        elif 'mail to user' in query:
            try:
                speak("what should i say")
                content = takeargs()
                to = "emailyouwant@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry man  i am not able to send email")





 
    
