# |_________________________________________________________________________|
# | This code was written by latunatv. GitHub-Repository: LATUNA_CODING     |
# |              GitHub-Profile: https://github.com/latunatv/               |
# |_________________________________________________________________________|

# Import
import math

# Code

print("__________________________________________________________________")
print("__________________________________________________________________")
print("Warning! This program is a fun project and has not been bug-checked.")
print("By continuing I am aware of the mistakes! (Press ENTER to continue)")
print("__________________________________________________________________")
print("__________________________________________________________________")
print("|Rechenarten: Addition, Subtraktion, Division, Multiplikation, Quadratwurzel, Potenz|")

rechenart = input("Gib die Rechenart an: ")

if rechenart == "Addition":
    summand_1 = input("Gib den Wert des 1. Summanden an: ")
    summand_2 = input("Gib den Wert des 2. Summanden an: ")
    ergebnis = float(summand_1) + float(summand_2)
    print("Das Ergebnis ist " + str(ergebnis) + ".")


if rechenart == "Subtraktion":
    minuend = input("Gib den Wert des Minuenden an: ")
    subtrahend = input("Gib den Wert des Subtrahenden an: ")
    ergebnis = float(minuend) - float(subtrahend)
    print("Das Ergebnis ist " + str(ergebnis) + ".")


if rechenart == "Division":
    dividend = input("Gib den Wert des Dividenden an: ")
    divisor = input("Gib den Wert des Divisoren an: ")
    ergebnis = float(dividend) / float(divisor)
    print("Das Ergebnis ist " + str(ergebnis) + ".")


if rechenart == "Multiplikation":
    factor_1 = input("Gib den Wert des 1. Faktors an: ")
    factor_2 = input("Gib den Wert des 2. Faktors an: ")
    ergebnis = float(factor_1) * float(factor_2)
    print("Das Ergebnis ist " + str(ergebnis) + ".")

if rechenart == "Quadratwurzel":
    zahl = float(input("Gib den Wert an, von dem die Quadratwurzel gezogen werden soll: "))
    wurzel = math.sqrt(zahl)
    print(f"Die Quadratwurzel von {zahl} ist {wurzel}.")

if rechenart == "Potenz":
    basis = input("Gib den Wert der Basis an: ")
    exponent = input("Gib den Wert der Potenz an: ")
    ergebnis = float(basis) ** float(exponent)
    print("Das Ergebnis ist " + str(ergebnis) + ".")

else:
    print("Diese Rechenart ist (noch) nicht vorhanden! / Fehler!")
print(" Starte das Programm neu, wenn du erneut rechnen willst!")
input("Beliebige Taste drücken...")

# |_________________________________________________________________________|
# | This code was written by latunatv. GitHub-Repository: LATUNA_CODING     |
# |              GitHub-Profile: https://github.com/latunatv/               |
# |_________________________________________________________________________|
