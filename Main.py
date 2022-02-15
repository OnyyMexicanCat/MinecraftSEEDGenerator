import random
import argparse
import time
import string
from xmlrpc.client import INVALID_ENCODING_CHAR
import config as conf
startup = """
IT = Ciao e benvenuti nel mio generatore di seed minecraft creato da @OnyyTheBest questo script molto semplice vi permetterà di usare dei seed pre fatti molto carini e anche di generare dei seed, ma la chicca più importante è il fatto è che questi seed saranno visibili prima ancora della, creazione del mondo, come? beh questo lo devi scoprire tu ;D

ENG = Hello and welcome to my minecraft seed generator created by @OnyyTheBest this very simple script will allow you to use very nice pre-made seeds and also to generate seeds, but the most important gem is the fact is that these seeds will be visible even before the creation of the world, how? well this you have to find out ;D
"""
print(startup)
time.sleep(1)
selection1 = """
IT = Vuoi generare un seed o ne vuoi usare uno gia' generato?
ENG = Do you want to generate a seed or use an already generated one?
"""
Giampietro=open(("Seeds.txt"),"a")
def stop():
    stopexe = input("Press Return to continue...")
    return;
print(selection1)
print('[1] Si/yes')
print('[2] No, I want to generate it')
d1a = input ("Per favore seleziona 1 o 2 // Please select 1 or 2: ")
if d1a == "1":
    print("Ecco i seed piu' popolari! // Here are the most popular seeds!")
    print(conf.NUM1)
    print(conf.NUM2)
    print(conf.NUM3)
    print(conf.NUM4)
    print(conf.NUM5)
    print(conf.NUM6)
    print(conf.NUM7)
    print(conf.NUM8)
    print(conf.NUM9)
    print(conf.NUM10)
    print(conf.NUM11)
    print(conf.NUM12)
    print(conf.NUM13)
    print(conf.NUM14)
    print(conf.NUM15)
elif d1a == "2":
    print("Inizio la generazione // Start generation...")
    infgenerator =int(input("Quanti seed vuoi generare? // how many seeds do you want to generate?: "))
    if infgenerator == 0:
        print("New Random Seeds:")
        print("")
        ilporcodio = [random.randint(-9223372036854775807,9223372036854775807) for ran in range (0,10)]
        print(ilporcodio + "Made with love by @OnyyTheBest")
        print(f"https://www.chunkbase.com/apps/seed-map#{ilporcodio}")
        stop()
    else:
        for n in range(int(infgenerator)):
            ildioghane = "".join(random.choices(
                                    string.digits,
                                    k = 14))
            ildioghane2 = "".join(random.choices(
                                string.digits,
                                    k = 14))
            oronzo =f"https://www.chunkbase.com/apps/seed-map#{ildioghane}"
            oronzo1 = f"https://www.chunkbase.com/apps/seed-map#{step}"
            step = "-" + ildioghane2
            print(ildioghane)
            print(oronzo)
            Giampietro.write(ildioghane + "\n")
            print(step)
            Giampietro.write(step + "\n")
            print(oronzo1)
        print("Gen by @OnyyTheBest \n")
        Giampietro.close()
    print("Vuoi salvare i link? // Do you want to save links?")
    print('[1] Si/yes')
    print('[2] No.')
    d1a2 = input ("Per favore seleziona 1 o 2 // Please select 1 or 2: ")
    if d1a2 == '1':
        for n in range(int(infgenerator)):
            f=open(("Links.txt"), "a")
            f.write(oronzo + "\n")
            f.write(oronzo1 + "\n")
        f.close
    elif d1a2 == '2':
        input("\n\nPremi enter e il programma si chiudera' automaticamente//Press enter until the program closes automatically")
    else:
        print("tasto sbagliato :D // Wrong button :D")