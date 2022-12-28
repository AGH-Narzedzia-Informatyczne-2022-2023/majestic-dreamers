import os
import platform

def main():
    if platform.system() == 'Windows':
        os.system('./wonsz3D/MegoWonsz9.exe')
    else:
        os.system('cd ./wonsz3D && bottles ./MegoWonsz9.exe')
