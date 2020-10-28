# variabelen 
# input()
# print()

 

# Doel: Voornaam en achternaam kunnen invoeren. Het programma weergeeft de volledige naam.

 

Score = 0
import time

 

print("Hello You!, ik ben Alex Marquez")
print("Wie ben jij?")
voornaam = input()

 

print("")

 

print("Hello" + " " + voornaam)

 

print("")

 

print("Ik ben een nieuwkomer op het Mediacollege Amsterdam")
print("Door een aantal vragen over mij te beantwoorden leer je mij beter kennen.")

 

print("")
print("")
time.sleep(3)

 

# Vraag 1
antwoord1 = input("Hoe oud ben ik? \na 19 jaar \nb 20 jaar \nc 21 jaar \nd 22 jaar \nAnswer: ")
if antwoord1 == "b" or antwoord1 == "20 jaar" or antwoord1 == "B":
    Score +=1
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is B (16)")
    print("Score: ", Score)
    print("\n")

 

time.sleep(1)

 

# Vraag 2
antwoord2 = input("Hoelang duurde me vorige opleiding? \na 2 jaar \nb 3 jaar \nc 4 jaar \nd 5 jaar \nAnswer: ")
if antwoord2 == "a" or antwoord2 == "2 jaar" or antwoord2 == "A":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is A (2 jaar)")
    print("Score: ", Score)
    print("\n")

 

time.sleep(1)

 

# Vraag 3
antwoord2 = input("Wat is mijn favoriete kleur? \na Groen \nb Goud \nc Blauw \nd Rood \nAnswer: ")
if antwoord2 == "c" or antwoord2 == "Blauw" or antwoord2 == "C":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is C (Aqua)")
    print("Score: ", Score)
    print("\n")

 

time.sleep(1)

 

# Vraag 4
antwoord2 = input("Wat is mijn favoriete game? \na Fortnite \nb Rocket League \nc Avenger Game \nd GTA 5 \nAnswer: ")
if antwoord2 == "c" or antwoord2 == "Avenger Game" or antwoord2 == "C":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is C (Avenger Game)")
    print("Score: ", Score)
    print("\n")

 

print("")
time.sleep(1)

 

# Vraag 5
antwoord2 = input("Welk muziek artiest luister ik naar? \na The Weeknd \nb Aminam \nc Avicii \nd Pitbull \nAnswer: ")
if antwoord2 == "d" or antwoord2 == "Pitbull" or antwoord2 == "D":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is D (Pitbull)")
    print("Score: ", Score)
    print("\n")


# Eind score
print("Wil je nog een vraag over mij voor meer punten? (nee) (ja)")

 

if input() == "ja":
    time.sleep(1)
    print("")
    antwoord6 = input("Wat is mijn lievelings serie op Netflix? \na KobraKai \nb La Casa del Papel \nc Umbrella Academy \nd The Flash \nAnswer: ")
    if antwoord6 == "b" or antwoord6 == "La Casa del Papel" or antwoord6 == "B" or antwoord6 == "La Casa del Papel":
        Score +=1
        print("Goed!")
        print("")
        print("Jouw eind score is: ", Score) 
    else:
        Score -=1
        print("Niet goed! Het antwoord is B (La Casa del Papel)")
        print("")
        print("Jouw eind score is: ", Score)

 

else:
    print("Jouw eind score is: ", Score)

   
