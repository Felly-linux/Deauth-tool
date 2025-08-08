from Deauth import deauth_interface
import os
from colorama import Fore
from time import sleep 
print(Fore.RED +"DO NOT CLOSE THIS WINDOWS, IF YOU CLOSE IT THE ATTACK MIGHT FAIL")
sleep(3)
os.system("sudo airodump-ng start ", deauth_interface)
os.system("sudo airodump-ng ", deauth_interface)