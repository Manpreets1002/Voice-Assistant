import eel
import os
from commands import *
def start_first():
    eel.init("Front End")

    os.system('start msedge.exe --app="http://localhost:8000/main.html"')

    eel.start('main.html', mode=None ,host="localhost", block = True)