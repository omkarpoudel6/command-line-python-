import random
import sys

def takeinput():
    command=input(">")
    checking_command(command)

def checking_command(command):
    if command=="help":
        help()
    elif command=="checkip":
        checkip()
    elif command=="banner":
        banner()
    elif command=="testcon":
        testcon()
    elif command=="credir":
        credir()
    elif command=="crefile":
        crefile()
    elif command=="remdir":
        remdir()
    elif command=="remfile":
        remfile()
    elif command=="openurl":
        openurl()
    elif command=="traceip":
        traceip()
    elif command=="devip":
        devip()
    elif command=="exit":
        sys.exit()


def devip():
    print("Displays all the devices ip address connected to the network")
    takeinput()

def traceip():
    print("This command will trace the specified ip")
    takeinput()

def openurl():
    print("This command will open the specified site in the default web browser")
    takeinput()

def remfile():
    print("This command will delete a file from the specified location")
    takeinput()

def remdir():
    print("This command will delete a directory from the specified location")
    takeinput()

def crefile():
    print("This command will create a file in specified location")
    takeinput()

def help():
    print("This command will show all the available command in this command line")
    print("Commands               Descriptions")
    print("\n")
    print("help                   Displays all the available commands with their description")
    print("credir                 Creates directory in specified location")
    print("crefile                Creates a file in specified location")
    print("remdir                 Deletes a directory from the specified location")
    print("remfile                Deletes a file from the specified location")
    print("openurl                Opens the specified site in the default web browser")
    print("traceip                Traces the specified ip")
    print("checkip                Displays ip address of the device")
    print("banner                 Displays different background pic each time we type this command")
    print("testcon                Checks whether there is internet connection or not")
    print("devip                  Displays all the devices ip address connected to the network")
    takeinput()

def checkip():
    print("This command will display ip address of the device")
    takeinput()


def testcon():
    print("This command will check whether there is internet connection or not")
    takeinput()

def credir():
    print("This command will create directory in specified location")

def first():
    print("################################################################################################")
    print("                                     Welcome to Command Line                                    ")
    print("\n")
    print("######  #####     #     #           #       #     #     #       ######  #####  #       ")
    print("#    #  #       #   #   #           #   #   #   #   #   # #     #    #    #    # #     ")
    print("#    #  #      #     #  #           #   #   #  #     #  #  #    #    #    #    #  #    ")
    print("#    #  #      #     #  #           #   #   #  #     #  #   #   #    #    #    #   #   ")
    print("######  #####  #######  #           #   #   #  #######  #    #  ######    #    #    #  ")
    print("# #     #      #     #  #           #       #  #     #  #   #   # #       #    #   #   ")
    print("#  #    #      #     #  #           #       #  #     #  #  #    #  #      #    #  #    ")
    print("#   #   #      #     #  #           #       #  #     #  # #     #   #     #    # #     ")
    print("#    #  #####  #     #  #####       #       #  #     #  #       #    #  #####  #       ")
    print("\n")
    takeinput()

def banner():
    #print("This command will display different banner each time we type this command")
    rand=random.randint(0,12)
    if rand==0:
        print("\n")
        print("######  #####     #     #           #       #     #     #       ######  #####  #       ")
        print("#    #  #       #   #   #           #   #   #   #   #   # #     #    #    #    # #     ")
        print("#    #  #      #     #  #           #   #   #  #     #  #  #    #    #    #    #  #    ")
        print("#    #  #      #     #  #           #   #   #  #     #  #   #   #    #    #    #   #   ")
        print("######  #####  #######  #           #   #   #  #######  #    #  ######    #    #    #  ")
        print("# #     #      #     #  #           #       #  #     #  #   #   # #       #    #   #   ")
        print("#  #    #      #     #  #           #       #  #     #  #  #    #  #      #    #  #    ")
        print("#   #   #      #     #  #           #       #  #     #  # #     #   #     #    # #     ")
        print("#    #  #####  #     #  #####       #       #  #     #  #       #    #  #####  #       ")
        print("\n")
        takeinput()

    elif rand==1:
        print("\n");
        print("######     #     #     #  ######  ######  ")
        print("#    #   #   #   #  #  #  #    #  #       ")
        print("#    #  #     #  #  #  #  #    #  #       ")
        print("#    #  #     #  #  #  #  #    #  #       ")
        print("######  #######  #  #  #  #    #  ######  ")
        print("# #     #     #  #     #  #    #       #  ")
        print("#  #    #     #  #     #  #    #       #  ")
        print("#   #   #     #  #     #  #    #       #  ")
        print("#    #  #     #  #     #  ######  ######  ")
        print("\n")
        takeinput()

    elif rand==2:
        print("\n");
        print("#     #     #     ######     #     #     #  ")
        print("#     #   #   #   #    #   #   #   # #   #  ")
        print("#     #  #     #  #    #  #     #  #  #  #  ")
        print("#     #  #     #  #    #  #######  #  #  #  ")
        print("#     #  #######  ######  #     #  #   # #  ")
        print("#     #  #     #  # #     #     #  #   # #  ")
        print(" #   #   #     #  #  #    #     #  #   # #  ")
        print("  # #    #     #  #   #   #     #  #    ##  ")
        print("   #     #     #  #    #  #     #  #     #  ")
        print("\n")
        takeinput()

    elif rand==3:
        print("\n");
        print("######     #     ######  #    #     #       ###     #    #       ")
        print("#        #   #   #    #  #    #   #  #       #    #  #   #       ")
        print("#       #     #  #    #  #    #  #    #      #   #    #  #       ")
        print("#       #     #  #    #  #    #  #    #      #   #    #  #       ")
        print("#       #######  ######  #    #  ######      #   ######  #       ")
        print("#       #     #  # #     #    #  #    #      #   #    #  #       ")
        print("#       #     #  #  #     #   #  #    #      #   #    #  #       ")
        print("#       #     #  #   #     # #   #    #  #   #   #    #  #       ")
        print("######  #     #  #    #     #    #    #  #####   #    #  ######  ")
        print("\n")
        takeinput()

    elif rand==4:
        print("\n");
        print("#       #     #     ######  ######  ######  #       #       ######  ")
        print("#   #   #   #   #   #    #  #       #       #       #       #    #  ")
        print("#   #   #  #     #  #    #  #       #       #       #       #    #  ")
        print("#   #   #  #     #  #    #  #       #       #       #       #    #  ")
        print("#   #   #  #######  ######  #       ######  #       #       #    #  ")
        print("#       #  #     #  # #     #       #       #       #       #    #  ")
        print("#       #  #     #  #  #    #       #       #       #       #    #  ")
        print("#       #  #     #  #   #   #       #       #       #       #    #  ")
        print("#       #  #     #  #    #  ######  ######  ######  ######  ######  ")
        print("\n")
        takeinput()

    elif rand==5:
        print("\n");
        print("######     #     ######  ######  #       #  #####  ######  ######  ")
        print("#        #   #   #       #       #   #   #    #    #    #  #    #  ")
        print("#       #     #  #       #       #   #   #    #    #    #  #    #  ")
        print("#       #     #  #       #       #   #   #    #    #    #  #    #  ")
        print("#       #######  ######  ######  #   #   #    #    ######  #    #  ")
        print("#       #     #       #  #       #       #    #    # #     #    #  ")
        print("#       #     #       #  #       #       #    #    #  #    #    #  ")
        print("#       #     #       #  #       #       #    #    #   #   #    #  ")
        print("######  #     #  ######  ######  #       #  #####  #    #  ######  ")
        print("\n")
        takeinput()

    elif rand==6:
        print("\n");
        print("#    #  ######  ######  ######  ######  ")
        print("#   #   #    #  #    #  #    #  #       ")
        print("#  #    #    #  #    #  #    #  #       ")
        print("# #     #    #  #    #  #    #  #       ")
        print("#       ######  #    #  #    #  ######  ")
        print("# #     # #     #    #  #    #       #  ")
        print("#  #    #  #    #    #  #    #       #  ")
        print("#   #   #   #   #    #  #    #       #  ")
        print("#    #  #    #  ######  ######  ######  ")
        print("\n")
        takeinput()

    elif rand==7:
        print("\n");
        print("#       #  ######  #       ######  #####  ######  ")
        print("#   #   #  #    #  # #     #    #    #    #       ")
        print("#   #   #  #    #  #  #    #    #    #    #       ")
        print("#   #   #  #    #  #   #   #    #    #    #       ")
        print("#   #   #  #    #  #    #  ######    #    #       ")
        print("#       #  #    #  #   #   # #       #    #       ")
        print("#       #  #    #  #  #    #  #      #    #       ")
        print("#       #  #    #  # #     #   #     #    #       ")
        print("#       #  ######  #       #    #  #####  ######  ")
        print("\n")
        takeinput()

    elif rand==8:
        print("\n")
        print("######     #     #       ######  ")
        print("#    #   #   #   #       #       ")
        print("#    #  #     #  #       #       ")
        print("#    #  #     #  #       #       ")
        print("######  #######  #       ######  ")
        print("#    #  #     #  #       #       ")
        print("#    #  #     #  #       #       ")
        print("#    #  #     #  #       #       ")
        print("######  #     #  ######  ######  ")
        print("\n")
        takeinput()

    elif rand==9:
        print("\n");
        print("#    #     #     ######     #     ######  #       ")
        print("#    #   #   #        #   #   #   #    #  # #     ")
        print("#    #  #     #      #   #     #  #    #  #  #    ")
        print("#    #  #     #     #    #     #  #    #  #   #   ")
        print("######  #######     #    #######  ######  #    #  ")
        print("#    #  #     #    #     #     #  # #     #   #   ")
        print("#    #  #     #    #     #     #  #  #    #  #    ")
        print("#    #  #     #   #      #     #  #   #   # #     ")
        print("#    #  #     #  ######  #     #  #    #  #       ")
        print("\n")
        takeinput()

    elif rand==10:
        print("\n");
        print("######  ######  #       #  ######  ######  #       #     #     ")
        print("#    #  #       # #     #       #  #       #   #   #   #   #   ")
        print("#    #  #       # #     #      #   #       #   #   #  #     #  ")
        print("#    #  #       #  #    #      #   #       #   #   #  #     #  ")
        print("######  ######  #  #    #     #    ######  #   #   #  #######  ")
        print("#    #  #       #   #   #     #    #       #       #  #     #  ")
        print("#    #  #       #   #   #    #     #       #       #  #     #  ")
        print("#    #  #       #    #  #   #      #       #       #  #     #  ")
        print("######  ######  #     # #  ######  ######  #       #  #     #  ")
        print("\n")
        takeinput()

    elif rand==11:
        print("\n");
        print("######  ######  #    #  ######  #####  ######  #####  ######  ")
        print("#       #    #  #    #  #    #    #    #    #    #    #       ")
        print("#       #    #  #    #  #    #    #    #    #    #    #       ")
        print("#       #    #  #    #  #    #    #    #    #    #    #       ")
        print("#       #    #  #    #  ######    #    #    #    #    ######  ")
        print("#       #    #  #    #  # #       #    #    #    #         #  ")
        print("#       #    #  #    #  #  #      #    #    #    #         #  ")
        print("#       #    #  #    #  #   #     #    #    #    #         #  ")
        print("######  ######  ######  #    #    #    ######  #####  ######  ")
        print("\n")
        takeinput()


first()
