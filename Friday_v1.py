import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

speech = sr.Recognizer()


greeting_dic = {'hello':'hello','hi':'hi'}
mp3_greeting_list = ['Friday\greeting_accept.mp3','Friday\greeting_accept_2.mp3']

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print('Listening........')
    with sr.Microphone() as source:
        audio = speech.listen(source=source,timeout=10,phrase_time_limit=5)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('network error.')
    except sr.WaitTimeoutError:
        pass

    return voice_text

def is_valid_greeting(greeting_dic,voice_note):
    for key, value in greeting_dic.iteritems():
        #'Hello Friday'
        if value== voice_note.split(' ')[0]:
            return True
            break
        else:
            return False



if __name__ == '__main__':

    playsound('Friday\greeting.mp3')


    while True:

        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))

        if is_valid_greeting(greeting_dic,voice_note):
            print('In greeting.............')
            play_sound(mp3_greeting_list)
            continue
        elif 'open' in voice_note:
            os.system('explorer C:\\"{}"'.format(voice_note.replace('open', '')))
            continue
        elif 'by' in voice_note:
            exit()





