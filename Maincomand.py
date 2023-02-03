import speech_recognition as sr
import os
import sys
import webbrowser
import datetime

now = datetime.datetime.now()

def talk(words):
	print(words)
	os.system("say " + words)
talk("Привіт, чим я можу допомогти вам?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говоріть")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="uk-UA").lower()
        print("Ви сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не зрозуміла")
        zadanie = command()
    return zadanie

def makeSomething(zadanie):
    if 'відкрий сайт' in zadanie:
        talk("Вже відкриваю")
        url = 'https://www.youtube.com/shorts/9ecSqQVXAbg'
        webbrowser.open(url)

    elif 'стоп' in zadanie:
        talk("Так, звичайно, без проблем")
        sys.exit()
    elif 'привіт' in zadanie:
        talk("Привіт, я, Сірі")
    elif 'котра година' in zadanie:
        print (str(now))
    elif 'який рік' in zadanie:
        print("%d" % now.year)
    elif 'який місяць' in zadanie:
        print("%d" % now.month)
    elif 'який день' in zadanie:
        print("%d" % now.day)
while True:
	makeSomething(command())