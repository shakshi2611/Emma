import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")    
    else:
        speak("good evening!") 

    speak("i am Emma sir, Please tell me how may i help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:

        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

    #logic for executing tasks based on query

    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
