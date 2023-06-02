import random

import speech_recognition as sr
import os
import win32com.client
import webbrowser
from playsound import playsound
import openai
import datetime
from AppOpener import open
from AppOpener import close
speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"USER: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def say(text):
    speaker.Speak(text)

def ai(prompt):
    openai.api_key = "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"

    while True:
        model = "text-davinci-003"
        user = query


        print("Genarating....")
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=user,
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            n=1,
            stop=None
        )

        response = completion.choices[0].text
        print(response)
        say(response)
        break

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some Error Occured . Sorry From Jarvis"


#def say(text):
 #   os.system(f"say {text}")
if __name__ == '__main__':


     text="Hello! Welcome To JARVISE "
     say(text)
     while True:
        print("Listening....")
        query = takeCommand()
        sites = [["Youtube" ,"https://www.youtube.com/"],["Google" ,"https://www.google.com/"],["Jio Cinema", "https://www.jiocinema.com/"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir... ")
                webbrowser.open(site[1])
        #say(query)
        #if "open music".lower() in query.lower():
            #playsound = (cd\Users\KIIT\Documents\music\O Bedardeya_320(PagalWorld.com.se).mp3)
            #say.Starfile(f"Opening {musicPath}")
        #if "open chrome".lower() in query.lower():
         #   chromepath=("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
          #  speaker.Speak(f"opening Chrome {chromepath}")
        if "the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f" sir time {strfTime} Hora  hai ")
        apps =[["google chrome"],["netflix"],["wps office"],["calculator"],]
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]} Sir...")
                open(app[0])
            if f"close {app[0]}".lower() in query.lower():
                say(f"Closing {app[0]} Sir...")
                close(app[0])
        if "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)









