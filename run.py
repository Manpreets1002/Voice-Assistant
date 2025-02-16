import multiprocessing
import multiprocessing.process
from main import start_first,intro

def introduction():
    print("Process 3 is Running")
    intro()

def start():
    print("Process 1 is Running")
    start_first()

def hotword_detect():
    print("Process 2 is running")
    from features_VA.helper import hotword
    hotword()
    

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=start)
    p2 = multiprocessing.Process(target=hotword_detect)
    p3 = multiprocessing.Process(target=introduction)
    from commands import intro
    p1.start()
    p2.start()
    p3.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()
    if p3.is_alive():
        p3.terminate()
        p3.join()

    print("System Stop")