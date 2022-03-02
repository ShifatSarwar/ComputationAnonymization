import pyttsx3
import scenarioRunner
import boxPlotMnM
import random
import os
from gtts import gTTS
import playsound
engine = pyttsx3.init()
#It allows Speak rather than print out words
def speak(command):
    tts = gTTS(text=command, lang='en')
    r = random.randint(1,10000000)
    audiofile = 'audio-'+str(r) + '.mp3'
    tts.save(audiofile)
    playsound.playsound(audiofile)
    os.remove(audiofile)


if __name__ == '__main__':
    # scenarioRunner.runGraphAnonymizedInitial(3, 3)
    boxPlotMnM.genValGraphSame(35)
    # scenarioRunner.runGraphMnMInitial(2)
    speak("Process Complete")  
    print("Process Complete")      
        
        



