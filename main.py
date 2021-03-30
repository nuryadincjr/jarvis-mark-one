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
from word2number import w2n
from email.message import EmailMessage

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


def run_engine():
    command = take_command()
    if 'who am I' in command:
        talk('Nuryadin Abutani')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print('Currant dare is '+time)
        talk('Currant dare is ' + time)
    elif 'date' in command:
        time = datetime.datetime.now().strftime('%A %m %B %Y')
        print(time)
        talk('Currant time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'what is' in command:
        person = command.replace('what is', "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'I love you' in command:
        talk('I love you to')
    elif 'your name' in command:
        talk('my name is john')
    elif 'jook' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'write' in command:
        message = command.replace('write', '')
        pyautogui.typewrite(message)
        pyautogui.press('enter')
    elif 'send email' in command:
        email_info()
    elif 'book' in command:
        pdf_reader()
    elif 'translate' in command:
        person = command.replace('translate', '')
        translate(person)
    else:
        talk('Please say the command again')


def pdf_reader():
    book = open('read.pdf', 'rb')
    pdfReader = PyPDF4.PdfFileReader(book)
    page = pdfReader.numPages
    print('All page is ' +str(page))

    talk('What page will you start from?')
    page_start = w2n.word_to_num(take_command())
    print('Start page is '+str(page_start))
    talk('Until what page do you read?')
    page_end = w2n.word_to_num(take_command())
    print('End page is '+str(page_end))
    for num in range(page_start, page_end):
        page = pdfReader.getPage(page_start)
        text = page.extractText()
        print('Reading from pages '+str(page_start)+" of "+str(page_end))
        talk(text)


email_list = {
    'nuryadin': 'nuryadin.cjr@gmail.com',
    'abu': 'nuryadin.abu@gmail.com',
    'alia': 'aliya.sucirahayu@gmail.com'
}


def email_send(reciver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('abugrayhat@gmail.com', 'your_password')
    email = EmailMessage()
    email['From'] = 'abugrayhat@gmail.com'
    email['To'] = reciver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    talk('Your email has been sent')


def email_info():
    talk('To who you wont to send email?')
    name = take_command()
    reciver = email_list[name]
    talk('What is the Subject of your email?')
    subject = take_command()
    talk('Tell me the text in your email?')
    message = take_command()
    email_send(reciver, subject, message)


def translate(person):
    # print(googletrans.LANGUAGES)
    translator = googletrans.Translator()
    translated = translator.translate(person, dest=output_lang)
    converted_oudio = gtts.gTTS(translated.text, lang=output_lang)
    print(person)
    print(translated.text)
    converted_oudio.save('translate.mp3')
    playsound.playsound('translate.mp3')


while True:
    run_engine()
