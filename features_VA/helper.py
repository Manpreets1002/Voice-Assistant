import re
import pvporcupine
import pyaudio
import struct
import features_VA.features as oc
import time

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None

def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        KEYWORD = ["jarvis"]
        porcupine = pvporcupine.create(keywords=["jarvis"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate = porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h"*porcupine.frame_length,keyword)

            keyword_index = porcupine.process(keyword)
            
            if keyword_index >= 0:
                detect_key = KEYWORD[keyword_index]
                print("Hotword detected:",detect_key)
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
     
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
        if porcupine is not None:
            porcupine.delete()