# Task : voice assistant
# zeel shah

import streamlit as st # for streamlit
import pyttsx3 
import speech_recognition as sr
import wikipedia # for wikipedia
import webbrowser # for browser
import os
import datetime # for date and time
import pywhatkit # for youtube

engine = pyttsx3.init()
recognizer = sr.Recognizer()

# for audio of the virtual assistance
def speak(audio):
    #Speaks the provided audio using pyttsx3
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

# for gerreting everytime you click button
def greet():
    
    speak("welcome I am your virtual assistant. What can I help you with today?")

# for command that you give to your assistance
def command():
    #Listens for user input using speech recognition.
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
    
        print('Recognizing...')
        user_input = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {user_input }\n")
        st.write(user_input )
        return user_input .lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Could not request results from Google Web Speech API.")
        return None

# taking action depending on the command
def take_action(user_input):
    
    if user_input  in ('stop', 'exit','bye'):
        speak("Goodbye! Have a nice day.")
        st.stop()

    elif 'hello' in user_input :
        speak("hello welcome to virtual assistant what do you want me to do for you ")
        st.write("hello welcome to virtual assistant what do you want me to do for you ")
    elif 'what is your name' in user_input :
        speak("I am your virtual assistant , i am here to help you out")
        st.write("I am your virtual assistant , i am here to help you out")
    elif 'how are you' in user_input :
        speak("I am fine, how about you ? do you need any help")
        st.write("I am fine, how about you ? do you need any help")
    
    #open youtube video 
    elif 'youtube' in user_input :
        pywhatkit.playonyt(user_input )
        st.write("Opening YouTube...")

    
    # open any website or anything on google
    elif 'open' in user_input :
        pywhatkit.search(user_input ) 
        st.write("Opening Google...")

    #display current time
    elif 'time' in user_input :
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        st.write(f"The time is {strTime}")

    #display current date
    elif 'date' in user_input :
        date=datetime.datetime.now().strftime('%d /%m /%y')
        speak(f"Today's date is"+date)
        st.write(f"The date is {date}")

    # wether information about coresponding city or country
    elif 'weather' in user_input :
       pywhatkit.search(user_input )
       st.write("Opening weather forecast...")
    
    # search any text on wikipedia
    else:
        speak('Searching Wikipedia...')
        user_input  = user_input .replace("wikipedia", "")
        result = wikipedia.summary(user_input , sentences=2)
        speak("According to Wikipedia")
        st.write(result)
        speak(result)


def main():
    # Streamlit application.
    st.title("Virtual Assistant")
    greet()
    st.write("click on the button to speak")
    

    if st.button("Listen"):
        user_input = command()
        if user_input :
            take_action(user_input )


if __name__ == "__main__":
    main()
