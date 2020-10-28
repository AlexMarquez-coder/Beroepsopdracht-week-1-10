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
    print("Je bent gespot")
    print("")
    time.sleep(1)
    Verhaal4 = input("Game over")
    


def verhaalstukje5():
    print ("vluchten")
    print ("A. middag")
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
    print(" je bent gespot ")
    print("")
    time.sleep(1)
    Verhaal8 = input("Game over")
        


def verhaalstukje11():
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
    print("autorujdeN")
    print(" je bent gespot ")
    print("")
    time.sleep(1)
    Verhaal8 = input("Game over")
    
def verhaalstukje15():
    print("Lopen ")
    print("")
    print("Je bent op de grens van de Turkaje")
    time.sleep(1)
    print("Je zit in het vleigtuig naar Amsterdam")
    Verhaal4 = input("Je bent in veilig NedrelandS")
    
def verhaalstukje20(): # geen elektriciteit
    print("geeen elektriciteti ")
    print("")
    verhaalstukje5()
    

# hier start de  main
verhaalstukje1()
