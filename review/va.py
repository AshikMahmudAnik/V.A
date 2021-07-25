import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
cortana = pyttsx3.init()
voices = cortana.getProperty('voices')
cortana.setProperty('voice', voices[1].id)


def talk(text):
    cortana.say(text)
    cortana.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def run_cortana():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Yes, I agree')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    run_cortana()
