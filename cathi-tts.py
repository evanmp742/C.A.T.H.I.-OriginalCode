import time
import os
import sys
import logging
from time import ctime
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def restart() :
    try:
        while True:
                time.sleep(0.5)
               # os.execv('/home/pi/myPiConfig/Test/restartMySelf.py',  [''])
                os.execv(sys.executable, [sys.executable] +  ['cathi-tts.py'])
    except KeyboardInterrupt:
        print " Quit"
    except Exception as e:
        print " Quit with error " + str(e)

def main() :
    text = raw_input('Enter something to say: ')
    tts = gTTS(text, lang='en')
    tts.save("tmp.mp3")
    song = AudioSegment.from_mp3("tmp.mp3")
    play(song)
    os.remove("tmp.mp3")
    restart()

main()
