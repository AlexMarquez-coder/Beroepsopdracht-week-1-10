import time


# hier worden de functions 
def verhaalstukje1():
    print("Hallo mijn naam Naya ik ben 11 jaar en woon in Syrië")
    print ("A. Naar buiten gaan")
    print ("B. Binnen blijven")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A":
        verhaalstukje2()
        # naar buiten
    elif antwoord=="B":
        verhaalstukje3() # binnen blijven
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje1()


def verhaalstukje2():
    print("")
    print("Naar buiten gaan")
    print ("A. Kijken waar de schoten van daan komen")
    print ("B. Vluchten")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A":
        verhaalstukje4() # buiten is een oorlog gaande 
    elif antwoord=="B":
        verhaalstukje5() # binnen blijven
    else:
        print("Je kunt alleen antwoorden met A of B.")

def verhaalstukje4():
    print("")
    print("Je bent gespot")
    print("")
    time.sleep(1)
    Verhaal4 = input("Game over")
    


def verhaalstukje5():
    print("")
    print ("Vluchten")
    print ("A. Middag")
    print ("B. Avond")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A":
        verhaalstukje8()
        # naar buiten
    elif antwoord=="B":
        verhaalstukje11() # binnen blijven
    else:
        print("Je kunt alleen antwoorden met A of B.")
        
def verhaalstukje8():
    print("")
    print("Je bent gespot")
    print("")
    time.sleep(1)
    Verhaal8 = input("Game over")

def verhaalstukje3():
    print("")
    print("Binnenen blijeven")
    print("")
    print("Bellen voor hulp")
    time.sleep(1)
    verhaalstukje16()


def verhaalstukje11():
    print("")
    print ("Avond, hoe ga je?")
    print ("A. Auto")
    print ("B. Lopen")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A":
        verhaalstukje13()
        # naar buiten
    elif antwoord=="B":
        verhaalstukje15() # binnen blijven
    else:
        print("Je kunt alleen antwoorden met A of B.")
        
        
def verhaalstukje13():
    print("")
    print("Je gaat autorijden")
    print("Je bent gespot ")
    print("")
    time.sleep(1)
    Verhaal8 = input("Game over")
    
def verhaalstukje15():
    print("")
    print("Lopen ")
    print("")
    print("Je bent op de grens van de Turkije")
    time.sleep(1)
    print("")
    print("Je zit in het vleigtuig naar Amsterdam")
    time.sleep(1)
    print("")
    Verhaal4 = input("Je bent in veilig Nederland")
    time.sleep(1)
    

def verhaalstukje16():
    print("")
    print("Je hebt geen electriciteit wil je poberen te vluchten of het optegeven")
    print ("A. vluchten")
    print ("B. opgeven")
    verhaal10 = input("Maak een keuze, A of B? ")
    if verhaal10 == "A":
        print("")
        verhaalstukje5()
    elif verhaal10 == "B":
        print("Opgeven en niks doen")
    

# hier start de  main
verhaalstukje1()
