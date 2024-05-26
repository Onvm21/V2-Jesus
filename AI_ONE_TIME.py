from gpt4all import GPT4All

#from GUI import *

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
import speech_recognition as sr  # create SR as speech rec.
import pyttsx3

global command1, command, response

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 180)  # change of speed
engine.say('Listening')
engine.runAndWait()

#print_response = tk.Label(root, text = "listening", font=("Times New Roman", 20)) # these two aren't doing anything either... they might have been overriden by the gpt code.
#print_response.pack

response = ""

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("listening...")
            #print_response2 = tk.Label(root, text = "listening", font=("Times New Roman", 20))
            #print_response2.pack
            voice = listener.listen(source)  # definition for the voice input
            command = listener.recognize_google(voice)  # this is a google api that recognises the sound passed in and makes it into text
            command = command.lower()
            if 'jesus' in command:
                command = command.replace('jesus', '')
                print(command)
                return command
    except:
        pass
    #return command


def Run_program():
    ask = take_command()
    with model.chat_session():
        response1 = model.generate(prompt=ask, temp=0)
        talk(response1)
        response = response1
        print(response)
    #return response


Run_program()
print(response)