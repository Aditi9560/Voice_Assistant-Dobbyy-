import speech_recognition as sr
import webbrowser
import pyttsx3
#pip install pocketsphinx
import musiclibrary
import requests
from openai import OpenAI

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="904676dcac574062bedcb44b4926f058"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="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",)

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant dobby."},
        {"role": "user",  "content": command}
    
    ]
)

    return(completion.choices[0].message.content)

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open leetcode" in c.lower():
        webbrowser.open("https://www.leetcode.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")

        if r.status_code ==200:
            #parse the json response
            data=r.json()

            #extract the articles
            articles=data.get('articles',[])

            #print the headlines
            
            for article in articles:
                speak(article['title'])
    else:
        #let open ai handle the request
        output=aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing dobby.....")

    while True:
        #listen for the wake word dobby
        #obtain audio from microphone
        r = sr.Recognizer()
        print("recognizing..")
    # recognize speech using google
        try:
            with sr.Microphone() as source:
                 print("Listening....!")
                 audio = r.listen(source,timeout=2,phrase_time_limit=1)

            
            word= r.recognize_google(audio)
            if(word.lower()=="dobby"):
                speak("ya")

            #listen for command
            with sr.Microphone() as source:
                 print("dobby Active...!")
                 audio = r.listen(source)

                 command= r.recognize_google(audio)
                 processcommand(command)
            

        except Exception as e:
            print("error; {0}".format(e))