# |_________________________________________________________________________|
# | This code was written by latunatv. GitHub: https://github.com/latunatv/ |
# |              GitHub-Profile: https://github.com/latunatv/               |
# |_________________________________________________________________________|


print("__________________________________________________________________")
print("__________________________________________________________________")
print("Warning! This program is a fun project and has not been bug-checked.")
print("By continuing I am aware of the mistakes! (Press ENTER to continue)")
print("__________________________________________________________________")
print("__________________________________________________________________")
print("|Rechenarten: Addition, Subtraktion, Division, Multiplikation|")

rechenart = input("Gib die Rechenart an: ")

if rechenart == "Addition":
    summand_1 = input("Gib den Wert des 1. Summanden an: ")
    summand_2 = input("Gib den Wert des 2. Summanden an: ")
    ergebnis = float(summand_1) + float(summand_2)
    print("Das Ergebnis ist " + str(ergebnis) + ".")


if rechenart == "Subtraktion":
    minuent = input("Gib den Wert des Minuenden an: ")
    subtrahent = input("Gib den Wert des Subtrahenden an: ")
    ergebnis = float(minuent) - float(subtrahent)
    print("Das Ergebnis ist " + str(ergebnis) + ".")


if rechenart == "Division":
    divident = input("Gib den Wert des Dividenden an: ")
    divisor = input("Gib den Wert des Divisoren an: ")
    ergebnis = float(divident) / float(divisor)
    print("Das Ergebnis ist " + str(ergebnis) + ".")


if rechenart == "Multiplickation":
    factor_1 = input("Gib den Wert des 1. Faktors an: ")
    factor_2 = input("Gib den Wert des 2. Faktors an: ")
    ergebnis = float(factor_1) * float(factor_2)
    print("Das Ergebnis ist " + str(ergebnis) + ".")

else:
    print("Diese Rechenart ist (noch) nicht vorhanden!")
    print(" Starte das Programm neu, wenn du erneut rechnen willst!")
    input("Beliebige Taste drücken...")
# |_________________________________________________________________________|
# | This code was written by latunatv. GitHub: https://github.com/latunatv/ |
# |              GitHub-Profile: https://github.com/latunatv/               |
# |_________________________________________________________________________|
