from __future__ import unicode_literals
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
# for message
import urllib.request
import urllib.parse
# for youtube  vedio download
import youtube_dl
# for instagram sent message
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as Ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am FRIDAY sir  Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None" 
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query      
# wikipedia
        if 'wikipedia' in query:
            speak('searching wikipedia...') 
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
# open web platform  
        elif 'open chrome' in query:
            speak("opening chrome")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            
        elif 'close chrome' in query:
            speak("closing")
            os.system("TASKKILL /F /IM chrome.exe")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("www.google.com")

        elif 'open amazon' in query:
            speak("opening amazon")
            webbrowser.open("amazon.in")

        elif 'open gmail' in query:
            speak("opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")
# search platform
        elif 'google search about' in query:
            speak('searching on google...') 
            query = query.replace("google search about", "")
            webbrowser.open(f'https://www.google.com/search?q={query}')
        
        elif 'youtube search about' in query:
            speak('searching on youtube...') 
            query = query.replace("youtube search about", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

        elif 'facebook search about' in query:
            speak('searching on facebook...') 
            query = query.replace("facebook search about", "")
            webbrowser.open(f'https://www.facebook.com/search/top/?q={query}')

        elif 'instagram search about' in query:
            speak('searching on instagram...') 
            query = query.replace("instagram search about", "")
            webbrowser.open(f'https://www.instagram.com/{query}')

        elif 'pininterest search about' in query:
            speak('searching on pininterest...') 
            query = query.replace("pininterest search about", "")
            webbrowser.open(f'https://in.pinterest.com/search/pins/?q={query}')

        elif 'search all about' in query:
            speak('searching on ...') 
            query = query.replace("search all about", "")
            webbrowser.open(f'https://www.google.com/search?q={query}')
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            webbrowser.open(f'https://www.facebook.com/search/top/?q={query}')
            webbrowser.open(f'https://www.instagram.com/{query}')
            webbrowser.open(f'https://in.pinterest.com/search/pins/?q={query}')    
# movie downloader
        elif 'open movies downloader' in query:
            speak("opening 9 x movies")
            webbrowser.open("https://9xmovies.stream")
            
        elif 'open fullmovies downloader' in query:
            speak("opening full movies")
            webbrowser.open("https://khatrimazafull.cam")
# music downloader
        elif 'open music downloader' in query:
            speak("opening m p 3 downloader")
            webbrowser.open("https://www.mp3juices.cc/")
# vedio downloader
        elif 'open video downloader' in query:
            speak("opening vedio downloader")
            link = input("paste the link here : ")
            ydl_opts = {}
            os.chdir('C:\\Users\\admin\\Downloads')
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print("vedio dowloaded succesfully")  
# time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            srt2time = datetime.datetime.now().strftime("%A %B %d %Y")
            print(strTime)
            print(srt2time)
            speak(f"Sir , the time is {strTime}")
            speak(srt2time)
# send mail
        elif 'send mail' in query:
            try:
                speak("whom do you want to send mail")
                to2 = input()
                to = (f"{to2}@gmail.com")
                print(to)
                speak("What should i say?")
                content = takeCommand()
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                # print(e)
                speak("Retry")
# play song 
        elif 'play song' in query:
            import music
# climate
        elif 'climate' in query:
            print("speak your city name")
            speak("speak your city name")
            query = takeCommand().lower()
            if query == 'none':
                query = takeCommand().lower()
            driver = webdriver.Chrome()
            driver.get(f"https://www.google.com/search?q=weather+forecast+{query}&rlz=1C1CHBD_enIN838IN838&oq=weather+forc&aqs=chrome.2.69i57j0l5.15716j0j7&sourceid=chrome&ie=UTF-8")
            forcast = driver.find_element_by_class_name("wob_dcp").text
            forcast1 = driver.find_element_by_class_name("Ab33Nc").text
            driver.quit()
            forcast2 = forcast1.replace("C | °F", "celcius")
            print(forcast2)
            speak(f"According to trusted department it is {forcast2} and {forcast} today")
# sent instagram message
        elif 'send message to' in query:
            instafriend ={
                        "tanmay":"tanmay.13__", 
                        "jayesh":"jaychoudhary125", 
                        "lucky":"_pratham._._", 
                        "rohit":"rohit14_10_4", 
                        "aditya":"_.mr_satav",
                        "disha":"dishashinde36", 
                        "ananya":"_ananya_21_28",
                        "utkarsh":"_.utkarsh._04",
                        "manorama":"manorama_01_09_95",
                        "chaitanya":"chaitanyaxsakat",
                        "sairaj":"sairajchore_456",
                        "yogesh":"madhavyogesh451",
                          }
            query = query.replace("send message to","")
            if query == 'none':
                speak("speak person you want to send message")
                query = takeCommand().lower()

            if query == 'input':
                speakuser = takeCommand().lower()

            if query == 'input':
                query = input("enter username : ")

            usern = instafriend[query]
            speak("speak the message")
            message_ = takeCommand().lower()
            if message_ == 'none': 
                message_ = takeCommand().lower()

            if message_ == 'input': 
                message_ = input("enter your message : ")

            class bot:
                def __init__(self, username, password, user, message):
                    self.username = username
                    self.password = password
                    self.user = user
                    self.message =  message
                    self.base_url = 'https://www.instagram.com/'
                    self.bot = webdriver.Chrome()
                    self.login()


                def login(self):
                    self.bot.get(self.base_url)
                    
                    enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
                    enter_username.send_keys(self.username)
                    enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
                    enter_password.send_keys(self.password)
                    enter_password.send_keys(Keys.RETURN)
                    notnow = WebDriverWait(self.bot,20).until(Ec.presence_of_element_located((By.CLASS_NAME, 'cmbtv')))
                    a = notnow.find_elements_by_tag_name("button")[0]
                    action = ActionChains(self.bot)
                    action.click(a)
                    action.perform()
                    not_now = WebDriverWait(self.bot,20).until(Ec.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
                    b = not_now.find_elements_by_tag_name("button")[1]
                    actions = ActionChains(self.bot)
                    actions.click(b)    
                    actions.perform()
                    time.sleep(1)
                    self.bot.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
                    time.sleep(1)
                    self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
                    time.sleep(1)
                    self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(self.user)
                    time.sleep(1)
                    self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
                    time.sleep(1)
                    self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click()
                    time.sleep(1)
                    self.bot.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(self.message)
                    time.sleep(1)
                    self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                    self.bot.quit()
                    
            def init():     
                bot('tanmay.13__', '99136611', usern, message_)
                print(f"successfully sent\n message : {message_}\n to {usern}")
                speak("message successfully sent!")
                
            init()
            # tanmay.13__
# tease
        elif 'teaser' in query:
            IN = 20*input()
            speak(IN)

        elif 'thank you jarvis' in query:
            speak("no sir ")
            speak("it's my work")

        elif 'exit' in query:
            print("Good Bye sir .Thank you for giving your time!")
            speak("Good Bye sir Thank you for giving your time!")
            # speak("and don't forgot that pratham")
            # speak("i am created by tanmay")
            exit()
'''   
#message
        elif 'send message' in query:
            num = input("Enter your phone : ")
            print("speak the message")
            speak("speak the message")
            msg = takeCommand()
            def sendSMS(apikey, numbers, sender, message):
                data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender})
                data = data.encode('utf-8')
                request = urllib.request.Request("https://api.textlocal.in/send/")
                f = urllib.request.urlopen(request, data)
                fr = f.read()
                return(fr)

            resp =  sendSMS('apikey', f'{num}','TXTLCL', f'{msg}')
            print (resp)
            speak("Message sent successfully!")
'''
