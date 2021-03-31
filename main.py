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
default_input_lang = 'id'
default_output_lang = 'en'


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language=default_input_lang)
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
        translate()
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

all_lang = {
        'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
         'basque': 'eu', 'belarusian':'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
         'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
         'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
         'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
         'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
         'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn',
         'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it',
         'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
         'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt',
         'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt',
         'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne',
         'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt',
         'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr',
         'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl',
         'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg',
         'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug',
         'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
    }

def translate():
    lang_list = googletrans.LANGUAGES
    talk('into what language do I translate?')
    # print(lang_list['en'])
    commend = take_command()
    output_lang = all_lang[commend]
    input_lang = default_input_lang
    print(lang_list[input_lang] +" to " +lang_list[output_lang])
    talk('what can i translate?')
    person = take_command()
    translator = googletrans.Translator()
    translated = translator.translate(person, dest=output_lang)
    converted_oudio = gtts.gTTS(translated.text, lang=output_lang)
    print(person)
    print(translated.text)
    converted_oudio.save('translate.mp3')
    playsound.playsound('translate.mp3')


while True:
    run_engine()
