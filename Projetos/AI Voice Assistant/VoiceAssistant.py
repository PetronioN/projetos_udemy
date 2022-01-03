import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import warnings
import smtplib
import webbrowser as wb
import os
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes # pip install pyjokes

wikipedia.set_lang("pt")

warnings.catch_warnings()

warnings.simplefilter("ignore")

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

newVoiceRate = 250 # Velocidade da voz
engine.setProperty('rate', newVoiceRate)

def speak(audio): # Função de saída de áudio.
    engine.say(audio)
    engine.runAndWait()

def time(): # Retorna o horário
    timeNow = datetime.datetime.now().strftime("%I:%M:%S")
    speak("São")
    speak(timeNow)

def date(): # Retorna a data atual
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("A data atual é")
    speak(date)
    speak("do")
    speak(month)
    speak("de")
    speak(year)

def wishme(): # Retorna as boas vindas e informações iniciais
    
    global timeDay

    speak("Seja bem vindo de volta!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        timeDay = "Tenha um bom dia!"
        speak("Bom dia!")
    elif hour >= 12 and hour < 18:
        timeDay = "Tenha uma boa tarde!"
        speak("Boa tarde!")
    elif hour >= 18 and hour <= 24:
        timeDay = "Tenha uma boa noite!"
        speak("Boa noite!")
    else:
        timeDay = "Tenha um bom dia!"
        speak("Bom dia!")
    speak("Lisa a seu serviço. Em que posso ajudar você?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language = 'pt-Br') # Reconhecer a fala na lingua escolhida
        print(query)
    except Exception as e:
        print(e)
        speak("Fale novamente, por favor...")

        return "None"

    return query

def SendMail(to, content): # Envio de email de um email para outro
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("emaillogin@gmail.com", "1234senha")
    server.sendemail("emaillogin@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/PC/Pictures")

def cpu():
    usage = str(psutil.cpu_percent)
    speak("CPU está em " + usage)

    battery = psutil.sensors_battery
    speak("Bateria está em ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        # Conjunto de if para reconhecer o que você está em busca
        if "horário" in query:
            time()
            
        elif "data" in query:
            date()

        elif "sair" in query:
            speak(timeDay)
            quit()

        elif "wikipédia" in query:
            speak("Buscando...")
            query = query.replace("wikipédia", "")
            try:
                result = wikipedia.summary(query, sentences = 2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)

        elif "envie um e-mail" in query:
            try:
                speak("O que eu devo escrever?")
                content = takeCommand()
                to = "teste@gmail.com"
                SendMail(to, content)
                speak("O email foi enviado com sucesso.")
            except Exception as e:
                speak(e)
                speak("O email não pôde ser enviado.")

        elif "pesquise no google" in query:
            speak("O que eu devo pesquisar?")
            ChromePath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(ChromePath).open_new_tab(search + ".com.br")
        
        elif "desligar" in query or "logout" in query:
            os.system("shutdown - 1")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query or "reiniciar" in query:
            os.system("shutdown /r /t 1")

        elif "lembre" in query:
            speak("O que eu devo lembrar?")
            data = takeCommand()
            speak("Você me pediu para lembrar de " + data)
            remember = open("data.txt", "w") # Opção write(escrever)
            remember.write(data)
            remember.close()
        
        elif "armazenado" in query:
            remember = open("data.txt", "r") # Opção read(ler)
            speak("Você me pediu para lembrar de " + remember.read())
        
        elif "screenshot" in query:
            screenshot()
            speak("Feito!")

        elif "cpu" in query:
            cpu()
        
        elif "piada" in query: # Infelizmente o pyjokes não está disponível em pt-BR.
            jokes()
