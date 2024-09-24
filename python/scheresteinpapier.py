# |_________________________________________________________________________|
# | This code was written by latunatv. GitHub-Repository: LATUNA_CODING     |
# |              GitHub-Profile: https://github.com/latunatv/               |
# |_________________________________________________________________________|


import random

print("************************************")
print("       Schere - Stein- Papier       ")
print("************************************")

liste_game = ["Schere", "Stein", "Papier"]

def game():
    rndm_pick = random.choice(liste_game)

    my_pick = input("Schere, Stein, Papier: ")

    global counter

    # _________________________________________________________________________________________
    if my_pick == "Schere":
        if rndm_pick == "Schere":
            print("UNENTSCHIEDEN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)

        elif rndm_pick == "Stein":
            print("VERLOREN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)
            counter = counter - 1

        elif rndm_pick == "Papier":
            print("GEWONNEN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)
            counter = counter + 1

    # _________________________________________________________________________________________
    elif my_pick == "Stein":
        if rndm_pick == "Schere":
                print("GEWONNEN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)
                counter = counter + 1

        elif rndm_pick == "Stein":
                print("UNENTSCHIEDEN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)

        elif rndm_pick == "Papier":
                print("VERLOREN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)
                counter = counter - 1

     #_________________________________________________________________________________________
    elif my_pick == "Papier":
        if rndm_pick == "Schere":
                print("VERLOREN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)
                counter = counter - 1

        elif rndm_pick == "Stein":
                print("GEWONNEN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)
                counter = counter + 1

        elif rndm_pick == "Papier":
                print("UNENTSCHIEDEN! Eingabe: " + my_pick + ". COM-Eingabe: " + rndm_pick)

    # _________________________________________________________________________________________
    else:
        print("FEHLER! Falsche Eingabe!")
    # _________________________________________________________________________________________

def points():
    global counter
    if counter < 0:
        counter = 0
    print(counter)


counter = 0
while True:
    game()
    points()


# |_________________________________________________________________________|
# | This code was written by latunatv. GitHub-Repository: LATUNA_CODING     |
# |              GitHub-Profile: https://github.com/latunatv/               |
# |_________________________________________________________________________|
