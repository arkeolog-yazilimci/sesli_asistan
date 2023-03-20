from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import pyaudio
import os
import random

r = sr.Recognizer()

def record(ask= False):
    with sr.Microphone() as source :
        if ask:
            print(ask)
    audio = r.listen(source)
    voice = ""
    try:
        voice = r.recognize_google(audio,language="tr-TR")
    except sr.UnknownValueError:
        print("Asistan : anlayamadım")
    except sr.RequestError:
        print("Asistan: Sistem Çalışmıyor")
    return voice


def speak(string):
    tts = gTTS(text=string,lang="tr")
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Hoş Geldin")
voice = record()
if voice != '':
    print(voice)

