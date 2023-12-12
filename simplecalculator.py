#|_________________________________________________________________________|
#| This code was written by latunatv. GitHub: https://github.com/latunatv/ |
#|              GitHub-Profile: https://github.com/latunatv/               |
#|_________________________________________________________________________|


input("Warning! This program is a fun project and has not been bug-checked.")
input("By continuing I am aware of the mistakes! (Press ENTER to continue)")

is_addition = input("Addition: True oder False: ")

if is_addition == "True":
    summand_1 = input("Gib den Wert des 1. Summanden an: ")
    summand_2 = input("Gib den Wert des 2. Summanden an: ")
    ergebnis = int(summand_1) + int(summand_2)
    print("Das Ergebnis ist " + str(ergebnis) + ".")

else:
    is_subtraction = input("Subtraktion: True oder False: ")
    if is_subtraction == "True":
        minuent = input("Gib den Wert des Minuenden an: ")
        subtrahent = input("Gib den Wert des Subtrahenden an: ")
        ergebnis = int(minuent) - int(subtrahent)
        print("Das Ergebnis ist " + str(ergebnis) + ".")

    else:
        is_division = input("Division: True oder False: ")
        if is_division == "True":
            divident = input("Gib den Wert des Dividenden an: ")
            divisor = input("Gib den Wert des Divisoren an: ")
            ergebnis = int(divident) / int(divisor)
            print("Das Ergebnis ist " + str(ergebnis) + ".")

        else:
            is_multiplication = input("Multiplikation: True oder False: ")
            if is_multiplication == "True":
                factor_1 = input("Gib den Wert des 1. Faktors an: ")
                factor_2 = input("Gib den Wert des 2. Faktors an: ")
                ergebnis = int(factor_1) * int(factor_2)
                print("Das Ergebnis ist " + str(ergebnis) + ".")

            else:
                print("Es gibt keine weiteren Rechnungsmöglichkeiten!")
                print(" Starte das Programm neu, wenn du erneut rechnen willst!")
                input("Beliebige Taste drücken...")

#|_________________________________________________________________________|
#| This code was written by latunatv. GitHub: https://github.com/latunatv/ |
#|              GitHub-Profile: https://github.com/latunatv/               |
#|_________________________________________________________________________|
