#import modules
import requests
import platform
import os
import sys
import subprocess
import gtts

# Define color codes for terminal output
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Error handling function
def error_handling(e):
    print("The program is not working properly, checking errors...")
    
    def check_internet_connection(url='http://www.google.com/', timeout=5):
        try:
            response = requests.get(url, timeout=timeout)
            return True
        except requests.ConnectionError:
            return False

    if check_internet_connection():
        print(bcolors.GREEN + "Internet connection is available.")
    else:
        print(bcolors.WARNING + "No internet connection.")
        print(bcolors.WARNING + "Please check your internet connection.")
        print(bcolors.FAIL + "The program is terminating...")
        sys.exit()

    if e == "ModuleNotFoundError":
        print(bcolors.FAIL + "Module not found")


# Function to get the operating system type
def get_os_type():
    os_type = platform.system()
    
    if os_type == "Linux":
        if os.path.isfile('/system/build.prop'):
            os_type = "Android"
        else:
            try:
                with open("/etc/os-release") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith("ID="):
                            os_type_dist = line.strip().split('=')[1].strip('"')
                            break
            except FileNotFoundError:
                os_type_dist = "Linux (Unknown Distribution)"
            os_type = "Linux"
    elif os_type == "Darwin":
        os_type = "MacOS"
    elif os_type == "Windows":
        os_type = "Windows"
    else:
        os_type = "Unknown"

    return os_type


# Function to handle flow based on OS type
def flowTransfer(os_type):
    if os_type == "Linux":
        redir = "Linux operating system detected, redirecting...\nStarting terminal Linux assistant program"
        linux(redir)
    elif os_type == "Android":
        aredir = "Android operating system detected, redirecting..."
        android(aredir)
        os.system("python android/welcome.py")
    elif os_type == "Windows":
        print("The operating system type: Windows")
        os.system("python android/main.py")
    else:
        print("Unknown operating system or Mac, they can't be supported.")

# Android specific functions
def android(aredir):
    def printf(c,msg):
        print(c+msg)
        subprocess.call("termux-tts-speak '{}'".format(msg), shell=True)
    printf(bcolors.HEADER, aredir)


    def toolInstall(tool):
        printf(bcolors.HEADER, tool)
        printf(bcolors.GREEN, "Select your option")
        tools = ["0) Main menu", "1) sl", "2) cowsay", "3) cmatrix"]
        for i in tools:
            print(i)
        num = int(input("Enter your option: "))
        match num:
            case 0:
                redir = "Back to main menu..."
                linux(redir)
            case 1:
                speak = "Updating Linux and installing sl package"
                printf(bcolors.GREEN, speak)
                result = subprocess.run("sudo apt update && sudo apt install sl -y", shell=True, stdout=open("output.log", "w"), stderr=open("error.log", "w"))
                if result.returncode != 0:
                    print("An error occurred. Check error.log for details.")
                else:
                    printf(bcolors.GREEN, "Installation is complete")
            case 2:
                speak = "Updating Linux and installing cowsay package"
                printf(bcolors.GREEN, speak)
                subprocess.call("touch runner.sh && chmod +x runner.sh", shell=True)
                with open("runner.sh", "w") as f:
                    f.write("apt update && apt install cowsay")
                subprocess.run("./runner.sh", shell=True, stdout=open("output.log", "w"), stderr =open("error.log", "w"))
                printf(bcolors.GREEN, "Installation is complete")
        toolInstall("Return to tools menu...")





    printf(bcolors.GREEN, "Select your option")
    tools = ["0) Exit", "1) Tools Install", "2) Voice Assistant", "3) Help (cmd details)"]
    for i in tools:
        print(i)
    opt = int(input(bcolors.GREEN + "Enter your option: "))
    match opt:
        case 0:
            printf(bcolors.FAIL, "Closing program...")
            sys.exit()
        case 1:
            print("Executing")
            tool = "Starting terminal tools install program"
            toolInstall(tool)
        case 2:
            print("Case 2: Voice Assistant functionality not implemented yet.")
    redir = ""
    android(redir)
    printf(bcolors.FAIL, "Program ended...")

# Linux specific functions
def linux(redir):
    
    def printf(c, msg):
        try:
            a1 = gtts.gTTS(msg)
            a1.save("tts2.mp3")
            print(c + msg)
            subprocess.call("mpv tts2.mp3", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except ModuleNotFoundError:
            error_handling("ModuleNotFoundError")
        except Exception as e:
            error_handling(e)

    printf(bcolors.HEADER, redir)

    # Function to install tools
    def toolInstall(tool):
        printf(bcolors.HEADER, tool)
        printf(bcolors.GREEN, "Select your option")
        tools = ["0) Main menu", "1) sl", "2) cowsay", "3) cmatrix"]
        for i in tools:
            print(i)
        num = int(input("Enter your option: "))
        match num:
            case 0:
                redir = "Back to main menu..."
                linux(redir)
            case 1:
                speak = "Updating Linux and installing sl package"
                printf(bcolors.GREEN, speak)
                result = subprocess.run("sudo apt update && sudo apt install sl -y", shell=True, stdout=open("output.log", "w"), stderr=open("error.log", "w"))
                if result.returncode != 0:
                    print("An error occurred. Check error.log for details.")
                else:
                    printf(bcolors.GREEN, "Installation is complete")
            case 2:
                speak = "Updating Linux and installing cowsay package"
                printf(bcolors.GREEN, speak)
                subprocess.call("touch runner.sh && chmod +x runner.sh", shell=True)
                with open("runner.sh", "w") as f:
                    f.write("apt update && apt install cowsay")
                subprocess.run("./runner.sh", shell=True, stdout=open("output.log", "w"), stderr =open("error.log", "w"))
                printf(bcolors.GREEN, "Installation is complete")
        toolInstall("Return to tools menu...")

    # Welcome TTS message
    printf(bcolors.GREEN, "Select your option")
    tools = ["0) Exit", "1) Tools Install", "2) Voice Assistant", "3) Help (cmd details)"]
    for i in tools:
        print(i)
    opt = int(input(bcolors.GREEN + "Enter your option: "))
    match opt:
        case 0:
            printf(bcolors.FAIL, "Closing program...")
            sys.exit()
        case 1:
            print("Executing")
            tool = "Starting terminal tools install program"
            toolInstall(tool)
        case 2:
            print("Case 2: Voice Assistant functionality not implemented yet.")
    redir = ""
    linux(redir)
    printf(bcolors.FAIL, "Program ended...")

# Function call to start the program
os_type = get_os_type()
flowTransfer(os_type)