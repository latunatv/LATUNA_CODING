import getpass
import platform
import os
import socket
import subprocess
benutzername = getpass.getuser()
print("Ocolomate CP [Version 1.0 (beta)](c) Ocolomate. Alle Rechte vorbehalten.")
path = f"C:/Users/{benutzername}>"

def command():
    global path, benutzername
    command = input(path)

    if command == "help":
        print("")
        print("COMMAND-LIST:")
        print("- help | Provides information")
        print("- current_user | Displays the current username")
        print("- system_info | Shows information about the operating system")
        print("- list_files | Lists files in the current directory")
        print("- get_ip | Displays the computer's IP address")
        print("- show_env | Shows environment variables")
        print("- open_folder | Opens the current directory in File Explorer")
        print("- list_processes | Lists running processes")
        print("- network_info | Shows network information")
        print("- system_time | Displays current system time")
        print("")


    elif command == "current_user":
        try:
            username = getpass.getuser()
            print(f"Current User: {username}")
        except Exception as e:
            print(f"Error retrieving username: {e}")

    elif command == "system_info":
        system_info = platform.system()
        release_info = platform.release()
        architecture_info = platform.architecture()
        print(f"Operating System: {system_info}")
        print(f"Version: {release_info}")
        print(f"Architecture: {architecture_info}")

    elif command == "list_files":
        current_directory = os.getcwd()
        files = os.listdir(current_directory)
        print(f"Files in the current directory ({current_directory}):")
        for file in files:
            print(file)

    elif command == "get_ip":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")

    elif command == "show_env":
        environment_variables = os.environ
        print("Environment Variables:")
        for variable, value in environment_variables.items():
            print(f"{variable}: {value}")

    elif command == "open_folder":
        current_directory = os.getcwd()
        os.system(f"start explorer {current_directory}")

    elif command == "list_processes":
        result = subprocess.check_output("tasklist", shell=True, text=True)
        print("List of Running Processes:")
        print(result)

    elif command == "network_info":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")

    elif command == "system_time":
        current_time = subprocess.check_output("time /t", shell=True, text=True)
        print(f"Current System Time: {current_time.strip()}")


    else:
        print("ERROR! This command is not existing!")
while True:
    command()

