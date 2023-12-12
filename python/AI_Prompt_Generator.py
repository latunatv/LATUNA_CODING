version = input("Wähle deine Minecraft-Version: ")
command = input("Wie soll ein Command heißen? (ohne /): ")
happen = input("Was passieren soll. Format: wird..., passiert...: ")
code = input("Wenn du eine Vorlage hast, schreibe sie hier hinein. Sonst: schreibe irgendwas hier hinein: ")

#Auswahl
is_format = input("Hast du eine Vorlage für den Code?: Ja: True, Nein: False: ")

#Code


is_format = is_format == "True"

if is_format:
    print("______________________________________")
    print("")
    print("")
    print("")
    print("Erstelle mir ein Minecraft-Plugin in der Version " + version + " in Paper")
    print("Mit dem Befehl /" + command + " " + happen)
    print("Achte auf dieses Grundprnzip:")
    print("")
    print("")
    print(code)
    print("")
    print("")
    print("")
    print("______________________________________")
    print("")
    input("Drücke eine Taste, um das Programm zu beenden...")






else:
    print("______________________________________")
    print("")
    print("")
    print("")
    print("Erstelle mir ein Minecraft-Plugin in der Version " + version + " in Paper")
    print("Mit dem Befehl /" + command + " " + happen)
    print("")
    print("")
    print("")
    print("______________________________________")

    input("Drücke eine Taste, um das Programm zu beenden...")
