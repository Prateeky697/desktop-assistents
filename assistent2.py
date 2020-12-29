import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import speech_recognition
 
engine=pyttsx3.init('sapi5')
voices=engine.getproperty('voices')
engine.setproperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good mornning")
    elif hour >= 12 and hour <= 16:
        speak("Good afternoon sir")
    else:
        speak("good evening sir")     

    speak("I am W ,may i help you")

def takeCommand():
    recognizer=speech_recognition.Recognizer
    with speech_recognition.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio=recognizer.listen(source)
    try:
        print("Recognizing...")    
        query=recognizer.recognize_google(audio,language='en-in')
        print(f"user said {query}\n")

    except Exception as e:
        print("say that please again")
        return "none"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP("smtp.email.com",587)
    server.ehlo()
    server.starttls()
    server.login("yadavprateek697@gmail.com","prateekyadav@999")
    server.sendmail("akyyarmyboy@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()
        if wikipedia in query:
            speak("Searching wekipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'playmusic' in query:
            music_dir='E:\\video\\dataStructure\\_Dawn_Of_Justice_-_HINDI_Trailer(480p)'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'open vs code' in query:
            codePath = ':\\Users\\prateek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'email to prateek' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to="aky2@gmail.com"
                sendEmail(to,content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry my friend mahesh i am not able to send massage")

            

            

        

    

            


