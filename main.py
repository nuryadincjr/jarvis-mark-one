import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import smtplib
import PyPDF4
import googletrans
import gtts
import playsound
from email.message import EmailMessage

from pip._vendor.chardet.metadata import languages

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
input_lang = 'id-ID'
output_lang = 'en'

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language=input_lang)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Currant time is ' + time)
    elif 'pukul' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Sekarang pukul ' + time)
    elif 'what is' in command:
        person = command.replace('what is', "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'I love you' in command:
        talk('oh, I love you to')
    elif 'your name' in command:
        talk('my name is jarvis')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'write' in command:
        message = command.replace('write', '')
        pyautogui.typewrite(message)
        pyautogui.press('enter')
    elif 'kirim email' in command:
        email_info()
    elif 'read a book' in command:
        pdf_reader()
    elif 'terjemah' in command:
        person = command.replace('terjemah', '')
        translate(person)
    elif 'siapa saya' in command:
        talk('Bos besar')
    else:
        talk('Please say the command again')

def pdf_reader():
    book = open('read.pdf', 'rb')
    pdfReader = PyPDF4.PdfFileReader(book)
    page = pdfReader.numPages
    print(page)
    page = pdfReader.getPage(100)
    text = page.extractText()
    talk(text)

email_list = {
    'nuryadin': 'nuryadin.cjr@gmail.com',
    'abu': 'nuryadin.abu@gmail.com',
    'alia': 'aliya.sucirahayu@gmail.com'
}

def translate(person):
    # print(googletrans.LANGUAGES)
    translator = googletrans.Translator()
    translated = translator.translate(person, dest=output_lang)
    converted_oudio = gtts.gTTS(translated.text, lang=output_lang)
    print(person)
    print(translated.text)
    converted_oudio.save('translate.mp3')
    playsound.playsound('translate.mp3')


def email_send(reciver,subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('abugrayhat@gmail.com', 'password')
    email = EmailMessage()
    email['From'] = 'abugrayhat@gmail.com'
    email['To'] = reciver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    talk('Your email has been sent')

def email_info():
    talk('Kepada siapa email akan dikirim?')
    name = take_command()
    reciver = email_list[name]
    talk('Apa sabjek dari email anda?')
    subject = take_command()
    talk('Beritahu saya apa pesannya?')
    message = take_command()
    email_send(reciver, subject, message)

while True:
    run_jarvis()
