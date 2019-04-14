import text_to_speech as say
import sys
import random
def safe(Girl,Boy):
    dialogues = ["best friends always together","bhaiya mere rakhi ke bandhan ko nibhana","yeee dosti..hum nahi todenge","born rivals","both hates each other","kumbh ke mele main bichde hue bhai bhen"]
    if(Girl == "harshita sharma" and Boy != "piyush agarwal"):
        dialogue = random.choice(dialogues)
        print(dialogue)
        say.speak(dialogue)
        sys.exit()
        
