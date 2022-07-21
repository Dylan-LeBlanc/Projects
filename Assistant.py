import speech_recognition as sr
import webbrowser as wb
import os
import pyttsx3 as ai
engine = ai.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def main():
    while True:
        text = listen()
        statement(text)

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.record(source, duration = 4)
            try: 
                text = r.recognize_google(audio, language = 'en-US')
            except Exception as e:
                text = "none"
                return text
    if (audio is not True):
                text = r.recognize_google(audio, language = 'en-US')
                

    return text
def statement(text):
    try:    
                ############## Turn Off Commands #############
                if text == "Quantum go to sleep":
                    ai.speak('Quantum is going to sleep')
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                if text == "Quantum turn off":
                    ai.speak('Quantum is shutting down')
                    os.system('shutdown /s /t 1')

                ############## Website Commands ##############

                if text == "Quantum open YouTube":
                    wb.open('http://YouTube.com')
                    ai.speak("Opening Youtube")
                if text == "Quantum open Google":
                    wb.open('http://Google.com')
                    ai.speak("Opening Google")
        
                ############## App Commands (Open) ###############

                if text == "Quantum open valorant":
                    ai.speak("opening valorant")
                    os.startfile('C:\Riot Games\Riot Client\RiotClientServices.exe')
                if text == "Quantum open Spotify":
                    ai.speak("opening spotify")
                    os.startfile('spotify.exe')
                if text == "Quantum open Epic":
                    ai.speak("opening Epic Games")
                    os.startfile('C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe')
                if text == "Quantum open Steam":
                    ai.speak("opening steam")
                    os.startfile('C:\Program Files (x86)\Steam\steam.exe')

                ############# App Commands (Close) ##############

                if text == "Quantum exit rocket League":
                    ai.speak("Closing rocket league")
                    os.system("TASKKILL /F /IM RocketLeague.exe")
                if text == "Quantum exit valorant":
                    ai.speak("Closing Valorant")
                    os.system("TASKKILL /F /IM VALORANT-Win64-Shipping.exe")
                    os.system("TASKKILL /F /IM RiotClientServices.exe")
                if text == "Quantum exit Fall Guys":
                    ai.speak("Closing fall guys")
                    os.system("TASKKILL /F /IM FallGuys_client_game.exe")
                if text == "Quantum exit Steam":
                    ai.speak("Closing steam")
                    os.system("TASKKILL /F /IM steam.exe")
                if text == "Quantum exit Spotify":
                    ai.speak("Closing spotify")
                    os.system("TASKKILL /F /IM spotify.exe")
                print("You said : {}".format(text))

    except:
        print("Sorry could not recognize what you said")   
main()