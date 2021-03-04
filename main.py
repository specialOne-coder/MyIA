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


def parler(text):
    moteur.say(text)
    moteur.runAndWait()


def prendreCommande():
    try:
        with sr.Microphone() as source:
            print("J'écoute.....")
            voix = ecouteur.listen(source)
            commande = ecouteur.recognize_google(voix)
            commande = commande.lower()
            if 'fernanda' in commande:
                commande = commande.replace('fernanda','')
                print(commande)
                parler("Bonjour")
            else:
                parler('je mappele fernanda')
                print('je m\'appele fernanda')
    except:
        pass
    return commande


def run_fernanda():
    commande = prendreCommande()
    print(commande)
    if 'joue' in commande:
        son = commande.replace('joue','')
        parler('je joue le son de' + son)
        pywhatkit.playonyt(son)
        print('joue ...')
    elif 'heure' in commande:
        heure = _datetime.datetime.now().strftime('%H:%M')
        print(heure)
        parler('il est  ' + heure)
    elif 'Bonjour' in commande:
        parler('Bonjour')
        parler('Je suis fernanda')
        parler('Que puis je faire pour toi')
    elif 'ça va' in commande:
        print("je vais bien et toi ")
        parler("je vais bien et toi ")
    elif 'appele' in commande:
        print("je m'appelle fernanda ")
        parler("je m'appelle fernanda ")
    elif 'video' in commande:
        son = commande.replace('joue', '')
        parler('je joue ' + son)
        pywhatkit.playonyt(son)
        print('joue ...')
    elif 'que signifie' in commande:
        personne = commande.replace('que signifie','')
        info = wikipedia.summary(personne,1)
        print(info)
        parler(info)
    elif 'qui est' in commande:
        personne = commande.replace('que est','')
        info = wikipedia.summary(personne,1)
        print(info)
        parler(info)
    elif 'date' in commande:
        date = _datetime.datetime.now().date()
        print(date)
        parler('aujourdhui cest le  ' + date)
    elif 'seul' in commande:
        print("Je suis en couple avec ferdinand")
        parler( "Je suis en couple avec ferdinand")
    elif 'parle' in commande:
        parler(pjo.get_jokes())
    elif 'gl' in commande:
        parler('Ferdinand')
        parler('Christian')
        parler('Firmin')
        parler('Sodjine')
        parler('Benjamin')
        parler('Kelly')
        parler('Adriano')
    elif 'journe' in commande:
        parler('Tout va bien et de ton coté')
    else:
        parler('Sil vous plaît jai rien entendu')

while True:
    run_fernanda()