import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    elif hour >= 18 and hour < 0:
        speak("good evening")


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email ID', 'passcode')
    server.sendmail('reciever email', to, content)
    server.close

def takecommand():
    #It takes command from user as input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold == 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        #print(e)--prints error in console
        print("say that again please...")
        return "none"

    return query

if __name__ == "__main__":
    wishMe()
    speak("hi i'm thor,  your desktop assistant,  waiting for your command.")
    while True:
        query = takecommand().lower()


        # Logic for executing task based query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia...")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open watsapp web' in query:
            webbrowser.open("watsappweb.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\vamshi\\Music\\Songs' #set music path as per your desktop
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))   

        elif 'whats the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open visual studio code' in query:
            os.startfile("C:\\Users\\vamshi\\AppData\\Local\\Programs\\Microsoft VS Code\\code") #set path of your VS dir

        elif 'send email to surya' in query:
            try:
                speak("what should be written in mail.")
                content = takecommand()
                to = "vamshisuryaaa@gmail.com"
                sendemail(to, content)
                speak("email has been sent..")
            except Exception as e:
                print(e)
                speak("sorry jarvis was unable to send")
        
        elif 'quit' in query:
            speak('thanks for using jarvis, always ready to make your work easy...see you again')
            exit()