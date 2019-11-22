def takeinput():
    command=input(">")
    checking_command(command)

def checking_command(command):
    if command=="help":
        help()
    if command=="lookip":
        lookip()
    if command=="banner":
        banner()
    if command=="testcon":
        testcon()
    if command=="credir":
        credir()
    if command=="crefile":
        crefile()
    if command=="remdir":
        remdir()
    if command=="remfile":
        remfile()
    if command=="visitsite":
        vstsite()
    if command=="traceip":
        traceip()

def traceip():
    print("This command will trace the specified ip")
    takeinput()

def vstsite():
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
    print("vstsite                Opens the specified site in the default web browser")
    print("traceip                Traces the specified ip")
    print("lookip                 Displays ip address of the device")
    print("banner                 Displays different background pic each time we type this command")
    print("testcon                Checks whether there is internet connection or not")
    takeinput()

def lookip():
    print("This command will display ip address of the device")
    takeinput()

def banner():
    print("This command will display different banner each time we type this command")
    takeinput()

def testcon():
    print("This command will check whether there is internet connection or not")
    takeinput()

def credir():
    print("This command will create directory in specified location")

print("##########################################################")
print("               Welcome to Command Line                    ")
print("\n")
takeinput()
