import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Moring!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello sir, I am jarvis. How may i help you")


def takeCommand():
    # it takes microphone input from the user and return a string.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognzing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if('wikipedia' in query):
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif('open youtube' in query):
            webbrowser.open("youtube.com")

        elif('open google' in query):
            webbrowser.open("google.com")

        elif('open stack overflow' in query):
            webbrowser.open("stackoverflow.com")

        elif('play music' in query):
            music_dir = "D:\\Python with Harry\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif('the time' in query):
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"sir, the time is {strTime}")

        elif('open code' in query):
            codePath = "C:\\Users\Aman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
