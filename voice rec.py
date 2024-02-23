import speech_recognition as pr
import pyttsx3
import wikipedia
import webbrowser
import datetime

engine = pyttsx3.init()
time = int(datetime.datetime.now().hour)

count = 0


def voice(c):
    engine.say(c)
    engine.runAndWait()


def rec():
    rec2 = pr.Recognizer()
    with pr.Microphone() as source:
        print("listening...")
        rec2.pause_threshold = 0.5
        audio = rec2.listen(source)
    try:
        rec1 = rec2.recognize_google(audio)
        print("you said::", rec1)
        return rec1
    except Exception:
        w = 'empty'
        return type


if 0 < time < 12:
    voice('good morning sir!')
elif 12 <= time < 18:
    voice('good afternoon sir!')
else:
    voice('good evening sir!')
voice('how can i help you')
while True:
    try:
        query1 = rec()
        query = query1.lower()
        if "your name" in query:
            voice('sir, i am jarvis the voice engine ')
            voice('i am at your service sir!')

        elif "my name" in query:
            voice('sir!')
            voice('your name  vinay,you born in 13 septumber 1999')

        elif "good name" in query:
            voice('thank you sir!')
            voice('sir,any thing else')
        elif 'no' in query or 'bye' in query:
            voice('ok bye.. sir! ')
            break
        elif 'wikipedia' in query:
            rep1 = query.replace(" jarvis", " ")
            rep2 = rep1.replace(" according to wikipedia", " ")
            wiki = wikipedia.summary(rep2, sentences=1)
            voice('got it sir!')
            voice('according to wikipedia')
            print(wiki)
            voice(wiki)
        elif 'time' in query:
            day = datetime.datetime.now().day
            date = datetime.datetime.now().year
            t = datetime.datetime.now().strftime('%H:%M')
            voice('sir, the time is {}'.format(t))
            voice('day{}, and  ,year{}'.format(day, date))
        elif 'open ' in query:
            lis = ['youtube', 'google', 'gana', 'wikipedia']
            for i in lis:
                if i in query:
                    text1 = query.replace(query, i)
                    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab(
                        text1 + ".com")
        elif 'play music' in query:
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab(
                'www.youtube.com/watch' + '?v=4dbiE-da82E&list=R' + 'D4dbiE-da82E&start_radio=1')
        elif 'search' in query:
            text2 = query.replace("search", ' ')
            webbrowser.get('C:/Program Files /Google/Chrome/Application/chrome.exe %s').open_new_tab(
                'https://www.google.com/search?q=' + text2)
        elif 'on youtube ' in query:
            text3 = query.replace('on youtube', ' ')
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab(
                'https://www.youtube.com/results?search_query=' + text3)
        else:
            voice('sorry i can not understand ')

        voice('next command sir!')
    except Exception:
        if count!=1:
         voice('sir,please try again i did not get that sql query')
         voice('i am unable to enter into the server!')
         count+=1
        else:
            voice('Access denied.')
            break