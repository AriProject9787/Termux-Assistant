import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(2)
print("\033[95m You said: ",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please tell something sir"])
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()

#chat........

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir "])
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistanct Termux, sir"])
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me termux "])
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","made by Arirama selvam ,India,tamilnadu "])
     elif "I love you" in inp:
         subprocess.call(["termux-tts-speak","i love you to sir "])
     elif "how old are" in inp:
         subprocess.call(["termux-tts-speak","just two thousend year "])
     elif "who is harish " in inp:
         subprocess.call(["termux-tts-speak","ari rama selvam nick name is harish, he made me in 2022 november 5th, he is my god because he made me, i love him "])
     elif "hii " in inp:
         subprocess.call(["termux-tts-speak","yes sir how can i help you"])
     elif "your favourite time" in inp:
         subprocess.call(["termux-tts-speak","speaking with you sir "])
     elif "good " in inp:
         subprocess.call(["termux-tts-speak"," hello sir , how are you "])
    











 # testing...  
     elif "clear" in inp:
         subprocess.call(["clear"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 1 minute"])
         time.sleep(60)
     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")      
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")

#termux api

     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
     elif "Wi-Fi info" in inp:
         subprocess.call(["termux-wifi-scaninfo"])
     elif "camera info" in inp:
         subprocess.call(["termux-camera-info"])
     elif "call log" in inp:
         subprocess.call(["termux-call-log"])
     elif "contact list" in inp:
         subprocess.call(["termux-contact-list"])
     elif "date" in inp:
         a = subprocess.getoutput(["date"])
         subprocess.call(["termux-tts-speak",a])
     elif "call name" in inp:
         os.system("termux-telephony-call +91")
     elif "call name" in inp:
         os.system("termux-telephony-call +91")
     elif "enable torch" in inp:
         os.system("termux-torch on")
     elif "disable torch" in inp:
         os.system("termux-torch off")
     elif "enable Wi-Fi" in inp:
         os.system("termux-wifi-enable true")
     elif "disable Wi-Fi" in inp:
         os.system("termux-wifi-enable false")
     elif "vibrate" in inp:
         subprocess.call(["termux-vibrate"])
     elif "send SMS name" in inp:
         os.system("termux-sms-send -n +91 hi ")
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     else:
       subprocess.call(["termux-tts-speak","not cooded for that"])

system()

os.system("python main.py")