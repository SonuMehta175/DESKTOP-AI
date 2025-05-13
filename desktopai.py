from openai import OpenAI  # chatbot like interaction 
import pyaudio             # for input and output of audio
from geopy.geocoders import Nominatim # converting address in latitude 
import asyncio                        # use for asynchronous sleep 
import subprocess  # use for open notepad 
import webbrowser  # use for open google 
import pyttsx3     # use for converting text to speech
import qrcode      # use for generate qr code and saving it 
import datetime    # for current time
import speech_recognition as sr #create a recognizer (no speech recognisation permed in one line)
import requests     # to interact with websites and apis 
from bs4 import BeautifulSoup # for html or xml document joined with request 
import os # use for interact with system
import psutil # system performance monitoring like process ending starting 
import pyautogui   #moves the mouse to a position 
import wikipedia   # searching for something "like python"
import pywhatkit   # sending whatsapp messages instantly
import random      #generate random number
from plyer import notification    #desktop notification displaying
from pygame import mixer          # initialize sound mixer 
import speedtest                  # for internet speed
from pynput.keyboard import Key,Controller# for keyboard keys controller
from time import sleep            # pause execution for some time 
from googletrans import Translator # translating something 
from gtts import gTTS             #convert speech and saving somewhere in file 
import googletrans                # for translating something 
import geocoder                   # get ip location 
from playsound import playsound   #plays generated speech
import time                       #work related with time
import json                       #writes a sample dictionary from apis 
from tkinter import *             #opens a gui window 
from PIL import Image,ImageTk,ImageSequence # manipulating images
keyboard = Controller()
mixer.init()

for i in range(3):  
    a = input("Enter Password to get help from kanha :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME ! PLZ SPEAK [radhe radhe] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")


root = Tk()
root.geometry("1000x500")
# function for playing a glf in starting to give a graphical interactive interface 
def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("nova.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("Startup2.mp3")
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.02)
    root.destroy()
play_gif()
root.mainloop()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

#function for speaking something by the engine
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function for taking voice command
def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 100  # Ignores background noise/music
    r.dynamic_energy_threshold = True  # Auto-adjust to environment

    with sr.Microphone() as source:
        print("Listening your command ...")

        r.adjust_for_ambient_noise(source, duration=1)  # Noise adaptation

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Capture voice
        except sr.WaitTimeoutError:
            print("No speech detected. Try again.")
            return "None"

    try:
        print("Processing speech...")
        query = r.recognize_google(audio, language='en-in')  # Recognize speech
        print(f"You said: {query}\n")
        return query.lower()  # Convert to lowercase for easy comparison

    except sr.UnknownValueError:
        print("Couldn't understand the command. Please repeat.")
        return "None"

    except sr.RequestError:
        print("Network error. Check your internet connection.")
        return "None"

#function for greeting in starting 
def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("radhe radhe ,goodmorning")
    elif hour >12 and hour<=18:
        speak("radhe radhe, Good Afternoon ")

    else:
        speak("radhe radhe Good Evening")

    speak("Please tell me, How can I help you ?")

#function for playing the music from existing music folder from the system system 
def play_music():
    music_folder =  "C:\\Users\\mehta\\Music"
    songs = os.listdir(music_folder)
    song = random.choice(songs)
    song_path = os.path.join(music_folder, song)
    os.startfile(song_path)
#function for closing file 
def close_file():
    speak("Please specify the file or application name you want to close.")
    file_name = takeCommand().strip().lower()  # Take voice input

    if not file_name or file_name in ["cancel", "exit", "stop"]:
        speak("Okay, cancelling the request.")
        return

    found = False  # Flag to check if the file is found
    
    # Loop through all running processes
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            if file_name in process_name:  # Check if filename matches
                os.system(f"taskkill /F /PID {process.info['pid']}")  # Force kill
                speak(f"Closing {process_name}")
                found = True
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Skip any processes that can't be accessed

    if not found:
        speak("File or application not found. Please check the name and try again.")

#function for file opening 
def open_file():
    speak("Please specify the file name or full path.")
    file_name = takeCommand().strip().lower()  # Take voice input

    if not file_name or file_name in ["cancel", "exit", "stop"]:
        speak("Okay, cancelling the request.")
        return
    
    # If the user provides a full file path
    if os.path.isfile(file_name):  # Check if file exists
        os.startfile(file_name)
        speak(f"Opening {file_name}")
        return

    # Get the current user's home directory
    user_home = os.path.expanduser("~")  # Fetches C:\Users\YourUsername

    # Common directories to search
    common_dirs = [
        os.path.join(user_home, "Documents"),
        os.path.join(user_home, "Downloads"),
        os.path.join(user_home, "Desktop")
    ]

    found = False  # Flag to check if the file is found

    for directory in common_dirs:
        for root, _, files in os.walk(directory):  # Walk through folders
            for file in files:
                if file_name in file.lower():  # Check if filename matches
                    file_path = os.path.join(root, file)
                    os.startfile(file_path)
                    speak(f"Opening {file}")
                    found = True
                    return

    if not found:
        speak("File not found. Please try again with the correct name or full path.")

# function for search song on the youtube
def search_on_youtube(song_name):
    try:
        # Construct the YouTube search URL
        search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"

        # Open the web browser and search for the song on YouTube
        webbrowser.open(search_url)
    except Exception as e:
        print("An error occurred:", str(e))
        print("Sorry, I couldn't perform the search.")

# function for checking the internet speed 
def check_internet_speed():
    st=speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / (1024 * 1024)  # Convert bytes to megabits
    upload_speed = st.upload() / (1024 * 1024)  # Convert bytes to megabits
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")
    speak(f"Download Speed is {download_speed:.2f} Mbps")
    speak(f"Upload Speed is {upload_speed:.2f} Mbps")
    speak(f"Ping is {ping} milliseconds")
#function for checking current location 
def get_current_location():
    try:
        # Get the current location based on IP address
        location = geocoder.ip('me')
        if location:
            return location.address
        else:
            return "Location not found."
    except Exception as e:
        print(f"Error occurred while getting location: {str(e)}")
        return "Location not found."

# for generating qr code which u want to make like for instagram , whatsapp, phonepay etc 
def generate_qr_code(text_or_url, filename="qr_code.png"):
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(text_or_url)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(filename)

        print(f"QR code generated successfully as {filename}")
    except Exception as e:
        print(f"Error occurred while generating QR code: {str(e)}")

# a small game for refreshing mind doing work 
def game_play():
    print("LETS PLAYYYYYYYYYYYYYY")
    speak("Lets Play ROCK PAPER SCISSORS !!")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

# for volume inreasing function 
def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
# volume fecreasing function 
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
# for searching something on google function  
def searchGoogle(query):
        if "google" in query:
         import wikipedia as googleScrap
        query = query.replace("nova","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")
# searching something on you tube 
def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("nova","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Mam")
# searching something from wikipedia 
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("nova","")
        Results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(Results)
        speak(Results)
#for translating something
async def translategl(query):
    speak("Sure mam")
    print(googletrans.LANGUAGES)
    translator = Translator()

    # Await the translation
    text_to_translate = await translator.translate(query, src="auto", dest="hi")
    
    # Get the translated text
    text = text_to_translate.text
    print(f"Translated text: {text}")
    
    try:
        # Convert text to speech and save the file
        speakgl = gTTS(text=text, lang="hi", slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(5)
        os.remove("voice.mp3")
    except Exception as e:
        print("Unable to translate")
        print(e)

# translating a text as a example function 
def main():
    query = "translate"
    
    if "translate" in query:
        query = "hello"  # Example input to translate
        
        # Run the asynchronous translation function
        asyncio.run(translategl(query))

# after translation something  translation text with voice 
def speak(text):
    """Function to speak a given text using gTTS."""
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("voice.mp3")
    playsound("voice.mp3")
    time.sleep(1)
    os.remove("voice.mp3")
# function for news in which u want 
def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=464ecfbf36c349da888af8b33cb033f2",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=464ecfbf36c349da888af8b33cb033f2",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=464ecfbf36c349da888af8b33cb033f2",
        "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=464ecfbf36c349da888af8b33cb033f2",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=464ecfbf36c349da888af8b33cb033f2",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=464ecfbf36c349da888af8b33cb033f2"
    }

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Start listening for the field the user wants
    speak("Please tell me which field of news you want: business, entertainment, health, science, sports, or technology.")
    
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        field = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {field}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service. Please try again later.")
        return

    url = None
    for key, value in api_dict.items():
        if key in field:
            url = value
            speak(f"Found news category: {key}")
            print(f"URL: {url}")
            break
    
    if not url:
        speak("Sorry, I could not find the news category. Please try again.")
        return

    response = requests.get(url)
    news = response.json()

    if news.get("status") == "ok":
        speak("Here is the first news.")
        arts = news["articles"]
        for articles in arts:
            article = articles["title"]
            speak(f"News headline: {article}")
            print(article)
            print(f"For more info, visit: {articles['url']}")
            
            # Ask whether to continue or stop based on voice command
            speak("Press one to continue or press two to stop.")
            
            with mic as source:
                print("Listening for continue or stop command...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Command recognized: {command}")
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Stopping the news feed.")
                break
            except sr.RequestError:
                speak("Sorry, I'm having trouble connecting to the service. Stopping the news feed.")
                break
            
            if command == "2":
                speak("Stopping the news feed.")
                break
            elif command != "1":
                speak("I didn't understand that. Stopping the news feed.")
                break
    else:
        speak(f"Error fetching news: {news.get('message')}")

      

# a list of  some apps which are in system 
dictapp = {
    "commandprompt": "cmd",
    "paint": "mspaint",  
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt"
}
# temprory voice file making and after use it is remove it self 
def speak(text):
    """Function to speak a given text using gTTS."""
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("voice.mp3")
    playsound("voice.mp3")
    time.sleep(1)
    os.remove("voice.mp3")
#for opening app function
def openappweb(query):
    speak("Launching, mam")
    
    # Check if the query contains a website URL
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("kanha", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
        speak(f"Opening {query}.")
    else:
        # Check if the query contains an app name from dictapp
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}.exe")
                speak(f"{app} opened successfully.")
                return
        speak("App not found in the list.")
#for closing app function
def close_app(query):
    speak("Closing app, mam")
     # Full path to taskkill command
    taskkill_path = r"C:\Windows\System32\taskkill.exe"
    # Check if the query contains an app name from dictapp
    keys = list(dictapp.keys())
    for app in keys:
        if app in query:
            
            os.system(f"{taskkill_path} /f /im {dictapp[app]}.exe")
            
            speak(f"{app} closed successfully.")
            return
    speak("App not found to close.")
# for listening what we want to do close a app or open or exit 
def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    speak("Please tell me the application or website you want to open or close.")
    
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command recognized: {command}")
        
        # Open or close app based on the command
        if "open" in command or "launch" in command:
            openappweb(command)
        elif "close" in command:
            close_app(command)
        else:
            speak("Sorry, I didn't recognize the command.")
    
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service. Please try again later.")

# basic calculation function 
def add(x, y):
       return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
# function for clearing old tasks 
def clear_old_tasks():
    speak("Do you want to clear old tasks? Please say YES or NO")
    query = takeCommand().lower()
    if "yes" in query:
        with open("tasks.txt", "w") as file:
            file.write("")
        return True
    elif "no" in query:
        return False
    else:
        speak("Invalid response. Assuming NO.")
        return False

#function for entering new tasks 
def enter_tasks():
    tasks = []
    no_tasks = int(input("Enter the number of tasks: "))
    for i in range(no_tasks):
        task = input(f"Enter task {i+1}: ")
        tasks.append(task)
        with open("tasks.txt", "a") as file:
            file.write(f"{i+1}. {task}\n")
    return tasks
# function for scheduling day 
def schedule_day():
    tasks = []
    clear_old = clear_old_tasks()
    no_tasks = int(input("Enter the number of tasks: "))
    for i in range(no_tasks):
        task = input(f"Enter task {i+1}: ")
        tasks.append(task)
        with open("tasks.txt", "a") as file:
            file.write(f"{i+1}. {task}\n")


# api key for chatbot like interaction 
API_KEY="ddc-p7QmKYeLkG8FXMV8rSpedbSmhQ4xJ8fPWrL0KCig8d1ALrCTxW"
BASE_URL = "https://api.sree.shop/v1"

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Set speaking rate
engine.setProperty('volume', 0.9)  # Set volume

# Speak function
def speak(text):
    """
    Convert text to speech.
    """
    engine.say(text)
    engine.runAndWait()

# Voice input function
def listen():
    """
    Listen to user input via microphone and convert it to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError:
            speak("There was an issue with the speech recognition service.")
            return None
# function for chat
def chat_completion(user_input):
    """
    Generate a normal chat completion response using the OpenAI API.
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        # Extracting the response content directly
        response_message = completion.choices[0].message.content
        return response_message
    except Exception as e:
        return f"An error occurred: {e}"


# function for entering in chatbot interactiona nd doing work 
def meen():
    speak("Welcome! I am your voice assistant. How can I help you?")
    while True:
        speak("You can say 'Chat', or 'Exit' to interact with me.")
        query = listen()  # Listen for a voice command

        if query is None:
            continue  # Skip if no valid input is received

        
        elif "chat" in query:
            speak("What is your question?")
            user_input = listen()
            if user_input:
                response = chat_completion(user_input)
                print("\nChat Response:")
                print(response)
                speak("Here is my answer.")
                speak(response)

        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I didn't understand that. Please try again.")
# function for showing schedule 
def show_schedule():
    file = open("tasks.txt","r")
    content = file.read()
    file.close()
    mixer.init()
    mixer.music.load("notification.mp3")
    mixer.music.play()
    notification.notify(
        title = "My schedule :-",
        message = content,
        timeout = 15
    )
# function for sendng messages via whatsapp
def sendMessage():
    phone_number = "+91 8607565765 "#replace ph.no. as per demand

    message = "RADHE RADHE "#replace the message as per demand

    # Send message
    try:
        pywhatkit.sendwhatmsg(phone_number, message, time_hour=14, time_min=10)  # Adjust time_hour and time_min as per your requirement
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

  # start now functioning with commands...............
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "radhe radhe" in query:
            greetMe()
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok , You can call me anytime")
                    break 

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done mam")
                    speak(f"Your new password is{new_pw}")

                elif "professor details" in query:
                    print("Hello, THIS project is assist by  ASSISTANT PROFFESSOR Mr. Anil Kumar ,Professor HEAD OF DEPATMENT DOCTOR BANTA SINGH JANGRA  . It's a pleasure to meet you.")
                    
                    
                    speak("Hello, THIS project is assist by  ASSISTANT PROFFESSOR Mr. Anil Kumar ,Professor HEAD OF DEPATMENT DOCTOR BANTA SINGH JANGRA  . It's a pleasure to meet you")
                    
                    while True:
                        teacher_query = takeCommand()
                        if teacher_query == "":
                            continue
                        if teacher_query.lower() == "exit":
                            speak("Goodbye, Professor. Have a great day!")
                            break
                        elif "how are you" in teacher_query.lower():
                            speak("I'm just a program, Professor, but thank you for asking.")
                        elif "tell me a joke" in teacher_query.lower():
                            speak("Why don't scientists trust atoms? Because they make up everything!")
                        elif "what's the weather like" in teacher_query.lower():
                            speak("I'm sorry, Professor, I cannot provide real-time weather information.")
                        elif "set a reminder" in teacher_query.lower():
                            speak("Sure, what would you like to be reminded of?")
                            reminder = takeCommand()
                            if reminder != "":
                                speak(f"Reminder set for {reminder}.")
                            else:
                                speak("I'm sorry, Professor. I'm still learning and may not be able to assist with that yet.")
                                

                elif "developer details" in query:
                    speak("My developer is sonu. she created me to assist with various tasks and make life easier.")
                    speak("If you have any questions or need further assistance, feel free to ask!")

                elif "schedule my day" in query:
                
                 schedule_day()
                elif "show my schedule" in query:
                 show_schedule()

                elif "play music" in query:
                    play_music()
                    
                elif"ask gpt" in query:
                    meen()

                elif "translate" in query:
                    main()
                elif "open file" in query:
                    open_file()
                   
                elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("kanha","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")                       
                     
                elif "play a game" in query:
                  game_play()  

                elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

               
                elif "click my photo" in query:
                      pyautogui.press("super")  # Open start/search menu (Windows)
                      time.sleep(1)
                      pyautogui.typewrite("Camera")  
                      time.sleep(1)  
                      pyautogui.press("enter")  # Open Camera app
                      time.sleep(5)  # Wait for Camera app to open
                      pyautogui.press("enter")  # Take picture
                      speak("SMILE")
                      speak("Photo clicked successfully")
                elif "hello" in query:
                    speak("Hello mam, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, mam")
                elif "how are you" in query:
                    speak("Perfect, mam")
                elif "thank you" in query:
                    speak("you are welcome, mam")
                
                elif "tired" in query:
                 speak("Playing your favourite songs, ma'am")
                  # List of URLs to choose from (Example: you can replace or add more URLs)
                 urls = [
                  "https://youtu.be/30YNd5fEGMo?si=Bbs3Bown5NSc","https://youtu.be/f18cpg-mTrY?si=ZQFhG_EJuzque9eD","https://youtu.be/6ZwwapPikyQ?si=IySOi0gck0kGtwjP"
                  "https://youtu.be/Yppzo6dTpzY?si=6Uw_AZ4I9ZAJPuKG","https://youtu.be/lxKFe_1QVRA?si=n9YB6ej4TjhYLyrt"
                   # Add more URLs here if needed
                    ]
                     # Choose a URL at random
                 selected_url = random.choice(urls)
                 webbrowser.open(selected_url)

                   
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
            
                elif "volume up" in query:
                    speak("Turning volume up")
                    volumeup()

                elif "volume down" in query:
                    speak("Turning volume down")
                    volumedown()

                elif "whatsapp " in query:
                    # from Dictapp import closeappweb
                    listen_for_command()

                elif "google" in query:
                    searchGoogle(query)
                elif "youtube" in query:
                    searchYoutube(query)
                elif "wikipedia" in query:
                    searchWikipedia(query)

                elif "news" in query:
                    latestnews()

                elif "calculate" in query:
                    
                    calculator()

                elif "message" in query:
                    
                    sendMessage()
                if "close file" in query or "close application" in query:
                          close_file()

                elif "temperature" in query:
                    search = "temperature in hansi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                      
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"mam, the time is {strTime}")
                    print(strTime)
                elif "finally sleep" in query:
                    speak("Going to sleep,mam")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("kanha","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                    
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                    print("You told me to remember that" + remember.read())

                elif "search a song" in query:
                    speak("Sure, what song would you like to search for on YouTube?")
                    song_name = takeCommand()
                    search_on_youtube(song_name)
                
                elif "meeting" in query:
                    speak("Ok mam opening meeet")
                    webbrowser.open("https://meet.google.com/")

                elif "check internet speed" in query:
                    query = "check internet speed"
                    check_internet_speed()
                    speak("Here are the current internet speed metrics.")
                    print("Here are the current internet speed metrics.")

                elif "show my location" in query:
                    current_location = get_current_location()
                    print("Your current location is:", current_location)
                    speak(f"Your current location is {current_location}.")
                
                elif "generate qr code" in query:
                    speak("Sure, please provide the text or URL for the QR code.")
                    text_or_url = takeCommand().lower()
                    text_or_url=input("enter the text")
                    print(f"text or url is { text_or_url}")
                    filename = "qr_code.png"  
                    generate_qr_code(text_or_url, filename)
                    speak("QR code generated successfully.")

                elif"shutdown system"in query:
                    subprocess.call(['shutdown', '/s', '/t', '0'])