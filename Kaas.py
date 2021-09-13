#Deze Script is gemaakt door CodeAura (Mike)
#Lees alles even goed door.

# 𝓚𝓪𝓪𝓼 𝓠𝓾𝓲𝔃 met Python

#-----------------------------------------------------------

import time 

Geel = input("Is kaas geel (J/N): ")
time.sleep(1)
if Geel == "J":
    Gaten = input("Zitten er gaten in (J/N): ")
    if Gaten == "N":
        Duur = input("Is de kaas zo belachelijk duur? (J/N) ")
        if Duur == "J":
            print("Emmentaler")
        else:
            print("Leerdammer")
    else:
        Steen = input("Is kaas zo hard als steen? (J/N) ")
        if Steen == "N":
            print("Goudse Kaas")
        else:
            print("Parmigiano Reggiano")
else:
    blauwe = input("Heeft de kaas blauwe schimmels? (J/N) ")
    if blauwe == "N":
        Korst = input("Heeft de kaas een korst? (J/N) ")
        if Korst == "N":
            print("Mozzerella")
        else:
            print("Camemret")
    else:
        Korst2 = input("Heeft de kaas een korst? (J/N) ")
        if Korst2 == "J":
            print("Bleu de Rochebaron")
        else:
            print("Fourme D'Ambert")
        
# ----------------------------------------------------------------------