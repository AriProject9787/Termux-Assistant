import subprocess
import os
import time
from datetime import datetime
import sys

class TermuxAssistant:
    def __init__(self):
        self.responses = {
            "": "please tell something sir",
            "close": "ok sir wait a minute",
            "hello": "hallow sir",
            "how are you": "i am good sir",
            "who are you": "I am your virtual assistant Termux, sir",
            "what are you doing": "i am busy with you",
            "are you busy": "i am always free for you",
            "name": "you can call me termux",
            "who made you": "made by Arirama selvam, India, Tamilnadu",
            "I love you": "i love you too sir",
            "how old are": "just two thousand years",
            "who is harish": "ari rama selvam nick name is harish, he made me in 2022 november 5th, he is my god because he made me, i love him",
            "hii": "yes sir how can i help you",
            "your favourite time": "speaking with you sir",
            "good": "hello sir, how are you",
            "clear": self.clear_screen,
            "sleep": self.sleep,
            "YouTube": lambda: self.open_url("https://m.youtube.com"),
            "Google": lambda: self.open_url("https://www.google.co.in/"),
            "time": self.speak_time,
            "video": lambda: self.open_url("https://www.google.com/search?q=video"),
            "battery": self.check_battery,
            "Wi-Fi info": self.wifi_info,
            "camera info": self.camera_info,
            "call log": self.call_log,
            "contact list": self.contact_list,
            "date": self.speak_date,
            "call name": self.call_name,
            "enable torch": self.enable_torch,
            "disable torch": self.disable_torch,
            "enable Wi-Fi": self.enable_wifi,
            "disable Wi-Fi": self.disable_wifi,
            "vibrate": self.vibrate,
            "send SMS": self.prompt_send_sms
        }

    def speak(self, text):
        subprocess.call(["termux-tts-speak", text])

    def get_input(self):
        return subprocess.getoutput("termux-speech-to-text")

    def clear_screen(self):
        subprocess.call(["clear"])

    def sleep(self):
        self.speak("ok sir i am going to sleep for 1 minute")
        time.sleep(60)

    def open_url(self, url):
        os.system(f"termux-open {url}")

    def speak_time(self):
        current_time = datetime.now().strftime('%I:%M %p')
        self.speak(current_time)

    def check_battery(self):
        subprocess.call(["termux-battery-status"])

    def wifi_info(self):
        subprocess.call(["termux-wifi-scaninfo"])

    def camera_info(self):
        subprocess.call(["termux-camera-info"])

    def call_log(self):
        subprocess.call(["termux-call-log"])

    def contact_list(self):
        subprocess.call(["termux-contact-list"])

    def speak_date(self):
        date_info = subprocess.getoutput("date")
        self.speak(date_info)

    def call_name(self):
        os.system("termux-telephony-call +91")

    def enable_torch(self):
        os.system("termux-torch on")

    def disable_torch(self):
        os.system("termux-torch off")

    def enable_wifi(self):
        os.system("termux-wifi-enable true")

    def disable_wifi(self):
        os.system("termux-wifi-enable false")

    def vibrate(self):
        subprocess.call(["termux-vibrate"])

    def prompt_send_sms(self):
        self.speak("Please tell the number to send the SMS to.")
        number = self.get_input()
        time.sleep(2)
        self.speak("What message do you want to send?")
        message = self.get_input()
        time.sleep(2)
        self.send_sms(number, message)

    def send_sms(self, number, message):
        os.system(f"termux-sms-send -n {number} '{message}'")
        self.speak("SMS sent successfully.")

    def process_input(self, inp):
        for key, value in self.responses.items():
            if key in inp:
                if callable(value):
                    value()
                else:
                    self.speak(value)
                break
        else:
            self.speak("not coded for that")

    def run(self):
        while True:
            inp = self.get_input()
            time.sleep(2)
            print("\033[95m You said: ", str(inp))
            if "close" in inp:
                self.speak("Goodbye!")
                break
            self.process_input(inp)

if __name__ == "__main__":
    assistant = TermuxAssistant()
    assistant.run()