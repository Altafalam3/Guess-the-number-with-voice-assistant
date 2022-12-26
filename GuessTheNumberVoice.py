import random
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# 0 is for male,1 is female voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeInput():
   # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Speak the Number...")
        print("Speak the Number...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        speak("Recognizing the number...")
        print("Recognizing the number...")
        query = r.recognize_google(audio, language='en-in')

        speak(f"User guess number: {query}")
        print(f"User guess number: {query}")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query



# random number generating
num = random.randint(1, 100)
# print(num)

guess = None
guesses = 0
flag = False

speak("You have 10 chances to guess the correct number..")
print("You have 10 chances to guess the correct number..")

while guess != num and guesses < 10:
    dummyguess = takeInput()

# check if input is number or it hasnt heard it properly
    if (dummyguess.isdigit()):
        guess = int(dummyguess)
    else:
        while(not dummyguess.isdigit()):
            speak("Give the input again since it is not integer")
            print("Give the input again since it is not integer")
            dummyguess = takeInput()
        guess=int(dummyguess)

    guesses += 1
    if (guess == num):
        flag = True
        break
    else:
        if (guess > num):
            speak("You have guessed higher..Guess a lower number")
            print("You have guessed higher..Guess a lower number")
        else:
            speak("You have guessed lower..Guess a higher number")
            print("You have guessed lower..Guess a higher number")

if (flag):
    speak(f"\nYou wonnn !! \nYou guessed the correct answer in {guesses} guesses")
    print(f"\nYou wonnn !! \nYou guessed the correct answer in {guesses} guesses")
else:
    speak(f"\nYou guessed the correct answer in {guesses} guesses")
    print("\nGame over ...Guesses over, try again!")
