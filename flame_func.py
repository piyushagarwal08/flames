import pyttsx3
import text_to_speech as say
import sys
import cheat
import pyfiglet
def Flames(Boy,Girl):
    flamess = {"friends":"best friends always together","love":"wah wah ram ji...jodi kya banai","affectionate":"ek tarfa pyaar ki ....baat he kuch aur hoti hai,\nits the most beautiful feeling in the world","marriage":"milan abhi aadha, adhura hai...love birds","enemies":"ladai ladai maaf karo... gandhi ji ko yaad karo","sister":"bhaiya mere rakhi ka bandhan tum nibhana...hehe"}
    flames = ["friends","love","affectionate","marriage","enemies","siblings"]
    Boy = Boy.lower()
    if Boy == '-1':
        sys.exit()
    Girl = Girl.lower()
    cheat.safe(Girl,Boy)
    boy = list(Boy)
    girl = list(Girl)    

    try:
        common = [i for i in boy if i in girl]
        common = set(common)  
    except:
        print("huh...you are just friends")
        sys.exit()
    for i in common:
        boy.remove(i)
        girl.remove(i)
    total_similar = len(boy)+len(girl)
    while(len(flames)!=1):
    
        count = (total_similar%len(flames))-1
        if count>0:
            right = flames[count+1:]
            left = flames[:count]
            flames = right+left
        else:
            flames = flames[:len(flames)-1]
    print(pyfiglet.figlet_format(f"{Girl} is {flames[0]} with {Boy}"))
    say.speak(f"{Girl} is {flames[0]} with {Boy}")
    print(flamess[flames[0]])
    say.speak(flamess[flames[0]])
