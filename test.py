import speech_recognition as sr
import pyttsx3
import pywhatkit
import _datetime
import wikipedia
import pyjokes as pjo


ecouteur = sr.Recognizer()
moteur = pyttsx3.init()
voices = moteur.getProperty('voices')
moteur.setProperty('voices',voices[1].id)


try:
    with sr.Microphone() as source:
        print("J'écoute.....")
        voix = ecouteur.listen(source)
        commande = ecouteur.recognize_google(voix)
        commande = commande.lower()
        if 'fernanda' in commande:
            commande = commande.replace('fernanda','')
            print(commande)
            moteur.say("Bonjour")
        else:
            moteur.say('je mappele fernanda')
            print('je m\'appele fernanda')

except:
    pass