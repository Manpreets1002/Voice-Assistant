import features_VA.features as oc
import time
import humingbird.resources as hr
import eel

labels = ["open","play youtube","youtube","google","vs code","whatsapp","search","google search"]
open_com = ["google","youtube","google collab","drive","leetcode","gmail","whatsapp","xbox","onedrive","vs code"]

def intro():
    oc.intro_speak("Hello My name is Jarvis &")
    oc.intro_speak("I'll be assisting you today")
    oc.intro_speak("I can play songs on youtube, can open apps on your desktop & answer any question")
    oc.intro_speak("What command do you wanna give?")

@eel.expose
def all_commands(msg = 1):
    if msg == 1:
        query = None
        while query == None:
            query = oc.query_creation()
        print("You said:",query)
    else:
        query = msg
        eel.Displaymsg(query)
        
    query = query.lower()

    prediction = hr.Text.predict(
        text = query,
        labels = labels
    )

    max_score = 0

    for val in prediction:
        if val["score"] > max_score:
            max_score = val["score"]
            max_val_text = val["className"]

    if max_val_text == "open" or max_val_text == "play youtube":
        inside_pred = hr.Text.predict(
            text = query,
            labels = open_com
        )
        max_score = 0

        for val in prediction:
            if val["score"] > max_score:
                max_score = val["score"]
                max_val_txt = val["className"]
            
        if max_val_txt == "play youtube":
            oc.PlayYoutube(query)
        else:
            oc.opencom(query)


    elif "exit" == query:
        oc.speaking("Thank You")
        oc.speaking("See you again")

    elif "google search" == max_val_text or "search" == max_val_text:
        oc.speaking("Finding")
        oc.search_query(query)

    else:
        oc.speaking("Not Run")
