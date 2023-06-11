import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Master!")
    else:
        speak("Good Evening Master!")
        
    speak("I am Ndroid. Your wish is my command")    

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('user said:', query)
    
        
    except Exception as e:
        #print(e)
        print("Sorry master can you repeat it")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ndkdnhshs@gmail.com', 'PennyHofstader100')
    server.sendemail('ndkdnhshs@gmail.com', to, content)
    server.clone()
    
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Getting info ready...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'access youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'access google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir = 'E:\\Divinity'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Master, The time is {strTime}")
            
        elif 'open code' in query:
            codepath ="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'send email' in query:
            try:
                speak("What's your text")
                content = takeCommand
                to = "niladrichaturvedi469@gmail.com"
                sendEmail(to ,content)
                speak("Your messeage has been delivered master")
            except Exception as e:
                print(e)
                speak("My Apologies Master but I can't send the text right now")