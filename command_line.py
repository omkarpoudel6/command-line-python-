import random
import sys
import webbrowser
import os
import socket

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
    elif command=="openurl":
        openurl()
    elif command=="traceip":
        traceip()
    elif command=="devip":
        devip()
    elif command=="exit":
        sys.exit()
    elif command=="dirch":
        dirch()
    elif command=="pwdir":
        pwdir()
    else:
        print("The specified command is not recognized")
        takeinput()

def pwdir():
    print(os.getcwd())
    takeinput()

def dirch():
    dir=input("(dirch)>")
    if dir=="back":
        takeinput()
    elif dir=="help":
        print("hello")
    else:
        try:
            os.chdir(dir)
            print("(",dir,")>>",end=" ")
            command1=input()
            if command1=="credir":
                    credir(dir)
            if command1=="crefile":
                    crefile(dir)
            elif command1=="back":
                dirch()
        except:
            print("Error!!! enter valid path")
            dirch()


def devip():
    print("Displays all the devices ip address connected to the network")


def traceip():
    print("This command will trace the specified ip")
    takeinput()

def openurl():
    #print("This command will open the specified site in the default web browser")
    url=input("(openurl)>>")
    try:
        urls="https://%s"%(url)
        webbrowser.open_new_tab(urls)
    except:
        print("Error!!! enter valid url")
    takeinput()

def remfile():
    print("This command will delete a file from the specified location")
    takeinput()

def remdir():
    print("This command will delete a directory from the specified location")
    takeinput()

def crefile(dir):
    print("This command will create a file in specified location")
    print("(",dir,") #crefile>>",end=" ")
    com=input()
    if com=="back":
        dirch()
    else:
        open(com,"w+")
    takeinput()

def help():
    print("This command will show all the available command in this command line")
    print("Commands               Descriptions")
    print("\n")
    print("help                   Displays all the available commands with their description")
    print("credir                 Creates directory in specified location should be used inside dirch command")
    print("crefile                Creates a file in specified location should be used inside dirch command")
    print("remdir                 Deletes a directory from the specified location should be used inside dirch command")
    print("remfile                Deletes a file from the specified location should be used inside dirch command")
    print("openurl                Opens the specified site in the default web browser")
    print("traceip                Traces the specified ip")
    print("checkip                Displays ip address of the device")
    print("banner                 Displays different background pic each time we type this command")
    print("testcon                Checks whether there is internet connection or not")
    print("devip                  Displays all the devices ip address connected to the network")
    print("dirch                  Changes current working dirctory")
    takeinput()

def checkip():
    print("This command will display ip address of the device")
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("google.com",80))
        print("IP: ",s.getsockname()[0])
    except:
        print("Error!!! there is no internet connection.")
    takeinput()


def testcon():
    print("This command will check whether there is internet connection or not")
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("google.com",80))
        print("There is internet connection.")
    except:
        print("There is no internet connection.")
    takeinput()
    takeinput()

def credir(dir):
    print("This command will create directory in specified location")
    print("(", dir, "#credir)>>", end=" ")
    com = input()
    if com=="back":
        dirch()
    else:
        dir1 = dir + com
        os.mkdir(dir1)
        dirch()

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
