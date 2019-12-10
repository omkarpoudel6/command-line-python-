#!/usr/bin/env python3


import random
import sys
import webbrowser
import os
import socket
import requests
import bs4
import shutil

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
    elif command=="urlip":
        urlip()
    elif command=="lsdir":
        lsdir()
    elif command=="exit":
        exit()
    else:
        print("The specified command is not recognized")
        takeinput()

def lsdir():
    print("displays all files of current directory")

def urlip():
    print("(urlip)>",end=" ")
    hostname=input()
    if hostname=="back":
        takeinput()
    else:
        try:
            hostip=socket.gethostbyname(hostname)
            print("IP: ",hostip)
        except:
            print("Enter Valid URL")
    takeinput()

def pwdir():
    print(os.getcwd())
    takeinput()

def dirch():
    dir=input("(dirch)>")
    if dir=="back":
        takeinput()
    elif dir=="help":
        print("Commands                           Description")
        print("\n")
        print("credir                             Creates a new directory in the current directory")
        print("crefile                            Creates a new file in the current directory")
        print("remfile                            Removes specified file for the current directory")
        print("remdir                             Removes empty directory for the current directory")
        print("cremdir                            Removes directory for the current directory")
        print("back                               Rolls back to change directory command")
        dirch()
    else:
        try:
            os.chdir(dir)
            print("(",dir,")>>",end=" ")
            command1=input()
            if command1=="credir":
                credir(dir)
            elif command1=="crefile":
                crefile(dir)
            elif command1=="remfile":
                remfile(dir)
            elif command1=="remdir":
                remdir(dir)
            elif command1=="cremdir":
                cremdir(dir)
            elif command1=="back":
                dirch()
        except:
            print("Error!!! enter valid path")
            dirch()


def devip():
    print("Displays all the devices ip address connected to the network")
    print("(devip)>>",end="")
    ip=input()
    if ip=="back":
        takeinput()
    else:
        try:
            command="nmap -sP "+ip+"/24"
            os.system(command)
            takeinput()
        except:
            print("Invalid ip address!!!")
            devip()


def traceip():
    print("Enter ip address to trace")
    print("(traceip)>>", end="")
    ip = input()
    url = "https://whatismyipaddress.com/ip/%s" % (ip)
    uClient = requests.get(url)
    uClient.close()
    soup = bs4.BeautifulSoup(uClient.text, "html.parser")
    table = soup.findAll("table")
    d = len(table)
    if d == 0:
        print("Enter valid Ip address")
    else:
        for i in range(0, d):
            print(table[i].getText())
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

def remfile(dir):
    print("This command will delete a file from the specified location")
    print("(",dir,") #(remfile)>>",end=" ")
    com=input()
    if com=="back":
        dirch()
    else:
        os.remove(com)
        dirch()

def remdir(dir):
    print("This command will delete a directory from the specified location")
    print("(", dir, ") #(remdir)>>", end=" ")
    com = input()
    if com == "back":
        dirch()
    else:
        coms = dir + com
        os.rmdir(coms)
        dirch()

def cremdir(dir):
    print("This command will delete a directory from the specified location")
    print("(", dir, ") #(cremdir)>>", end=" ")
    com = input()
    if com == "back":
        dirch()
    else:
        print("Are you sure you want to continue this will delete the folder and all it's inside contents y/n: ",end=" ")
        c=input()
        choice=c.lower()
        if choice=="y":
            coms = dir + com
            shutil.rmtree(coms)
        #os.rmdir(coms)
            dirch()
        else:
            dirch()

def crefile(dir):
    print("This command will create a file in specified location")
    print("(",dir,") #crefile>>",end=" ")
    com=input()
    if com=="back":
        dirch()
    else:
        open(com,"w+")
        dirch()
    takeinput()

def help():
    print("This command will show all the available command in this command line")
    print("Commands               Descriptions")
    print("\n")
    print("help                   Displays all the available commands with their description")
    print("credir                 Creates directory in specified location should be used inside dirch command(done)")
    print("crefile                Creates a file in specified location should be used inside dirch command(done)")
    print("remdir                 Deletes a directory from the specified location should be used inside dirch command")
    print("remfile                Deletes a file from the specified location should be used inside dirch command(done)")
    print("openurl                Opens the specified site in the default web browser(done)")
    print("traceip                Traces the specified ip(done)")
    print("checkip                Displays ip address of the device(done)")
    print("banner                 Displays different background pic each time we type this command(done)")
    print("testcon                Checks whether there is internet connection or not(done)")
    print("devip                  Displays all the devices ip address connected to the network")
    print("dirch                  Changes current working dirctory(done)")
    print("pwdir                  Displays the current working directory(done)")
    print("urlip                  Finds ip of specified website(done)")
    print("exit                   Quits the program")
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
        print("#     #     #     ######     #     #     #  ######  ")
        print("#     #   #   #   #    #   #   #   # #   #  #       ")
        print("#     #  #     #  #    #  #     #  #  #  #  #       ")
        print("#     #  #     #  #    #  #######  #  #  #  #       ")
        print("#     #  #######  ######  #     #  #   # #  ######  ")
        print("#     #  #     #  # #     #     #  #   # #  #       ")
        print(" #   #   #     #  #  #    #     #  #   # #  #       ")
        print("  # #    #     #  #   #   #     #  #    ##  #       ")
        print("   #     #     #  #    #  #     #  #     #  ######  ")
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
