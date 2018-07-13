import time
import os
import sys
import logging
from time import ctime
import speech_recognition as sr

def restart() :
    try:
        while True:
                time.sleep(0.5)
               # os.execv('/home/pi/myPiConfig/Test/restartMySelf.py',  [''])
                os.execv(sys.executable, [sys.executable] +  ['cathi-stt.py'])
    except KeyboardInterrupt:
        print ("Quit")
    except Exception as e:
        print ("Quit with error " + str(e))

def main() :
    print("")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        print(r.recognize_google(audio))
        time.sleep(0.5)
        restart()
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you were saying. Please try again")
        restart()
    except sr.RequestError as e:
        print("Sorry, our systems are clogged up. Please try again later.")
        restart()

main()
