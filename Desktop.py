import os
import getpass
from sys import platform

username = getpass.getuser()
if platform == 'win32':
    print(os.listdir(f'C:\\Users\\{username}\\Desktop'))
elif platform == "linux" or platform == "linux2":
    print(os.listdir(f'/home/{username}/Desktop'))
elif platform == "darwin":
    print(os.listdir(f'/Users/{username}/Desktop'))
else:
    print('OS not recognized')